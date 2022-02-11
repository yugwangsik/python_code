val=$1
path_type=0

if [ -f 'info.ini' ] && [ -f 'info_v2.ini' ]; then
	if [ -n "$val" ]; then
		source info_v2.ini $val
		path_type=1
		. ./file_select.sh $input_path $download_path $data_path $result_path
	else
		source info.ini
		. ./directory_search.sh $input_path $download_path $data_path
	fi

fi
