import sqlite3
 
conn = sqlite3.connect('userDB.db')

conn.execute(
    '''
    create table user_info (ID text, PW text)
    '''
)
 
conn.close()
