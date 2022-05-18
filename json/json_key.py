import json
import os
import pickle

def search_dir(dir_path, _filelist, _dirlist):
    try:

        if os.path.isfile(dir_path):                                    
                file_extension = os.path.splitext(dir_path)[1]              
                if file_extension == ".json" or file_extension == ".JSON":    
                    _filelist.append(dir_path)       
                return None                      
                
        dir_list = []
        f_list = os.listdir(dir_path)                                 
        for fname in f_list:                                            
            file_extension = os.path.splitext(fname)[1]                
            if os.path.isdir(dir_path + "/" + fname):                  
                dir_list.append(dir_path + "/" + fname)                
                _dirlist.append(dir_path + "/" + fname)
            elif os.path.isfile(dir_path + "/" + fname):                
                if file_extension == ".json" or file_extension == ".JSON":
                    _filelist.append(dir_path + "/" + fname)

        for toDir in dir_list:                                          
            search_dir(toDir, _filelist, _dirlist)
    except Exception as e:
        print(e)


file_list = []
dir_list = []
jpg_list = []
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/다세대주택/구조물(균열)/보통/RGB' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/다세대주택/구조물(균열)/보통' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/다세대주택/구조물(균열)' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/다세대주택' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/단독주택' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/비주거용주택' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/아파트' 
#jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터/연립주택' 
jsonpath = '/home/e8ight_data/482Gdataset_origin/라벨링_데이터' 
search_dir(jsonpath, file_list, dir_list)   


for i in file_list:
    with open(i, encoding='utf-8') as f:
        data = json.load(f)
        j_name = data['Learning_Data_Info']['Json_Data_ID'] + '.jpg'
        jpg_list.append(j_name)

#print(len(file_list))

#print(type(jpg_list[1]))

with open('json_text.txt', 'w') as f:
    for line in jpg_list:
        f.write(line + '\n')
    #pickle.dump(jpg_list, f)

#with open('test.txt', 'rb') as f:
#    text = pickle.load(f)
    
