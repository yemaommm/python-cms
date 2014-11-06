import MySQLdb as sql

def conn(host,user,passwd,port,sqls):
    con=sql.connect(host=host,user=user,passwd=passwd,port=int(port),charset='utf8')
    cur=con.cursor()
    for q in sqls:
        cur.execute(q)
    r=cur.fetchall()
    cur.close()
    con.close()
    return r