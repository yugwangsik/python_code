import sys
import csv
import pandas as pd 
import re

def save_f(_topic, _data_list, _device):
    device_concat = []
    device_concat.append(_data_list[0])
    for i in _data_list:
        i.pop()
        if _device in i:
            device_concat.append(i)
   
    index = len(device_concat) 
    df_device = pd.DataFrame(device_concat)
    df_device.to_csv('device_info.csv', header=False, index=False)
        
    print("■ 디바이스 ", _device, "의 정보를 device_info.csv로 저장했습니다.")
    print("■ ", _device, "라인 수: ", index)
    return None



data_list = []
topic = []
device = sys.argv[1]

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
