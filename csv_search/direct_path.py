# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys
from datetime import datetime
import calendar
import pickle
import numpy as np
import time
from tqdm import tqdm

import merge

global_num = int(sys.argv[1])
pd.set_option('display.max_rows', None)


def csv_to_df_merge(_flist, fnum=None): 
    if fnum != None :                                               
        _flist = _flist[:fnum] 

    allData = []                                                
    _dataframe = pd.DataFrame()
    for file in tqdm(_flist, desc='csv 읽는 중'):                                             #_flist 만큼 실행
    #for file in _flist:                                             #_flist 만큼 실행
        _csvdf = pd.read_csv(file, skiprows = 1, header = None)     #csv파일 읽어옴i
        date_list = convert(_csvdf)
        _csvdf.insert(1, "unixtime", date_list)
        #print("1")

        allData.append(_csvdf)                                      #읽어온 데이터 list에 저장
        del [[_csvdf]]
        time.sleep(0.0001)                                              

    _dataframe = pd.concat(allData, axis=0, ignore_index=True)      #저장된 list 데이터프레임으로 합치기
    return _dataframe




def convert(__csvdf):
    time_list = []
    for i in tqdm(__csvdf[0], desc='UnixTime 추가 생성 중'):
        #print("2")
        _dtime = datetime.strptime(str(i), '%Y-%m-%d %H:%M:%S.%f')
        _unix = _dtime.timestamp()
        time_list.append(_unix)
        time.sleep(0.0001)

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
            #print("3")
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

        #for data in tqdm(_df, desc='데이터 정렬 중'): 
        for data in _df:
            #print("4")
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
            #time.sleep(0.0001)
            #cnt2 = 0
    
        __df_sort = pd.concat(result_list, axis=0, ignore_index=True)
        return _first, _last, _result, __df_sort
    except ValueError:
        print("csv파일의 날짜 형식을 확인해주세요.")
        sys.exit(0)



def save_df(_df_, _path, _option1=None, _option2=None):
    print("검색 결과를 pickle 파일로 저장했습니다.")
    print("pickle 파일경로는 ./df_data.pkl 입니다.")
    if _option1 == None and _option2 == None:
        save_file = sys.argv[3] + '/select1_allData.txt'
    elif _option2 == None:
        save_file = sys.argv[3] +'/select3_' + _option1 + '.txt'
    elif _option1 is not None and _option2 is not None:
        save_file = sys.argv[3] + '/select2_' + _option1 + '_' + _option2 + '.txt'
    
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
            #file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt, _path_type)
            global_num = 0
   

        elif _num == 2:
            date1 = input("■ 시작날짜 ex) 2021-06-01 :") + " 00:00:00"            #사용자가 시작 날짜 입력
            date_time1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')          #입력 날짜를 datetime으로 변환
            date2 = input("■ 종료날짜 ex) 2021-12-31 :") + " 23:59:59"            #사용자가 종료 날짜 입력
            date_time2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')          #입력 날짜를 datetime으로 변환

            _, _, result, _df_sort = df_sort(_df, date_time1, date_time2)
            #file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt, _path_type)
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
            #file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt, _path_type)
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
    csvpath = sys.argv[4]                       #로컬경로
    path_type = sys.argv[4]
#    direct_path = sys.argv[5]
#    print(direct_path)

#    if direct_path is None:
 
    #search_dir(csvpath, file_list, dir_list)                     #디렉토리에 csv파일이 존재하는가 판단 & 경로 저장
    file_list.append(sys.argv[2])    

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
