if [ -f 'info.ini' ]; then
    source info.ini
    python3 json_to_csv.py $val
fi
