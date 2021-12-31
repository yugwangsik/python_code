# -*- coding: utf-8 -*-
import pandas as pd
import os
from datetime import datetime

def search_dir(dir_path, _filelist):

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
        elif os.path.isfile(dir_path + "/" + fname):                #혹은 dir_path에 파일이 있으면 실행
            if file_extension == ".csv" or file_extension == ".CSV":#file_extension이 .csv 혹은 .CSV라면 실행
                _filelist.append(dir_path + "/" + fname)            #_filelist에 저장

    for toDir in dir_list:                                          #dir_list만큼 실행(재귀)
        search_dir(toDir, _filelist)


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


if __name__== "__main__" :

    file_list = []
    _f_limit=1000 
    csvpath = "C:/Users/Keti/Desktop/test"                     #로컬경로

    search_dir(csvpath, file_list)                             #디렉토리에 csv파일이 존재하는가 판단 & 경로 저장

    df = csv_to_df_merge(file_list, _f_limit)                  #df에 저장된 경로에 csv파일을 읽어와서 저장

    date1 = input("시작날짜 -> yyyy-mm-dd hh:mm:ss :")          #사용자가 시작 날짜 입력
    date_time1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')  #입력 날짜를 datetime으로 변환

    date2 = input("종료날짜 -> yyyy-mm-dd hh:mm:ss :")          #사용자가 종료 날짜 입력
    date_time2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')  #입력 날짜를 datetime으로 변환

    date_list = []                                              #데이터 프레임의 날짜 값을 넣을 리스트 생성
    i, _ = df.shape                                             #행과 열의 개수 반환
    cnt = 0                                                     
    
    while(cnt < i):                                             #cnt가 전체 행 개수(i)보다 작을 동안만 반복
        t = datetime.strptime(df[0][cnt], '%Y-%m-%d %H:%M:%S')  #데이터프레임에서 날짜열을 가져와서 dataTime형식으로 변환
        check = (t >= date_time1) and (t <= date_time2)         #데이터프레임의 날짜와 사용자가 입력한 날짜 사이를 구하는 조건
        
        if(check):                                              #True면 실행 (사용자가 입력한 범위 내 날짜)
            p = df.iloc[cnt,:]                                  #True인 날짜의 모든 열 저장
            date_list.append(p)                                 #list에 추가
        
        cnt += 1                                    

    for list in date_list:                                      #사용자가 입력한 날짜에 맞는 데이터 출력
        print(list)
