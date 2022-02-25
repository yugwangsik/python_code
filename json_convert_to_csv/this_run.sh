device=$1

if [ -f 'info.ini' ]; then
    source info.ini
    python3 json_to_csv.py $val
    python3 csv_information.py $device
fi
