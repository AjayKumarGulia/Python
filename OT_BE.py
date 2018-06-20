import sqlite3

def connect():
    conn = sqlite3.connect("OTKeeper.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS OTRecord (id INTEGER PRIMARY KEY, Worked_Hours integer, Date text, Duration text)")
    conn.commit()
    conn.close()

def Add(Worked_Hours, Date, Duration):
    conn = sqlite3.connect("OTKeeper.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO OTRecord VALUES (NULL,?,?,?)", (Worked_Hours, Date, Duration))
    conn.commit()
    conn.close()

def Remove(id):
    conn = sqlite3.connect("OTKeeper.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM OTRecord WHERE id =?",(id,))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("OTKeeper.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM OTRecord")
    rows = cur.fetchall()
    conn.close()
    return rows

def Search(Worked_Hours = "",Date = "",Duration = ""):
    conn = sqlite3.connect("OTKeeper.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM OTRecord WHERE Worked_Hours =? or Date = ? or Duration = ?",(Worked_Hours,Date,Duration))
    rows = cur.fetchall()
    conn.close()
    return rows

def Update(id,Worked_Hours,Date,Duration):
    conn = sqlite3.connect("OTKeeper.db")
    cur = conn.cursor()
    cur.execute("UPDATE OTRecord SET Worked_Hours =?, Date = ?,Duration = ? WHERE id = ?",(Worked_Hours,Date,Duration,id))
    conn.commit()
    conn.close()

connect()

#Add(4,"27th May", "8 to 9 PM")

#Remove(3)

#Search("Worked_Hours=4")

#print(Search(Worked_Hours=4))

print(view())
