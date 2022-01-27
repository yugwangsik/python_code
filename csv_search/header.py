


def open_txt():
    buf = []
    #f = open('/home/gwangsik/python_csv_project/csv_search/result_txt/search_header.txt', 'r')
    f = open('./result_txt/search_header.txt', 'r')
    f_header = f.readline()
    print(f_header)
    #print(buf)
    exec(f_header)
    f.close()
    print(buf)
    return buf


if __name__ == '__main__':
    open_txt()
