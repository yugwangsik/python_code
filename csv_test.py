# -*- coding: utf-8 -*-
import pandas as pd
import os
import sys 
import gc
import time
from datetime import datetime

def search_dir(dir_path, _filelist):

    if os.path.isfile(dir_path):
        file_extension = os.path.splitext(dir_path)[1]
        if file_extension == ".csv" or file_extension == ".CSV":
            _filelist.append(dir_path)
        return None

    dir_list = []  
    f_list = os.listdir(dir_path)
    for fname in f_list:
        file_extension = os.path.splitext(fname)[1]
        if os.path.isdir(dir_path + "/" + fname):
            dir_list.append(dir_path + "/" + fname)
        elif os.path.isfile(dir_path + "/" + fname):
            if file_extension == ".csv" or file_extension == ".CSV":
                _filelist.append(dir_path + "/" + fname)

    for toDir in dir_list:
        search_dir(toDir, _filelist)


def csv_to_df_merge(_flist, fnum=None): 
    
    if fnum != None :
        _flist = _flist[:fnum] 

    allData = []
    _dataframe = pd.DataFrame()
    for file in _flist:
        #_csvdf = pd.read_csv(file, encoding='cp949') 
        _csvdf = pd.read_csv(file, skiprows = 3, header = None) 
        #_dataframe = pd.DataFrame(_csvdf, columns=[''])
        allData.append(_csvdf)
        #allData.append(_csvdf.iloc[:,0])
        #print(allData)
        #print(_csvdf.iloc[:,0])
        #print(_csvdf)
        #print(pd.to_datetime(_csvdf[0]))     
        #test = _dataframe.append(_csvdf)
        print("-----------------------------------------------")
        #print(test) 
        #print(allData[0])
        del [[_csvdf]]

    _dataframe = pd.concat(allData, axis=0, ignore_index=True)
    #print(_dataframe.columns[5])
    #print(_dataframe.)
    return _dataframe


def index():
    x = input("행을 입력하시오.")
    y = input("열을 입력하시오.")
    return x, y


if __name__== "__main__" :

    file_list = []
    _f_limit=1000 
    csvpath = "C:/Users/Keti/Desktop/test"

    search_dir(csvpath, file_list)

    df = csv_to_df_merge(file_list, _f_limit)

    #print(df_m[0][0])
    #x, y = index()
    #epoch_time = 1639502344
    #time_val = time.localtime(epoch_time)
    #time_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))

    date1 = input("yyyy-mm-dd hh:mm:ss :")                      #사용자가 날짜 시작 범위 입력
    date_time1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')  #입력 날짜를 datetime으로 변환

    date2 = input("yyyy-mm-dd hh:mm:ss :")
    date_time2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    date_list = []              #데이터 프레임의 날짜 값을 넣을 리스트 생성
    i, j = df.shape             #행과 열의 개수 반환
    cnt = 0

    while(cnt < i):
        t = datetime.strptime(df[0][cnt], '%Y-%m-%d %H:%M:%S')
        
        if((t >= date_time1) and (t <= date_time2)):
            date_list.append(t)
            print(t)

        cnt += 1


    #unix_test = '1970-01-01 00:00:00'
    #date_time = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')                 # 입력 값을 datetime으로 변환
    #unix_time = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').timestamp()     # 입력 값을 unixtime으로 변환
    #unix_datetime = 

    #tt = (df.timestamp == date_time)

    #print(df[0][0])
    #print(df_m.loc[tt])

    
    #print(date_time)    #입력 날짜 UnixTime 변환
    #print(unix_time)
    #print(date_time - unix_datetime)

    
    
    #print(time_val)
    #print(time_formatted)

    #print (x, y)
    #print(df_m.iloc[:,0]) #날짜 열만 가져오기
    #print(df_m.at_time('08:31'))
    #a = df_m.iloc[[x,y]]
    #print(a)
