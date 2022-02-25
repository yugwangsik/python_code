import pandas as pd
import json
import os
import re
import sys


def search_dir(dir_path, _filelist, _dirlist):
    if os.path.isfile(dir_path):
        file_extension = os.path.splitext(dir_path)[1]
        if file_extension == ".json" or file_extension == ".JSON":
            _filelist.append(dir_path)
        return None

    dir_list = []
    f_list = os.listdir(dir_path)
    for fname in f_list:
        file_extension = os.path.splitext(fname)[1]
        if os.path.isdir(dir_path + "/" + fname):
            dir_list.append(dir_path + "/" + fname)
            _dirlist.append(dir_path + "/" + fname)
        elif os.path.isfile(dir_path + "/" + fname):
            if file_extension == ".json" or file_extension == ".JSON":
                _filelist.append(dir_path + "/" + fname)

    for toDir in dir_list:
        search_dir(toDir, _filelist, _dirlist)
            

def json_concat(_filst):
    data_list = []
    for f in _filst:
        with open(f, 'r') as fname:  
            d = fname.readline()
            data = json.loads(d)
            data_list.extend(data)
    
    df = pd.json_normalize(data_list)
    y, x = df.shape
    df.to_csv("./file_json/result.csv", index=False)

    header = list(df)
    print("↓↓헤더 정보↓↓ ")
    print(header)
    print("■ 결과 파일은 ./file_json/result.csv로 저장되었습니다. ")
    print("■ 전체 필드 개수: ", x)
    print("■ 전체 라인 개수: ", y)

if __name__ == '__main__':
    k_list = []
    file_list = []
    dir_list = []
    path = sys.argv[1]
    
    search_dir(path, file_list, dir_list)
    json_concat(file_list)

#with open('gwangik_006580.json', 'r') as f:
#    d = f.readline()
#    data = json.loads(d)
#    print(type(data))
#    print(data)
#
#    for i in range(len(data)):
#        key = str(data[i]["msg"].keys()).replace("dict_keys([", "")
#        key = key.replace("])", "")
#        key = key.replace("'", "")
#        key = key.replace(" ", "")
#        key = key.split(",")
#        if i == 0:
#            k_list = key
#            continue
#
#        for num in key:
#            if num not in k_list:
#                k_list.append(num)
#
#    #print(k_list)
#            
#    df = pd.json_normalize(data)
#    df.to_csv("test.csv", index=False)
#    df.to_csv("test.csv", header=False, index=False)
