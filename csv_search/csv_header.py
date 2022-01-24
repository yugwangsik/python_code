# -*- coding: utf-8 -*-
import os
import csv
import re
import sys

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
					return None

		for toDir in dir_list:                                          #dir_list만큼 실행(재귀)
			search_dir(toDir, _filelist, _dirlist)
	except Exception as e:
		print("csv파일이 없습니다.")


def header(_csv_header, _download_path):
	try:
		#print(_download_path)
		f_name = _download_path + "/header_field.txt"
		f = open(f_name, 'w')
		for field in _csv_header:
			data = field + ","
			f.write(data)

		f.close()
	    
		print(_csv_header)
		return _csv_header
	except Exception as e:
		print("헤더 파일이 없습니다.")





if __name__== "__main__" :
	try:
		file_list = []
		dir_list = []
		_f_limit=1000 
		csvpath = sys.argv[1]                       #로컬경로

		download_path = sys.argv[2]

		#print(download_path)

		search_dir(csvpath, file_list, dir_list)                    #디렉토리에 csv파일이 존재하는가 판단 & 경로 저장
		f_name = str(file_list)
		f_name = re.sub("\[|\]|\'","",f_name)
		f = open(f_name,'r', encoding='UTF8')
		rdr = csv.reader(f)

		csv_list = []

		for line in rdr:
		    csv_list.append(line)

		csv_header = csv_list[2]
		header(csv_header, download_path)

		f.close()
	except Exception as e:
		print("헤더 파일이 없습니다.")

