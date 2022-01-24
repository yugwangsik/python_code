<!--## 개요
  - python_csv_project/csv폴더에 테스트용 csv파일을 넣는다.<br> 
    단, csv파일의 첫번째 column에 날짜형식은 yyyy-mm-dd hh:mm:ss 형식이여야 한다.


## 실행 전 준비 및 경로 변경
  - python_csv_project/csv폴더에 테스트용 csv파일을 넣는다.<br> 
    단, csv파일의 첫번째 column에 날짜형식은 yyyy-mm-dd hh:mm:ss 형식이여야 한다.
  - info.ini user_path 변수의 경로를 자신의 환경에 맞추어서 변경한다.<br><br>
    	&lt;Linux&gt;<br>
      ```:~ $vim info.ini```<br>
      <img src="/img/user_path.PNG" width="50%" height="50%"></img><br><br>
    
    
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

  
-->

