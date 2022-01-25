
## 실행 전 준비 및 경로 변경
  - python_csv_project/csv_search/csv폴더에 csv파일을 넣는다.<br> 
    단, csv파일의 첫번째 column에 날짜형식은 yyyy-mm-dd hh:mm:ss 형식이여야 한다.
  - info.ini $val 변수의 경로를 자신의 환경에 맞추어서 변경한다.<br><br>
    $val = 'your_path'
<!--

## 실행
  ```cd python_csv_project```<br>
  ```bash this.run.sh```    

  
## 메뉴
  0.  끝내기&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  프로그램 종료
  1.  전체 데이터 검색&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  dataframe 전체 데이터 출력
  2.  날짜 범위 데이터 검색&nbsp;&nbsp;  시작날짜 ~ 종료날짜 입력하여 해당 범위 데이터만 출력
  3.  해당 월만 검색&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  1 ~ 12월까지 사용자가 입력한 월에 해당하는 데이터만 출력
  <br><br><img src="/img/menu.PNG" width="30%" height="30%"></img>


  
## csv_to_dataframe.py
  - 실행하면 csv_to_dataframe.py가 실행이 되고, 자신의 폴더 및 하위에 있는 csv파일의 경로를 리스트 형태로 저장한다.
  - 저장된 리스트에서 csv파일을 하나씩 dataframe 형태로 읽어와서 리스트에 저장한다.
  - dataframe형태로 저장된 리스트를 dataframe으로 다시 합친다.
  - 오름차순으로 정렬한 뒤 출력한다.
  - merge.py에 정렬된 dataframe 리스트를 넘겨준다.


## csv_header.py
  - 자신의 폴더 및 하위에 있는 csv파일 1개를 읽어오고 헤더를 제외한 data는 배제한다.
  - 헤더는 python_csv_project/csv_search/result_txt/header_field.txt로 저장한다.


## merge.py
  - python_csv_project/csv_search/result_txt/header_field.txt 파일을 읽어온다.
  - csv_to_dataframe.py에서 넘어온 리스트와 header_field.txt의 헤더를 합친다.
  - 합친 data를 python_csv_project/result_search/output.txt로 저장한다.


## header_search.py
  - python_csv_project/result_search/output.txt 파일을 읽어온다.
  - python_csv_project/csv_search/result_txt/search_header.txt 파일을 읽어온다.
  - search_header.txt의 헤더와 output.txt의 헤더를 비교하여 일치하는 헤더의 data를 리스트로 따로 저장한다.
  - 저장된 리스트를 python_csv_project/result_search/output.csv로 저장한다.
-->

