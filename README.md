# 개요
  현재 폴더 및 하위 폴더에 csv파일 경로를 list로 저장하고, list의 경로에 파일을 하나씩 읽어온 뒤 dataframe으로 변환하여 하나의 형태로 합친다.<br>
  그리고 전체 데이터 검색, 날짜 범위 데이터 검색, 해당 월만 검색, 끝내기 등의 기능을 지원한다.<br><br>
  추가적으로 검색된 결과를 pickle, text 파일로 저장한다.<br><br>
  저장경로는 result_txt 디렉토리에 저장한다.<br><br>
  +this_run.sh를 실행하면 마지막 결과로 전체 데이터 개수, 전체 csv파일 개수, 검색된 데이터 개수를 알 수 있다.<br><br>
  ※실행 ex)<br>
    :~ $bash this_run.sh<br><br>
  ※날짜 입력 ex)<br>
    2021-08-01<br>
    2021-8-1<br>
    
    

## Git 다운로드
  ```:~ $git clone https://github.com/yugwangsik/python_csv_project.git```


## 실행 전 준비 및 경로 변경
  - python_csv_project/csv폴더에 테스트용 csv파일을 넣는다.<br> 
    단, csv파일의 첫번째 column에 날짜형식은 yyyy-mm-dd hh:mm:ss 형식이여야 한다.
  - this_run.sh, csv_to_dataframe.py 파일을 준비한다.
  - csv_to_dataframe.py csvpath 변수의 경로를 자신의 환경에 맞추어서 변경한다.<br><br>
    	&lt;Linux&gt;<br>
      ```:~ $vim python_csv_project/csv_to_dataframe.py```<br>
      ```vim 편집기에서 라인번호 확인 명령어 --> :set nu```<br>
      <img src="/img/linux_line.PNG" width="50%" height="50%"></img><br><br>
    &lt;window&gt;<br>
      ```python 편집가능한 IDE에서 csv_to_dataframe.py 열기```<br>
      <img src="/img/win_line.PNG" width="50%" height="50%"></img>
    
  - python_csv_project/csv에 테스트용 csv파일을 이동시킨다.<br><br>
    &lt;Linux&gt;<br>
    <img src="/img/linux_path.PNG" width="50%" height="50%"></img><br><br>
    &lt;window&gt;<br>
    <img src="/img/win_path.PNG" width="30%" height="30%"></img>
    
    
## 데이터 변환 및 출력
  - this_run.sh를 실행하면 csv_to_dataframe.py가 실행이 되고, 자신의 폴더 및 하위에 있는 csv파일의 경로를 리스트 형태로 저장한다.
  - 저장된 리스트에서 csv파일을 하나씩 dataframe 형태로 읽어와서 리스트에 저장한다.
  - dataframe형태로 저장된 리스트를 dataframe으로 다시 합친다.
  - 오름차순으로 정렬한 뒤 출력한다.


## 실행
  ```cd python_csv_project```<br>
  ```bash this.run.sh```
  
  
## 메뉴
  0.  끝내기&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->  프로그램 종료
  1.  전체 데이터 검색&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->  dataframe 전체 데이터 출력
  2.  날짜 범위 데이터 검색&nbsp;&nbsp;-->  시작날짜 ~ 종료날짜 입력하여 해당 범위 데이터만 출력
  3.  해당 월만 검색&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->  1 ~ 12월까지 사용자가 입력한 월에 해당하는 데이터만 출력
  <br><br><img src="/img/menu.PNG" width="30%" height="30%"></img>

  
## 1. 전체 데이터 검색
  - 입력 칸에 1 입력한다.
  <br><img src="/img/select1.PNG" width="30%" height="30%"></img><br>
  

## 1-2. Result
  - 전체 데이터가 출력 되었는지 확인 한다.
    <br><img src="/img/select1_result.PNG" width="30%" height="30%"></img>
    
    
## 2-1. 날짜 범위 데이터 검색
  - 입력 칸에 2 입력한다.
  <br><img src="/img/select2.PNG" width="50%" height="50%"></img>


## 2-2. 날짜 입력
  - 날짜 입력 형식은 yyyy-mm-dd 형식 or yyyy-m-d 이다.
    <br><img src="/img/select2_date.PNG" width="30%" height="30%"></img>


## 2-3. Result
  - 입력한 날짜 범위에 맞는 데이터가 출력 되었는지 확인 한다.
    <br><img src="/img/select2_result.PNG" width="90%" height="90%"></img>


## 3-1. 해당 월만 검색
  - 입력 칸에 3 입력한다.
  <br><img src="/img/select3.PNG" width="30%" height="30%"></img>


## 3-2. 날짜 입력
  - 날짜 입력 형식은 yyyy-mm-dd 형식 or yyyy-m-d 이다.
  - 연도의 기준은 현재 연도를 기준으로 한다.
    <br><img src="/img/select3_date.PNG" width="30%" height="40%"></img>


## 3-3. Result
  - 입력한 날짜 범위에 맞는 데이터가 출력 되었는지 확인 한다.
    <br><img src="/img/select3_result.PNG" width="50%" height="50%"></img>



## result_txt
  <img src="/img/result_txt.PNG" width="50%" height="50%"><br>


