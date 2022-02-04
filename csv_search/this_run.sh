val=$1

if [ -f 'info.ini' ]; then
	source info.ini $val
	echo "{$direct_path}"
	echo "실행 작업: csv_to_dataframe.py"
	echo "input_path: " $input_path
	echo "download_path: " $download_path
	
	echo "============Header============"
	python3 csv_header.py $input_path $download_path
	
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
		python3 csv_to_dataframe.py list $input $input_path $download_path
		echo " "
		echo " "
		echo "==================select_header================="
		python3 header_search.py $download_path $data_path $result_path
	fi
fi
