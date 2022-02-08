# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys
from datetime import datetime
import calendar
import pickle
import numpy as np

import merge

global_num = int(sys.argv[2])
pd.set_option('display.max_rows', None)

def search_dir(dir_path, _filelist, _dirlist):

	try:
		if os.path.isfile(dir_path):                                    #해당 디렉토리에 csv파일이 있는지 판단
			file_extension = os.path.splitext(dir_path)[1]              #splitext()[1] 확장자만 반환  but, splitext() 전체경로 및 확장자까지 반환
			if file_extension == ".csv" or file_extension == ".CSV":    #확장자가 .csv 혹은 .CSV라면 실행
				_filelist.append(dir_path)                              #csv파일 list에 추가
			return None

		dir_list = []
		f_list = os.listdir(dir_path)                                   #현재 경로에 모든 파일 및 디렉토리 반환
		for fname in f_list:                                            
			file_extension = os.path.splitext(fname)[1]                 #리스트에서 확장자만 가져와서 변수에 저장
			if os.path.isdir(dir_path + "/" + fname):                   #dir_path에 디렉토리가 있으면 실행
				dir_list.append(dir_path + "/" + fname)                 #dir_path list에 저장
				_dirlist.append(dir_path + "/" + fname)
			elif os.path.isfile(dir_path + "/" + fname):                #혹은 dir_path에 파일이 있으면 실행
				if file_extension == ".csv" or file_extension == ".CSV":#file_extension이 .csv 혹은 .CSV라면 실행
					_filelist.append(dir_path + "/" + fname)            #_filelist에 저장

		for toDir in dir_list:                                          #dir_list만큼 실행(재귀)
			search_dir(toDir, _filelist, _dirlist)
	except Exception as e:
		print(e)
		print("탐색할 csv파일이 없습니다.")
		print(dir_path + "경로에 csv파일을 준비하세요.")
		exit()





def csv_to_df_merge(_flist, fnum=None): 
    if fnum != None :                                               
        _flist = _flist[:fnum] 

    allData = []                                                
    _dataframe = pd.DataFrame()
    for file in _flist:                                             #_flist 만큼 실행
        #_csvdf = pd.read_csv(file, skiprows = 3, header = None)     #csv파일 읽어옴
        _csvdf = pd.read_csv(file, skiprows = 1, header = None)     #csv파일 읽어옴i
        date_list = convert(_csvdf)
        #_dtime = datetime.strptime(str(_csvdf[0]), '%Y-%m-%d %H:%M:%S')
        _csvdf.insert(1, "unixtime", date_list)

        allData.append(_csvdf)                                      #읽어온 데이터 list에 저장
        del [[_csvdf]]                                              

    _dataframe = pd.concat(allData, axis=0, ignore_index=True)      #저장된 list 데이터프레임으로 합치기
    return _dataframe






def file_dir_cnt(f_cnt, d_cnt, cnt):                                                          #    sys.argv[0]   [1]   [2]
    if cnt > 1:                                             #명령어의 매개변수 개수를 측정 ex) python test.py       1     2
        if sys.argv[1] == 'list':
            print("\n■ 하위 디렉토리 개수: " + str(d_cnt))
            print("■ 탐색한 csv파일 개수: " + str(f_cnt))
        else:
            return None
    else:
        return None





def convert(__csvdf):
    time_list = []
    for i in __csvdf[0]:
        _dtime = datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S.%f')
        _unix = _dtime.timestamp()
        time_list.append(_unix)

    return time_list

    



def df_sort(_df, start_date_time=None, end_date_time=None):
    try:
        i, _ = _df.shape
        check = True
        cnt = 0
        date_list = []                                                      #데이터 프레임의 날짜 값을 넣을 리스트 생성
        date_sort = []
        __df_sort = pd.DataFrame()
    
        while(cnt < i):      
            t = datetime.strptime(_df[0][cnt], '%Y-%m-%d %H:%M:%S.%f')             #데이터프레임에서 날짜열을 가져와서 dataTime형식으로 변환
            if start_date_time is not None and end_date_time is not None:
                check = (t >= start_date_time) and (t <= end_date_time)            #데이터프레임의 날짜와 사용자가 입력한 날짜 사이를 구하는 조건
            if(check):
                df_all = _df.iloc[cnt,:]                                            #True인 날짜의 모든 열 저장       
                df_year = _df.iloc[cnt][0]
                date_list.append(df_all)                                 
                date_sort.append(df_year)                     
            cnt += 1
    
        date_sort = sorted(date_sort)
        
        
        _first = date_sort[0]
        _last = date_sort[len(date_sort)-1]
        _result = str(len(date_list))
        result_list = []
    
        j = len(date_list)
        cnt = 0
        cnt2 = 0

    
        while(cnt < j):
            ds = datetime.strptime(date_sort[cnt], '%Y-%m-%d %H:%M:%S.%f')
            while(cnt2 < j):
                dl = datetime.strptime(date_list[cnt2][0], '%Y-%m-%d %H:%M:%S.%f')
                if ds == dl:
                    result_list.append(date_list[cnt2])
                    cnt2 += 1
                    break
                else:
                    cnt2 += 1
            cnt += 1
            #cnt2 = 0
    
        __df_sort = pd.concat(result_list, axis=0, ignore_index=True)
        return _first, _last, _result, __df_sort
    except ValueError:
        print("csv파일의 날짜 형식을 확인해주세요.")
        sys.exit(0)



def save_df(_df_, _path, _option1=None, _option2=None):
    print("검색 결과를 pickle 파일로 저장했습니다.")
    print("pickle 파일경로는 " + _path + "/df_data.pkl 입니다.")
    if _option1 == None and _option2 == None:
        save_file = sys.argv[4] + '/select1_allData.txt'
    elif _option2 == None:
        save_file = sys.argv[4] +'/select3_' + _option1 + '.txt'
    elif _option1 is not None and _option2 is not None:
        save_file = sys.argv[4] + '/select2_' + _option1 + '_' + _option2 + '.txt'
    
    with open('df_data.pkl', 'wb') as f:
         pickle.dump(_df_, f)
    print("검색 결과를 " + save_file + " 파일로 저장했습니다.")
    _df_.to_csv(save_file, header=False, index=False, encoding='cp949')
       




def select(_num, _file_list, _df, _dir_list=None, argv_cnt=0):
    global global_num
    try:
        if _num == 1:
            first, last, result, _df_sort = df_sort(_df)
            print("■ 첫번째 데이터: " + first)
            print("■ 마지막 데이터: " + last)
            file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt)
            global_num = 0
   

        elif _num == 2:
            date1 = input("■ 시작날짜 ex) 2021-06-01 :") + " 00:00:00"            #사용자가 시작 날짜 입력
            date_time1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')          #입력 날짜를 datetime으로 변환
            date2 = input("■ 종료날짜 ex) 2021-12-31 :") + " 23:59:59"            #사용자가 종료 날짜 입력
            date_time2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')          #입력 날짜를 datetime으로 변환

            _, _, result, _df_sort = df_sort(_df, date_time1, date_time2)
            file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt)
            print("■ 검색된 데이터 수: " + result)

            global_num = 0
            return _df_sort, date1, date2

        elif _num == 3:
            now_year = 2021                                                         #datetime.now().year
            input_m = int(input("■ 월 1~12 ex) 8 :"))           
            day = str(calendar.monthrange(now_year, input_m)[1])
            start = str(now_year) + "-" + str(input_m) + "-" + "01 00:00:00"
            start_date = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            end = str(now_year) + "-" + str(input_m) + "-" + day + " 23:59:59"
            end_date = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')  

            _, _, result, _df_sort = df_sort(_df, start_date, end_date)
            file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt)
            print("■ 검색된 데이터 수: " + result)
            global_num = 0

            return _df_sort, str(input_m), None

        elif _num == 0:
            sys.exit("■ 종료합니다.")
        
        return _df_sort, None, None
            
    except Exception as e:
        return None





if __name__== "__main__" :

    file_list = []
    dir_list = []
    _f_limit=1000 
    csvpath = sys.argv[3]                       #로컬경로

#    direct_path = sys.argv[5]
#    print(direct_path)
#
#    if direct_path is None:
    search_dir(csvpath, file_list, dir_list)                     #디렉토리에 csv파일이 존재하는가 판단 & 경로 저장
    df = csv_to_df_merge(file_list, _f_limit)                    #df에 저장된 경로에 csv파일을 읽어와서 저장

    if global_num == 1 or global_num == 2 or global_num == 3:
        df_sort, option1, option2 = select(global_num, file_list, df, dir_list, len(sys.argv))
        save_df(df_sort, csvpath, option1, option2)
        merge.plus(df_sort, csvpath)
    else:
        num = int(sys.argv[2])       #int(input("\n원하는 메뉴의 번호를 입력하세요: "))
        global_num = num
        select(num, file_list, df, dir_list, len(sys.argv))

#    else:
#        file_list.append(direct_path)
#	dir_list.append(direct_path)
#        df = csv_to_df_merge(file_list, _f_limit)                    
#
#        if global_num == 1 or global_num == 2 or global_num == 3:
#            df_sort, option1, option2 = select(global_num, file_list, dir_list, df, len(sys.argv))
#            save_df(df_sort, csvpath, option1, option2)
#            merge.plus(df_sort)
#        else:
#            print(len(sys.argv))
#            num = int(sys.argv[2])       #int(input("\n원하는 메뉴의 번호를 입력하세요: "))
#            global_num = num
#            select(num, file_list, dir_list, df, len(sys.argv))
