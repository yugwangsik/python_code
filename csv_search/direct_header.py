# -*- coding: utf-8 -*-
import os
import csv
import re
import sys
import time
from tqdm import tqdm


def header(_csv_header, _download_path):
	try:
		h_list = []
		f_name = _download_path + "/header_field.txt"
		f = open(f_name, 'w')
		_csv_header.insert(1,"UnixTime")
		for field in _csv_header:
			data = field 
			f.write(str(data))
			h_list.append(data)

		f.close()
	    
		print(h_list)
		_num = len(h_list)
		
		return _csv_header, _num
	except Exception as e:
		print("Error: csv_header.py")
		print("경로가 맞지 않아 파일을 저장할 수 없습니다.")





if __name__== "__main__" :
	try:
		file_list = []
		dir_list = []
		_f_limit=1000 
		csvpath = sys.argv[1]                       #로컬경로

		download_path = sys.argv[2]

		file_list.append(sys.argv[1])
		f_name = str(file_list)
		f_name = re.sub("\[|\]|\'","",f_name)
		f = open(f_name,'r', encoding='UTF8')
		rdr = csv.reader(f)

		csv_list = []
		csv_list.append(next(rdr))

		_, num = header(csv_list, download_path)

		f.close()
		print("\nheader 파일의 경로는 " + sys.argv[2] + "/header_field.txt")
		print("원하는 헤더의 검색을 원할 경우 " + sys.argv[2] + "/search_header.txt 수정하세요.")
	except Exception as e:
		print("헤더 파일이 없습니다.")

