import csv
import re
import sys

def count():
    path = "/home/gwangsik/python_csv_project/result_search/output_csv.csv"
#    f = open(path, 'r')
#    data = f.readline()
#    print(data)
#    f.close()
    add_list = []
    f = open(path, 'r')
    rdr = csv.reader(f)
    for data in rdr:
        add_list.append(data)
    #print(rdr)
    f.close()
    add_list.pop()
    print(add_list)

if __name__ == "__main__":
    count()
