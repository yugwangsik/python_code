
	echo "------------메뉴------------"
	echo "0. 끝내기"
	echo "1. 전체 데이터 검색"
	echo "2. 날짜 범위 데이터 검색"
	echo "3. 해당 월만 검색"
	echo ""
	echo "원하는 메뉴의 번호를 입력하세요: "
	read input
	
	if [ $input = 0 ]
	then
		echo "■ 종료합니다."
	else
		time python3 csv_to_dataframe.py list $input
	fi

