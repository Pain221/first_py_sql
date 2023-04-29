import psycopg2 as pc2

def connection_open():
    global conn,cursor
    conn=pc2.connect("dbname=*** user=*** password=*** port=***")
    cursor=conn.cursor()

def connection_close():
    cursor.close()
    conn.close()
