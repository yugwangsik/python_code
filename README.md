# 개요
  현재 폴더 및 하위 폴더에 csv파일 경로를 list로 저장하고, list의 경로에 파일을 하나씩 읽어온 뒤 dataframe으로 변환한 뒤 계속해서 합친다.<br>
  그리고 사용자는 원하는 날짜의 범위를 입력하면 해당 날짜 범위의 데이터를 출력하는 프로그램이다.<br>
  +실행명령어에 'list'를 추가하여 실행하면 검색된 디렉토리의 전체 개수, csv파일 전체 개수를 알 수 있다.<br>
  ※실행 ex)<br>
    :~ $python3 csv_to_dataframe_vx.py list<br>
  ※날짜 입력 ex)<br>
    2021-08-01<br>
    2021-8-1<br>
    
    

## Git 다운로드
  ```:~ $git clone https://github.com/yugwangsik/python_csv_project.git```


## 실행 전 준비 및 경로 변경
  - python_csv_project/csv폴더에 테스트용 csv파일을 넣는다.<br> 
    단, csv파일의 첫번째 column에 날짜형식은 yyyy-mm-dd hh:mm:ss 형식이여야 한다.
  - csv_to_dataframe_vx.py 파일을 준비한다.
  - csv_to_dataframe_vx.py 48번 줄에 로컬 경로를 자신의 환경에 맞추어서 변경한다.<br><br>
    	&lt;Linux&gt;<br>
      ```:~ $vim python_csv_project/csv_to_dataframe_vx.py```<br>
      ```vim 편집기에서 라인번호 확인 명령어 --> :set nu```<br>
      <img src="/img/48line.PNG" width="50%" height="50%"></img><br><br>
    &lt;window&gt;<br>
      ```python 편집가능한 IDE에서 csv_to_dataframe_vx.py 열기```<br>
      <img src="/img/line.PNG" width="50%" height="50%"></img>
    
  - python_csv_project/csv에 테스트용 csv파일을 이동시킨다.<br><br>
    &lt;Linux&gt;<br>
    <img src="/img/linux_path.PNG" width="50%" height="50%"></img><br><br>
    &lt;window&gt;<br>
    <img src="/img/win_path.PNG" width="30%" height="30%"></img>


## 실행
  ```:~ $python3 csv_to_dataframe_vx.py```<br>
  ```:~ $python3 csv_to_dataframe_vx.py list```
  
  
## 메뉴
  0.  끝내기&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->  프로그램 종료
  1.  전체 데이터 검색&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->  dataframe 전체 데이터 출력
  2.  날짜 범위 데이터 검색&nbsp;&nbsp;-->  시작날짜 ~ 종료날짜 입력하여 해당 범위 데이터만 출력
  3.  해당 월만 검색&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-->  1 ~ 12월까지 사용자가 입력한 월에 해당하는 데이터만 출력
  <br><img src="/img/menu.PNG" width="30%" height="30%"></img>

  
## 1. 전체 데이터 검색
  - <br>
  <img src="/img/select1.PNG" width="30%" height="30%"></img>
  
  
## 날짜 입력
  - csv_to_dataframe_vx.py를 실행 시킨 뒤 시작날짜 종료날짜를 입력한다.
  - 날짜를 입력할 때 형식은 yyyy-mm-dd hh:mm:ss 형식으로 입력한다.<br>
    <img src="/img/date.PNG" width="50%" height="50%"></img>


## 데이터 read 및 변환
  - csv_to_dataframe_vx.py를 실행 시키면 자신의 폴더 및 하위에 있는 csv파일의  경로를 리스트 형태로 저장한다.
  - 저장된 리스트에서 csv파일을 하나씩 dataframe 형태로 읽어와서 리스트에 저장한다.
  - dataframe형태로 저장된 리스트를 dataframe으로 다시 합친다.


## Result
  - 입력한 날짜 범위에 맞는 데이터를 확인 한다.<br>
    <img src="/img/result.PNG" width="450px" height="1000px"></img>

## UPGRADE
  - 사용자가 원하는 월만 출력할 수 있도록 구현 요함<br>
  ex)<br>
  1번. 전체 검색<br>
  2번. 범위 검색<br>
  3번. 월만 검색<br>
