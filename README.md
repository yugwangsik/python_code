# 개요
  현재 폴더 및 하위 폴더에 csv파일 경로를 list로 저장하여 list의 파일을 하나씩 읽어온 뒤 dataframe으로 변환한 뒤 계속해서 합침.
  그리고 사용자는 원하는 날짜의 범위를 입력하면 해당 날짜 범위의 데이터를 출력하는 프로그램.
  ※날짜 입력 ex)2021-08-01 00:00:00
                2021-10-31 23:59:59

## Git 다운로드
  ```:~ $git clone https://github.com/yugwangsik/python_csv_project.git```


## 실행 전 준비 및 경로 변경
  - python_csv_project/csv폴더에 테스트용 csv파일을 넣는다. 단, csv파일의 첫번째 column에 날짜형식은 yyyy-mm-dd hh:mm:ss 형식이여야 한다.
  - csv_to_dataframe.py 파일을 준비한다.
  - csv_to_dataframe.py 48번 줄에 로컬 경로를 자신의 환경에 맞추어서 변경한다.
    <Linux>
      ```:~ $vim python_csv_project/csv_to_dataframe.py```
    <window>
      ```python 편집가능한 IDE에서 csv_to_dataframe.py 열기```
    <img src="/img/line.PNG" width="50%" height="50%"></img>
    
  - 로컬 경로 하위에 테스트용 csv파일을 이동시킨다.<br>
    <img src="/img/path.PNG" width="600px" height="200px"></img>

## 실행
  ```:~ $python3 csv_to_dataframe.py```
  
## 날짜 입력
  - csv_to_dataframe.py를 실행 시킨 뒤 시작날짜 종료날짜를 입력한다.
  - 날짜를 입력할 때 형식은 yyyy-mm-dd hh:mm:ss 형식으로 입력한다.<br>
    <img src="/img/test.PNG" width="500px" height="50px"></img>

## 데이터 read 및 변환
  - csv_to_dataframe.py를 실행 시키면 자신의 폴더 및 하위에 있는 csv파일의  경로를 리스트 형태로 저장한다.
  - 저장된 리스트에서 csv파일을 하나씩 dataframe 형태로 읽어와서 리스트에 저장한다.
  - dataframe형태로 저장된 리스트를 dataframe으로 다시 합친다.

## Result
  - 입력한 날짜 범위에 맞는 데이터를 확인 한다.<br>
    <img src="/img/test_result.PNG" width="400px" height="1000px"></img>
