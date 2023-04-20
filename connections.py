import psycopg2 as pc2

def connection_open():
    global conn,cursor
    conn=pc2.connect("dbname=komunalka user=postgres password=123 port=5432")
    cursor=conn.cursor()

def connection_close():
    cursor.close()
    conn.close()