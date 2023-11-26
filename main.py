import sqlite3
con = sqlite3.connect("database.db")
cur = con.cursor()
def create_table():
    create = "Create table if not exists emp(emp_name text,emp_id int, emp_sal int)"
    cur.execute(create)
    con.commit()
def insert_data():
    for i in range (3):
        name  = 'Divyansh'
        id = 3
        salary = 15000
        cur.execute("Insert into emp(emp_name,emp_id,emp_sal) values(?,?,?)",(name,id,salary))
        con.commit()
def remove():
    id = 3
    cur.execute("delete from emp where emp_id = ?",(id,))
    con.commit()
    d = cur.execute("select * from emp")
    for i in d.fetchall():
        print(i)
def update():
    cur.execute("update emp set emp_sal = 16000 where emp_id = 3")
    con.commit()
    u_data = cur.execute("select * from emp")
    for j in u_data.fetchall():
        print(j)
create_table()
insert_data()
remove()
