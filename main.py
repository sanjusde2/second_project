import sqlite3

db=sqlite3.connect('students')
pointer=db.cursor()

pointer.execute("""
create table goldenbatch(id int,name text,age int)
""")
pointer.execute("insert into goldenbatch values(1,'raju',20)")
db.commit()
pointer.execute("select * from goldenbatch")

single_data=pointer.fetchall()
print(single_data)

pointer.close()
db.close()
print("add new content")
