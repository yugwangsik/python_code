device=$1

if [ -f 'info.ini' ]; then
    source info.ini
    python3 json_to_csv.py $val
#    python3 csv_information.py $device
#    if [ -e 'device.txt']; then
#        python3 csv_information.py 1
#    else
#        python3 csv_information.py $device
#    fi
fi
