import MySQLdb as sql

def conn(host,user,passwd,port,sqls):
    con=sql.connect(host=host,user=user,passwd=passwd,port=int(port),charset='utf8')
    cur=con.cursor()
    u=0
    for q in sqls:
        u=cur.execute(q)
    i = len(sqls)
    if len(sqls[i-1])>6:
        #print sqls[i-1][0:6]
        if "UPDATE" == sqls[i-1][0:6]:
            r=u
            con.commit()
        else:
            r=cur.fetchall()
    cur.close()
    con.close()
    return r