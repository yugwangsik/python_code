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
			if i == 339:
				j += 1
				listup.insert(j, [])
				i = 0

	print(listup)
	return listup	



def indexHeader(_path):
	buf = []
	test = header.open_txt()
	buf = test
	
	return buf



def make(_data_list, _search_header):
	h_find = _data_list[0]
	
	h_list = []
	for i in range(len(_search_header[0])):
		h_list.append(re.sub(",","",str(_search_header[0][i])))

	#print(_search_header)
	#print(h_list)
	num = []
	cnt = 0
	for i in range(len(h_list)):
		for j in range(len(h_find)):
			if h_list[i] == h_find[j].strip():
				num.append(cnt)
			
			cnt += 1
		cnt = 0
	
	#print(num)
	result = [[]]
	cnt = 0
	#print(_data_list[29])
	for i in range(len(_data_list)-1):
		for j in num:
			#print(i)
			#print(j)
			#print(_data_list[i][j])
			result[cnt].append(_data_list[i][j])
		cnt += 1
		result.insert(cnt,[])
		

	return result



def save_f(_result, __data_path, __save_path, __search_header):
	__d_path = __data_path + "/select_search.csv"

	with open(__d_path, "w", newline='') as f:
		writer = csv.writer(f)
		for data in _result:
			writer.writerow(data)
			print(data)
	f.close()

	print("선택한 헤더에 해당하는 데이터를 저장하였습니다.")
	print("선택한 헤더는 " + str(__search_header) + " 입니다.")
	print("경로는 " + __save_path + " 입니다.")
		



if __name__ == "__main__" :
	
	path = sys.argv[1] + '/search_header.txt'
	data_path = sys.argv[2]
	save_path = sys.argv[3]

	data_list = pull_txt(data_path)
	search_header = indexHeader(path)

	result = make(data_list, search_header)
	save_f(result, data_path, save_path, search_header)







