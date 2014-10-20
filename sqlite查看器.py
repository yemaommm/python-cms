# coding=utf-8
import sqlite3
import string

def tabs():
	print u'请输入sqlite3数据库名称'
	db=raw_input("")
	cx=sqlite3.connect(db)
	cu=cx.cursor()
	while(1):
		cu.execute("select name from sqlite_master where type='table' order by name")
		print u'有以下数据表'
		tab=cu.fetchall()
		i=0
		for s in tab:
			i+=1
			print str(i)+':'+s[0]

		print u'请输入表名的编号'
		db=raw_input("")
		print str(list(tab)[string.atoi(db)-1][0])
		cu.execute("select * from "+str(list(tab)[string.atoi(db)-1][0]))
		ta=cu.fetchall()
		if(len(ta)==0):
			print u'表内无内容'
		else:
			col_name_list = [tuple[0] for tuple in cu.description]
			print len(col_name_list)
			xstr=''
			for count in range(len(col_name_list)):
				xstr+=col_name_list[count]
				for i in range(20-len(str(col_name_list[count]))):
					xstr+=" "
			print xstr

		print u'内容'
		xstr=''
		for xcount in range(len(ta)):
			for count in range(len(col_name_list)):
				xstr+=str(ta[xcount][count])
				for i in range(20-len(str(ta[xcount][count]))):
					xstr+=" "
			print xstr
			xstr=''
		#print col_name_list 
		print '\n\n'
		#print ta

if __name__ == "__main__":
    tabs()
