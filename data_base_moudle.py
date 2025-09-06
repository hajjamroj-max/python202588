import sqlite3
def create_database():
    Connection = sqlite3.connect('mft.db')
    Connection.close()

def save(address,area,price):
    Connection = sqlite3.connect('mft.db')
    Connection.cursor().execute("insert into homes (address,area, price) values (?,?,?);",[address,area,price])
    Connection.commit()
    Connection.close()


