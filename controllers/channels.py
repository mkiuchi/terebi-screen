#
# Endpoint:
#   /channels
# Prerequisite:
#   # dnf -y install python3-mysql
#

def channels_get() -> str:
    #ret = {"name": "日テレ", "adi": "hd/27"}
    ret = []
    import MySQLdb, configparser
    config = configparser.ConfigParser()
    config.read('conf/screen.ini')

    connector = MySQLdb.connect(
        user=config['database']['username'],
        passwd=config['database']['password'],
        host=config['database']['host'],
        db=config['database']['db'],
        charset=config['database']['charset']
    )

    cursor=connector.cursor()
    cursor.execute("SELECT * FROM Recorder_channelTbl")
    for row in cursor.fetchall():
        ret.append({
            "id": row[0],
            "type": row[1],
            "channel": row[2],
            "name": row[3],
            "channel_disc": row[4],
            "sid": row[5],
            "skip": row[6]
            })
    cursor.close
    connector.close

    return ret
    #return 'do some magic!'
