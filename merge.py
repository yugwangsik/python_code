import pandas as pd
import csv


def plus(_df):
	header_path = "/home/gwangsik/python_csv_project/result_txt/header_field.txt"
	header_line = []
	d_list = []
	f = open(header_path, 'r')

	i = 0

	#while True:
	lines = f.readline()
	print(type(lines))
	print(lines)
	print("========")
	
	lines = lines.split(",")
	print(type(lines))
	print(lines)
	print("========")
	
	for data in _df:
		d_list.append(data)

	for h_lines in lines:
		header_line.append(h_lines)
		d_list.insert(i, h_lines)
		i += 1

#	for add in header_line:
#		if i%2 == 0:
#			print(i)
#			print(add)
#			d_list.insert(i, add)
#			#print(d_list)
#		else:
#			i += 1
#			continue
#		i += 1	
	
	print(d_list)
	print(header_line[0])
	f.close()
	OutputCsv(d_list)


def OutputCsv(_data):
	with open("../output_csv.csv", 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(_data)


