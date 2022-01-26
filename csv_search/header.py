


def open_txt():
    #f = open('/home/gwangsik/python_csv_project/csv_search/result_txt/search_header.txt', 'r')
    f = open('./result_txt/search_header.txt', 'r')
    f_header = f.readline()
    f.close()
    return f_header


if __name__ == '__main__':
    open_txt()
