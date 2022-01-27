import csv
import re
import sys
import header

def pull_txt(_data_path):
	_d_path = _data_path + "/output.txt"

	f = open(_d_path, 'r')
	line = f.readline()
	line = line.split(",")
	
	
	i = 0
	j = 0
	listup = [[]]
	for data in line:
		if data != '':
			listup[j].append(data)
			i += 1
			if i == 169:
				j += 1
				listup.insert(j, [])
				i = 0

	
	return listup	



def indexHeader(_path):
	buf = []
#	f = open(_path, 'r', newline='')
#	data = f.readline()
#	data = data.strip()
#	data = re.sub("\'|\'|\[|\]","",data)
#	data = data.split(",")
	
	#data = data.lstrip

	

	#print(data)
	#f.close()
	print(type("header.open_txt()"))
	eval("header.open_txt()")
	
	print(eval("header.open_txt()"))
	
	print(buf)
	
	return buf



def make(_data_list, _search_header):
	h_find = _data_list[0]
	#print(h_find)
	#print(_search_header[0])
	find_num = [i for j in range(len(_search_header)) for i in range(len(h_find)) if _search_header[j] in h_find[i]]

	find_num = set(find_num)
	find_num = list(find_num)
	find_num = sorted(find_num)
	
	cnt = 0
	result_list = [[]]
	for i in range(len(_data_list)-1):
		for j in find_num:
			result_list[cnt].append(_data_list[cnt][j])
		cnt += 1
		result_list.insert(cnt,[])
#	result_list = [[]]
#	for i in range(len(_search_header)):
#		for j in range(len(h_find)):
#			if _search_header[i] == h_find[j]:
#				result_list[i].append(_data_list[i][j])
#		result_list.insert(i+1,[])
#
#	print(result_list)	
	return result_list



def save_f(_result, __data_path, __search_header):
	__d_path = __data_path + "/select_search.csv"

	with open(__d_path, "w", newline='') as f:
		writer = csv.writer(f)
		for data in _result:
			writer.writerow(data)
	f.close()

	print("선택한 헤더에 해당하는 데이터를 저장하였습니다.")
	print("선택한 헤더는 " + str(__search_header) + " 입니다.")
	print("경로는 " + __d_path + " 입니다.")
		



if __name__ == "__main__" :
	
	path = sys.argv[1] + '/search_header.txt'
	data_path = sys.argv[2]

	data_list = pull_txt(data_path)
	search_header = indexHeader(path)

	result = make(data_list, search_header)
	save_f(result, data_path, search_header)







