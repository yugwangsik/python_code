import os
import pickle

def search_dir(dir_path, _filelist, _dirlist, _savelist):
    try:

        if os.path.isfile(dir_path):                                    
                file_extension = os.path.splitext(dir_path)[1]              
                if file_extension == ".jpg" or file_extension == ".JPG":    
                    _filelist.append(dir_path)
                    _savelist.append(dir_path)
                return None                      
                

        dir_list = []
        f_list = os.listdir(dir_path)                                 
        for fname in f_list:                                            
            file_extension = os.path.splitext(fname)[1]                
            if os.path.isdir(dir_path + "/" + fname):                  
                dir_list.append(dir_path + "/" + fname)                
                _dirlist.append(dir_path + "/" + fname)
            elif os.path.isfile(dir_path + "/" + fname):                
                if file_extension == ".jpg" or file_extension == ".JPG":
                    #_filelist.append(dir_path + "/" + fname)
                    _filelist.append(os.path.splitext(fname)[0] + ".jpg")
                    _savelist.append(os.path.splitext(fname)[0] + ".jpg")
                    #_filelist.append(fname)

        for toDir in dir_list:                                          
            search_dir(toDir, _filelist, _dirlist, _savelist)
    except Exception as e:
        print(e)


file_list = []
save_list = []
dir_list = []
fail_list = []
text = []

#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/다세대주택/구조물(균열)/보통/RGB' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/다세대주택/구조물(균열)/보통' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/다세대주택/구조물(균열)' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/다세대주택' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/단독주택' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/비주거용주택' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/아파트' 
#jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터/연립주택' 
jpgpath = '/home/e8ight_data/482Gdataset_origin/원천_데이터' 
search_dir(jpgpath, file_list, dir_list, save_list) 

file_list.sort()


print("원천데이터 개수: " + str(len(file_list)))

with open('json_text.txt', 'r') as f:
    for line in f:
        text.append(line.rstrip('\n')) 
    #text = pickle.load(f) 

text.sort()

print("라벨링데이터 개수: " + str(len(text)))


for t in text:
    for fl in file_list:
        if t not in fl:
            if t not in fail_list:
                fail_list.append(t)
            break
        else:
            file_list.remove(fl)
            break


print("불일치 개수: " + str(len(fail_list)))


with open('jpg_text.txt', 'w') as f:
    for line in save_list:
        f.write(line + '\n')
