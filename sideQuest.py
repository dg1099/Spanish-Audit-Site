import sqlite3

conn = sqlite3.connect("Users/diann/AppData/Local/Google/Chrome/User Data/Default/Network/Cookies")
c = conn.cursor()

print(c.fetchall())

conn.close()