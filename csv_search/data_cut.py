import csv
import sys
import time
from tqdm import tqdm


def cutting(_path, _input_num):
    read_path = _path + "/add_csv.csv"
    csv_list = []
    f = open(read_path, "r")
    reader = csv.reader(f)
    for data in reader:
        csv_list.append(data)


    list_num = len(csv_list)

    cnt = len(csv_list[0])-1
    i = 0
    cut_num = []
    #for data in csv_list:
    for data in tqdm(csv_list, desc='제거할 라인 탐색 중'):
        if i > 0:
            if float(data[cnt]) >= _input_num:
                cut_num.append(i)
                i += 1
        else:
            i += 1
        time.sleep(0.05)

    cut_cnt = 0
    cut_num.reverse()
    #for j in cut_num:
    for j in tqdm(cut_num, desc='라인 제거 중'):
        del csv_list[j]
        cut_cnt += 1
        time.sleep(0.05)

    list_cnt = len(csv_list)
    print("\n■원본 라인 수(헤더포함): %d" %list_num)
    print("■제거한 라인 수: %d" %cut_cnt)
    print("■현재 라인 수(헤더포함): %d" %list_cnt)

    save_path = _path + "/cut_data.csv"
    print("■csv파일로 저장합니다. 경로는 "+ save_path + " 입니다.")

    with open(save_path, 'w', newline="") as f:
        writer = csv.writer(f)
        for data in csv_list:
            writer.writerow(data)
    



if __name__ == "__main__":
    #path = "/home/gwangsik/python_csv_project/result_search/add_csv.csv"
    path = sys.argv[1]
    input_num = int(sys.argv[2])
    cutting(path, input_num)
