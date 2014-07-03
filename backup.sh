now = `date`
python2.7 manage.py dumpdata > "$LOG_FOLDER/dump_db_$now"