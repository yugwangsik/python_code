
# -*- coding: utf-8 -*-
#Author : https://github.com/jeonghoonkang

#import text as txt
import pandas as pd
import os
import sys 
import pickle
import info #read info for processing
import gc


def change_string_to_arry(fstring):
    sub_buf=[]
    _line_num = 0

    _firstlist = fstring.split(",")   
    print (_firstlist)
    _range_end = len(_firstlist)
    print ("length of list :", _range_end)

    return _firstlist


def df_rm_header(dfobj, lines=1):
    #csvobj remove header #lines of line
    return dfobj 


def recursive_search_dir(_nowDir, _filelist):                              # 경로 확인 및 파일(폴더)가 존재하는지 체크하는 함수
    print(" [r-loop] CSV recursive searching ", _nowDir)

    if os.path.isfile(_nowDir):                                            # os.path.isfile() 파일이 존재하면 true반환
        file_extension = os.path.splitext(_nowDir)[1]                      # os.path.splitext()[1] 파일의 확장자만 반환 but, os.path.splitext() 파일경로 반환
        if file_extension == ".csv" or file_extension == ".CSV":           # 윗줄에서 반환 된 확장자가 .csv 파일이면 실행
            _filelist.append(_nowDir)                                      # _filelist에 경로를 append
        return None

    dir_list = []  # 현재 디렉토리의 서브디렉토리가 담길 list                 
    f_list = os.listdir(_nowDir)                                           # 경로 내의 모든 파일과 디렉토리를 반환
    for fname in f_list:
        file_extension = os.path.splitext(fname)[1]                        # os.path.splitext()[1]로 확장자를 반환 받음
        if os.path.isdir(_nowDir + "/" + fname):                           # os.path.isdir()로 현재 디렉토리의 하위 디렉토리가 존재하는지 판단(존재하면 true반환)
            dir_list.append(_nowDir + "/" + fname)                         # 현재 디렉토리의 하위 디렉토리들을 리스트로 만듬
        elif os.path.isfile(_nowDir + "/" + fname):                        # os.path.isfile()로 현재 디렉토리에 파일이 있는지 판단(존재하면 true반환)
            if file_extension == ".csv" or file_extension == ".CSV":
                _filelist.append(_nowDir + "/" + fname)

    for toDir in dir_list:
        recursive_search_dir(toDir, _filelist)


def printProgressBar(iteration, total, prefix = 'Progress', suffix = 'Complete',\
                      decimals = 1, length = 50, fill = '█'): 
    # 작업의 진행상황을 표시
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' %(prefix, bar, percent, suffix), end='\r')
    sys.stdout.flush()
    if iteration == total:
        print("...done")


def csv_to_df_merge(_flist, fnum=None): #csv 파일을 하나의 dataframe 으로 변환 
    
    if fnum != None :
        _flist = _flist[:fnum] #fnum 갯수로 제한

    allData = []# 읽어 들인 csv파일 내용을 저장할 빈 리스트를 하나 만든다
    _dataframe = pd.DataFrame()                                                          # _dataframe을 데이터프레임으로 만듬
    cnt = 0
    print(" 디렉토리 모든 CSV를 데이터프레임으로 변환중 ...")
    for file in _flist:                                                                 
        cnt += 1
        printProgressBar(cnt, len(_flist))
        _csvdf = pd.read_csv(file, skiprows = 3, header = None)                          # 파일의 맨 윗3줄을 제외하고 읽음
        #allData.append(_csvdf) # 리스트에 추가 
        test_dataframe = _dataframe.append(_csvdf)                                       # test_dataframe에 _dataframe.apped(_csvdf)로 데이터를 계속 이어서 붙임
        del [[_csvdf]]
        gc.collect()                                                                     # gc.collect() 메모리에 가비지메모리를 수거
    
    #_dataframe = pd.concat(allData, axis=0, ignore_index=True)
    print (cnt, "개의 파일을 처리했습니다.. ")
    return test_dataframe

def df_to_csv(_d, _h=None):                   # 데이터프레임을 csv파일로 저장

    if _h != None : 
        print ( "CSV with Header ... in ", df_to_csv.__name__)
        _d.columns = _h
        _d.to_csv("_o_df_2_csv.csv", header=True, index=False) #인덱스 없이 저장
    else :
        print ("CSV without Header ... ")    
        _d.to_csv("_o_df_2_csv.csv", header=False, index=False) 


def _dataframe_print_(_d):
    print (_d.head(10))
    print (_d.sample(20))    
    print (_d.tail(10))


if __name__== "__main__" :

    print ("디렉토리 경로", info.local_path)

    file_list = []
    _d_limit_f_=6000 # 개발에만 사용 일부 파일만 테스트, 테스트 파일 갯수
    csvpath = info.local_path                                                      # info.py 파일에서 local_path를 불러옴

    recursive_search_dir(csvpath, file_list)

    print (file_list[:10])    
    print (" ↑ 처리 대상 파일 중 10개")    
    print (len(file_list))

    df_m = csv_to_df_merge(file_list, _d_limit_f_)
  
   # 피클저장
    __f = open("_o_df.pkl","wb")
    pickle.dump(df_m,__f) 
    __f.close()
    
    # 출력 DF 정보
    print ("Dataframe 라인갯수", len(df_m.index))
    #_dataframe_print_(df_m)

    # CSV용 header 리스트 생성
    _header = info.fields_name
    header_list = change_string_to_arry(_header)
    
    # CSV 파일 저장 
    df_to_csv(df_m, header_list)



    # df_m = pd.read_csv(file_list[0], skiprows = 3, header = None) 
    # df = pd.read_pickle("df.pkl")
    # f = open("df.pkl", "rb")
    # temp = pickle.load(f)
    # f.close() 
    # df = pd.read_csv ('file_name.csv',usecols= ['column_name1','column_name2']) #subset of fields, sep='\t'
    # header=0, default, the first row of the CSV file will be treated as column names, header=None
    # df = pd.read_csv('example.csv', skiprows = 1,header = None)   

    # Ref.
    # https://towardsdatascience.com/how-to-read-csv-file-using-pandas-ab1f5e7e7b58
    # https://www.edureka.co/community/42836/how-to-read-pandas-csv-file-with-no-header

