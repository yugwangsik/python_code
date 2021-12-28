## git 다운로드
  ```:~ $git clone https://github.com/yugwangsik/python_code.git```


## 실행 전 준비 및 경로 변경
  - csv폴더에서 테스트용 csv파일을 다운로드한다.
  - csv to dataframe.py 파일을 다운로드한다.
  - csv to dataframe.py 48번 줄에 로컬 경로를 자신의 환경에 맞추어서 변경한다.
    <img src="/img/line.PNG" width="450px" height="35px"></img>
    
  - 로컬 경로 하위에 테스트용 csv파일을 이동시킨다.<br>
    <img src="/img/path.PNG" width="1000px" height="35px"></img>

## 실행 및 날짜 입력
  - csv to dataframe.py를 실행 시킨 뒤 시작날짜 종료날짜를 입력한다.
  - 날짜를 입력할 때 형식은 yyyy-mm-dd hh:mm:ss 형식으로 입력한다.

## 데이터 read 및 변환
  - csv to dataframe.py를 실행 시키면 자신의 폴더 및 하위에 있는 csv파일의  경로를 리스트 형태로 저장한다.
  - 저장된 리스트에서 csv파일을 하나씩 dataframe 형태로 읽어와서 리스트에 저장한다.
  - dataframe형태로 저장된 리스트를 dataframe으로 다시 합친다.

## result
  - 입력한 날짜 범위에 맞는 데이터를 확인 한다.
