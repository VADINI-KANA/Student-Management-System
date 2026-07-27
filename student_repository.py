import sqlite3
from database import connect_database
from student import Student



def add_student(first_name,last_name,age,course,email ):
    connection=None
    try:
        connection=connect_database()
        cursor=connection.cursor()
        cursor.execute ("""INSERT INTO students(first_name,last_name,age,course,email)
        VALUES(?,?,?,?,?)"""
        ,(first_name,last_name,age,course,email) )
        connection.commit()
        return"SUCCESS"

    except sqlite3.IntegrityError:
        return"EMAIL_ALREADY_EXISTS"

    except Exception as e:
        print("Error adding student:", e)
        
    finally:
       if connection:
          connection.close()
      
       


def get_all_students():
    connection=None
    try:
     connection=connect_database()
     cursor=connection.cursor()
     cursor.execute ("""SELECT* FROM students """)
     student_rows=cursor.fetchall()
     student_list=[]
     for student in student_rows:
        new_student= Student(student[0],
                        student[1],
                        student[2],
                        student[3],
                        student[4],
                        student[5])
        student_list.append(new_student)
     return student_list   
    except Exception as e:
       print("Error to select",e)    
     
    finally:
       if connection:
          connection.close() 
    
       
def get_student_by_email(email):
   connection=None
   try:
      connection=connect_database()
      cursor=connection.cursor()
      cursor.execute("""SELECT* FROM students WHERE email=?
        """,(email,))
      student=cursor.fetchone()
      if student:
         return Student( student[0],
                        student[1],
                        student[2],
                        student[3],
                        student[4],
                        student[5]) 
      return None 
   except Exception as e:
      print("Error email",e)
   finally:
      if connection:
         connection.close()
      
     
def update_student_course(email,new_course):
   connection=None
   try:
      connection=connect_database()
      cursor=connection.cursor()
      cursor.execute("""UPDATE students
       SET course=?
       WHERE email=?""",(new_course,email))
      connection.commit()
   except Exception as e:
      print("Error to update",e)
   finally:
      if connection:
         connection.close()


def delete_student(email):
   connection=None
   try:
      connection=connect_database()
      cursor=connection.cursor()
      cursor.execute("""DELETE FROM students WHERE email=?""" ,(email,))
      connection.commit()
   except Exception as e:
      print("Error to Delete",e)
   finally:
      if connection:
         connection.close()    







