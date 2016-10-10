#
# Endpoint:
#   /pinfo
#

def pinfo_get(channel_disc, channel_type, channel, etime) -> str:

    import datetime, pytz, configparser
    config = configparser.ConfigParser()
    config.read('conf/screen.ini')

    mytz = pytz.timezone("Asia/Tokyo")
    timestr = datetime.datetime.fromtimestamp(etime, tz=mytz)
    sqlstr = 'SELECT * FROM Recorder_programTbl WHERE channel_disc = ' + "'" + channel_disc + "' AND endtime >= '" + str(timestr) + "' LIMIT 10"
    print(sqlstr)

    ret = []

    import MySQLdb
    connector = MySQLdb.connect(
        user=config['database']['username'],
        passwd=config['database']['password'],
        host=config['database']['host'],
        db=config['database']['db'],
        charset=config['database']['charset']
    )

    cursor=connector.cursor()
    cursor.execute(sqlstr)
    for row in cursor.fetchall():
        ret.append({
            "title": row[5],
            "description": row[6],
            "program_disc": row[10],
            "starttime": row[8],
            "endtime": row[9]
            })
    cursor.close
    connector.close

    return ret
    #return 'do some magic!'
