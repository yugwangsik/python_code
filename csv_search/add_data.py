import csv
import re
import sys

def count():
    path = sys.argv[1] + "/output.csv"

    add_list = []
    f = open(path, 'r')
    rdr = csv.reader(f)
    for data in rdr:
        add_list.append(data)

    f.close()
    add_list.pop()
    add_list[0].pop()

    print("■필드 개수: " + str(len(add_list[0])))
    print("■전체 라인 개수: " + str(len(add_list)))


    line_cnt = 0
    line_nan = 0
    percent_nan = 0

    all_cnt = 0
    for data in add_list:
        for j in range(len(data)):
            if data[j] is not None:
                all_cnt += 1


    cnt = 0
    num = 0
    for data in add_list:
        if num > 0:
            for j in range(len(data)):
                if data[j] is None or data[j] == 'nan':
                    cnt += 1
                    line_cnt += 1
                    line_nan += 1
                else:
                    line_cnt += 1

            add_list[num].append(line_cnt)
            add_list[num].append(line_nan)
            percent_nan = round((line_nan/line_cnt) * 100, 2)
            add_list[num].append(percent_nan)

        line_cnt = 0
        line_nan = 0
        num += 1


    add_list[0].append("라인 총 데이터 수")
    add_list[0].append("NaN 데이터 수")
    add_list[0].append("NaN 비율")

    percent = round((cnt/all_cnt) * 100, 2)


    print("■전체 데이터 개수: %d" %all_cnt)
    print("■전체 NaN 데이터 개수: %d" %cnt)
    print("■전체 NaN 비율: %0.2f%%" %percent)

    return add_list



def save_f(_add_list):
    path = sys.argv[1] + "/add_csv.csv"
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        for data in _add_list:
            writer.writerow(data)

    f.close()



if __name__ == "__main__":
    add = count()
    save_f(add)
