import pandas as pd
import csv
import time
from tqdm import tqdm

def plus(_df, path):
	try:
		header_path = path + "/data_txt/header_field.txt"
		header_line = []
		d_list = [[]]
		add_list = [[]]


		f = open(header_path, 'r')

		i = 0
		j = 0

		lines = f.readline()
		lines = lines.split(",")
		
		#for data in _df:
		#for data, progress in zip(_df, tqdm(_df, desc='헤더와 데이터프레임 합치는 중')):
		for data in tqdm(_df, desc='헤더와 데이터프레임 합치는 중'):
			d_list[i].append(data)
			j += 1
			if j == 339:
				d_list.extend([[]])
				i += 1
				j = 0
			time.sleep(0.0001)

		
		d_list.insert(0,[])
		k = 0
		for h_lines in lines:
			d_list[0].append(h_lines)
		
		
		f.close()
		OutputCsv(d_list)
	except Exception as e:
		print("Error: merge.py")
		print("경로를 찾을 수 없습니다.")


def OutputCsv(_data):
	with open("../result_search/output.csv", 'w', newline='') as f:
		writer = csv.writer(f)
		for data_list in _data:
			writer.writerow(data_list)
	
	
#	with open("../result_search/output.txt", 'w') as f:
#		for data_list in _data:
#			for val in data_list:
#				f.write(str(val)+",")
#		
	f.close()
