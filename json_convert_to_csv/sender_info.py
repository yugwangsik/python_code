import sys
import csv
import pandas as pd 
import re
import matplotlib.pyplot as pyplot

def save_f(_topic, _data_list, _device):
#def save_f(_topic, _data_list, _device, _machine):
    device_concat = []
    device_concat.append(_data_list[0])
    d_list = _data_list
    d_list.pop(0)

    cnt = 0 
    x_list = []
    y_list = []
    name = []
    name.append(_data_list[0][0])   
    for i in d_list:
        i.pop()
        num = i[10]
        if num == '':
            num = 0.0
        
        #if _device in i:

        text = i[9]
        text = text[-2:]
        #print(i[2])
        unix = float(i[2])
        #print(unix)
        #print(type(unix))
        #if _device in i:
        #if _device in i and (text == "ra" or text == "RA"):
        if _device in i and text == "va":
            device_concat.append(i)

    device_concat.sort()
    device_concat.insert(0, device_concat[len(device_concat)-1])
    device_concat.pop()

    num = 0
 
    for data in device_concat:
        if num == 0:
            num += 1
        else:
            if data[15] == '':
                x_list.append(data[2])
                y_list.append(0.0)
            else:
                x_list.append(data[2])
                y_list.append(float(data[15]))
    
    x_list.pop(0)
    y_list.pop(0)

    label = []
    val = len(x_list)
    i = 0
    j = 0
    while j <= val-1:
        if i >= 3:
            i = 0

        if i == 0:
            label.append(x_list[j])
            i += 1
            j += 1
        else:
            label.append('')
            j += 1
            i += 1

    label[-1] = (x_list[-1])

    pyplot.rcParams["figure.figsize"] = [10,6]
    pyplot.scatter(x_list, y_list)
    pyplot.plot(x_list, y_list)
    pyplot.tick_params(axis='x', labelsize=7)
    pyplot.xticks(x_list, labels=label)
    pyplot.title('7c87cedb2940 fw_ver = va, msg.ceramic_state.v-position')
    pyplot.show()
    pyplot.savefig('data[15].png')

    index = len(device_concat) 
    df_device = pd.DataFrame(device_concat)
    #a = df_device.drop([2,5,6,7,8], axis='columns')
    df_device.to_csv('sender_info.csv', header=False, index=False)
    #a.to_csv('sender_test.csv', header=False, index=False)
        
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
