import sys
import csv
import pandas as pd 
import re

def save_f(_topic, _data_list, _device):
#def save_f(_topic, _data_list, _device, _machine):
    device_concat = []
    device_concat.append(_data_list[0])
    d_list = _data_list
    d_list.pop(0)

    cnt = 0 
    name = []
    name.append(_data_list[0][0])   
    for i in d_list:
        i.pop()
        num = i[10]
        if num == '':
            num = 0.0
        
        if _device in i:
        #if float(_machine) == float(num) and _device in i:
        #if float(_machine) == float(num):
        #if float(_machine) == float(num) and i[0] not in name:
            #print(device_concat[cnt][0])
            #print(i[0])
            #print(cnt)
            #name.append(i[0])
            device_concat.append(i)
        #if device_concat[cnt][0] != i[0]:
            #device_concat.append(i)
            #cnt += 1
    #print(name)
    #print(cnt) 
    device_concat.sort()
    device_concat.insert(0, device_concat[len(device_concat)-1])
    device_concat.pop()

    

    index = len(device_concat) 
    df_device = pd.DataFrame(device_concat)
    df_device.to_csv('sender_info.csv', header=False, index=False)
        
    print("■ 디바이스 ", _device, "의 정보를 device_info.csv로 저장했습니다.")
    print("■ ", _device, "라인 수: ", index)
    return None


data_list = []
topic = []
device = sys.argv[1]
#machine = sys.argv[2]

with open('./file_json/result.csv', 'r') as f:
    for line in f:
        row = line.split(",")
        data_list.append(row)


for data in data_list:
    if data[0] not in topic:
        topic.append(data[0])

del topic[0]

with open('device.txt', 'w') as file:
    for i in topic:
        file.write(i+',')

print("■ 총 기기 개수: ", len(topic))

#if device is not 1:
save_f(topic, data_list, device)
#save_f(topic, data_list, device, machine)
