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
		echo "■종료합니다."
	else
		python3 csv_to_dataframe.py list $input $input_path $download_path
		echo " "
		echo " "
		#echo "==================select_header================="
		#python3 header_search.py $download_path $data_path $result_path
		echo "==================요약================="
		python3 add_data.py $data_path

		echo "==================NaN 데이터 제거================="
		echo "일정 비율 이상의 NaN 데이터를 제거 하시겠습니까? (y/n)"
		read input2

		if [ $input2 == "y" ] || [ $input2 == "Y" ];
		then
			echo "비율을 입력하세요(% 생략): "
			read input3

			python3 data_cut.py $data_path $input3
		elif [ $input2 == "n" ] || [ $input2 == "N" ];
		then
			echo "■종료합니다."
		else
			echo "■종료합니다."	
		fi	
	fi
fi
