# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys
from datetime import datetime
import calendar

global_num = 0

def search_dir(dir_path, _filelist, _dirlist):

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



def csv_to_df_merge(_flist, fnum=None): 
    
    if fnum != None :                                               
        _flist = _flist[:fnum] 

    allData = []                                                
    _dataframe = pd.DataFrame()
    for file in _flist:                                             #_flist 만큼 실행
        _csvdf = pd.read_csv(file, skiprows = 3, header = None)     #csv파일 읽어옴
        allData.append(_csvdf)                                      #읽어온 데이터 list에 저장
        del [[_csvdf]]                                              

    _dataframe = pd.concat(allData, axis=0, ignore_index=True)      #저장된 list 데이터프레임으로 합치기
    return _dataframe



def file_dir_cnt(f_cnt, d_cnt, cnt):                                                          #    sys.argv[0]   [1]   [2]
    if cnt > 1:                                             #명령어의 매개변수 개수를 측정 ex) python test.py       1     2
        if sys.argv[1] == 'list':
            print("\n■ 전체 디렉토리 개수: " + str(f_cnt))
            print("■ 전체 csv파일 개수: " + str(d_cnt))
        else:
            return None
    else:
        return None


def df_sort(_df, start_date_time=None, end_date_time=None):
    i, _ = _df.shape
    check = True
    cnt = 0
    date_list = []                                                      #데이터 프레임의 날짜 값을 넣을 리스트 생성
    date_sort = []

    while(cnt < i):                                             
        t = datetime.strptime(_df[0][cnt], '%Y-%m-%d %H:%M:%S')             #데이터프레임에서 날짜열을 가져와서 dataTime형식으로 변환
        if start_date_time is not None and end_date_time is not None:
            check = (t >= start_date_time) and (t <= end_date_time)            #데이터프레임의 날짜와 사용자가 입력한 날짜 사이를 구하는 조건
        if(check):
            df_all = _df.iloc[cnt,:]                                            #True인 날짜의 모든 열 저장       
            df_year = _df.iloc[cnt][0]
            date_list.append(df_all)                                 
            date_sort.append(df_year)                     
        cnt += 1

    date_sort = sorted(date_sort)

    j = len(date_list)
    cnt = 0
    cnt2 = 0

    while(cnt < j):
        ds = datetime.strptime(date_sort[cnt], '%Y-%m-%d %H:%M:%S')
        while(cnt2 < j):
            dl = datetime.strptime(date_list[cnt2][0], '%Y-%m-%d %H:%M:%S')
            if ds == dl:
                print(date_list[cnt2])
                cnt2 += 1
            else:
                cnt2 += 1
        cnt += 1
        cnt2 = 0



def select(_num, _file_list, _dir_list, _df, argv_cnt=0):
    global global_num
    try:
        if _num == 1:
            file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt)
            print("전체 데이터 개수: " + str(len(_df)))
            df_sort(_df)

            global_num = 0

        elif _num == 2:
            date1 = input("■ 시작날짜 ex) 2021-06-01 :") + " 00:00:00"            #사용자가 시작 날짜 입력
            date_time1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')          #입력 날짜를 datetime으로 변환
            date2 = input("■ 종료날짜 ex) 2021-12-31 :") + " 23:59:59"            #사용자가 종료 날짜 입력
            date_time2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')          #입력 날짜를 datetime으로 변환

            file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt)
            df_sort(_df, date_time1, date_time2)

            global_num = 0

        elif _num == 3:
            now_year = 2021                                                         #datetime.now().year
            input_m = int(input("■ 월 1~12 ex) 8 :"))           
            day = str(calendar.monthrange(now_year, input_m)[1])
            start = str(now_year) + "-" + str(input_m) + "-" + "01 00:00:00"
            start_date = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
            end = str(now_year) + "-" + str(input_m) + "-" + day + " 23:59:59"
            end_date = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')  

            file_dir_cnt(len(_file_list), len(_dir_list), argv_cnt)
            df_sort(_df, start_date, end_date)
            global_num = 0

        elif _num == 0:
            sys.exit("■ 종료합니다.")
            
    except Exception as e:
        print(e)
        print("\n■ ERROR: 잘못 입력 하셨습니다.\n")
        return None




if __name__== "__main__" :

    file_list = []
    dir_list = []
    _f_limit=1000 
    csvpath = "C:/Users/Keti/Desktop/test"                       #로컬경로

    search_dir(csvpath, file_list, dir_list)                     #디렉토리에 csv파일이 존재하는가 판단 & 경로 저장
    df = csv_to_df_merge(file_list, _f_limit)                    #df에 저장된 경로에 csv파일을 읽어와서 저장


    while(True):
        try:
            if global_num == 1 or global_num == 2 or global_num == 3:
                select(global_num, file_list, dir_list, df, len(sys.argv))
            else:
                print("---------메뉴---------")
                print("0. 끝내기 \n1. 전체 데이터 검색 \n2. 날짜 범위 데이터 검색 \n3. 해당 월만 검색 \n")
                num = int(input("원하는 메뉴의 번호를 입력하세요: "))
                global_num = num
                select(num, file_list, dir_list, df, len(sys.argv))
        except Exception as e:
            print(e)
            print("\n■ ERROR: 다시 입력 하세요.\n")
            continue

            
            

