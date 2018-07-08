import MySQLdb




def insert(db,cursor):

	try:

		sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
		 LAST_NAME, AGE, SEX, INCOME)
		 VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
		cursor.execute(sql)
		db.commit()
	
	except:
   		db.rollback()	
	

def fetch(db,cursor):
	
	sql = "SELECT * FROM EMPLOYEE"
	try:
	   cursor.execute(sql)
	   results = cursor.fetchall()
	   for row in results:
	      fname = row[0]
	      lname = row[1]
	      age = row[2]
	      sex = row[3]
	      income = row[4]
	      print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
		     (fname, lname, age, sex, income ))
	except:
	   print("Error: unable to fecth data")


def update(db,cursor):

	sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
	try:
	 
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()


def deleteRecord(db,cursor):
		
	sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
	try:
	   cursor.execute(sql)
      	   db.commit()
	except:
	   db.rollback()


db = MySQLdb.connect("localhost","root","root","test" )	
cursor = db.cursor()


insert(db,cursor)
fetch(db,cursor)
update(db,cursor)
fetch(db,cursor)
deleteRecord(db,cursor)
fetch(db,cursor)


