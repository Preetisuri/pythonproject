import sqlite3
from sqlite3 import Error
 
 
def create_connection():
    database = "C:\\Users\Jeeva Rathinam\AppData\Local\Programs\Python\Python37-32\codetest\db\empdata.db"
    conn = None
    try:
        conn = sqlite3.connect(database,check_same_thread=False)
        print("Connection established")
        return conn
    except Error as e:
        print(e)
 
    return conn

def create_table(conn):
    create_table_sql = """ CREATE TABLE IF NOT EXISTS employees (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        designation text NOT NULL,
                                        address text NOT NULL,
                                        phonr integer NOT NULL
                                    ); """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def insert_emp(conn, empval):
    sql = """ INSERT INTO employees(name,designation,address,phonr)
              VALUES(?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, empval)
    conn.commit()
    #return cur.lastrowid

def delete_emp(conn, id):
    sql = 'DELETE FROM employees WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def show_emp(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    return rows

def srch_emp(conn,val):
    sql="SELECT * FROM employees WHERE name=? OR Designation=? OR Phonr=?"
    cur = conn.cursor()
    cur.execute(sql,(val,val,val))
    rows = cur.fetchall()
    return rows

def main():
    conn = create_connection()
    if conn is not None:
        #empval=('William','Intern','Norway',46416)
        #empid=insert_emp(conn,empval)
        #delete_emp(conn,2)
        rows=srch_emp(conn,'1654')
        for row in rows:
            print(row)
    else:
        print("Error! cannot create the database connection.")

 

if __name__ == '__main__':
    main()
