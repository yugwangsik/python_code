import csv



def pull_csv(_data_path):
	with open(_data_path, newline='') as f:
		print(f)
		reader = csv.reader(f)

	print(reader)
	f.close()
#	print(reader[0])



def indexHeader(_path):
	f = open(_path, 'r', newline='')
	data = f.readline()
	print(data[0])
	f.close()


if __name__ == "__main__" :
	path = '/home/gwangsik/python_csv_project/csv_search/result_txt/seach_header.txt'
	data_path = '/home/gwangsik/python_csv_project/result_search/output_csv.csv'

	pull_csv(data_path)
#	indexHeader(path)
