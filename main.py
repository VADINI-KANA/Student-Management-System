from database import create_table 
from student_repository import get_student_by_email
from student_repository import update_student_course
from student_repository import delete_student
from student_repository import add_student
from student_repository import get_all_students
def main():
    create_table()
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit") 
        choice=input("Choose an option: ")
        if choice =="1":
         first_name = get_valid_input("First Name: ")
         last_name =get_valid_input("Last Name: ")
         age = get_valid_age()
         course =get_valid_input("Course: ")
         email = get_valid_email()
         result= add_student(first_name,last_name,age,course,email)
         if result=="SUCCESS":
             print("Student added successfully!")
         elif result=="EMAIL_ALREADY_EXISTS":
            print("A student with this email already exists.")
        
        elif choice=="2":
            students= get_all_students()
            if not students:
                print("No studets found.")
            else:
                for student in students:
                    print("=" * 30)
                    print(f"ID: {student.id}")
                    print(f"First Name: {student.first_name}")
                    print(f"Last Name: {student.last_name}")
                    print(f"Age: {student.age}")
                    print(f"Course: {student.course}")
                    print(f"Email: {student.email}")
                    print("=" * 30)  
                                                   
        elif choice=="3":
            email=get_valid_email()
            student=get_student_by_email(email)
            if student:
                print("ID:", student.id)
                print("First Name:", student.first_name)
                print("Last Name:", student.last_name)
                print("Age:", student.age)
                print("Course:", student.course)
                print("Email:", student.email)
            else:
                print("student not found.")    
        elif choice=="4":
            email=get_valid_email()
            new_course=input("Enter your new_course: ")
            student = get_student_by_email(email)
            if student:
                update_student_course(email,new_course)
                print("New course updated successfully.")
            else:
                print("Student not found.")    
        elif choice=="5":
            email=get_valid_email()
            student=get_student_by_email(email)
            if student:
                delete_student(email)
                print("Student deleted successfully.")
            else:
                print("Student not found.")
        elif choice=="6":
            break 
        else:
            print("Invalid option. Please try again.")  
   

def get_valid_input(message):
        while True:
            value=input(message)
            if  value.strip()=="":
                print("This field cannot be empty.")
            else:
                return value
def get_valid_email():
        while True:
            email=input("Enter your Email: ")
            if email.strip()=="":
                print("Email cannot be empty.")
            elif ("@"in email) and( "." in email):
                return email  
           
            else:
                print("Please enter a valid email address.")

def get_valid_age():
        while True:
            try:
                message="Enter your age: "
                age=int(input(message))
                if age < 0 or age > 120:
                    print("Please enter a realistic age.")
                else:
                    return age 
            except ValueError:
                print("Please enter a valid number.")           
                         
               
if __name__ == "__main__":
        main()
         

          
