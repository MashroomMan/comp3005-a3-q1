import psycopg

'''
Name:       Elie Feghali
Student Id: 101185489
'''

# Hard coded specifically for my environment
# Change as required for yourself
host     = "localhost"
port     = "5432"
database = "School"
user     = "postgres"
password = "postgres"

# Global that connect my application to postgres database
connect = psycopg.connect(f"host={host} port={port} dbname={database} user={user} password={password}")

# Finds all students in the database and iterates over the student data to display their content
def getAllStudents():
    students = connect.cursor().execute("SELECT * FROM students").fetchall()
    for student in students:
        for col in student:
            print (col, end="\t")
        print()

# Adds a new student to the database given the following parameters
def addStudent(first_name, last_name, email, enrollment_date):

    connect.cursor().execute("""INSERT INTO students (first_name, last_name, email, enrollment_date)
                                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(enrollment_date)s)""", {'first_name':first_name, 'last_name':last_name, 'email':email, 'enrollment_date':enrollment_date})

# Updates a student's email given a student id and a new email
def updateStudentEmail(student_id, email):

    connect.cursor().execute(""" UPDATE students SET email = %(email)s WHERE student_id = %(student_id)s""",
                             {'student_id':student_id, 'email':email})

# Deletes a student from the database given their student id
def deleteStudent(student_id):

    connect.cursor().execute(""" DELETE FROM students WHERE student_id = %(student_id)s""", 
                             {'student_id':student_id})

def main():

    flag = True
    while(flag):

        # displays all the possible options to test the application
        print("\n \n")
        print("1. getAllStudents()")
        print("2. addStudent()")
        print("3. updateStudentEmail()")
        print("4. deleteStudent()")
        print("5. exit")
        option = input("Choose an option from the following: ")
        print("\n \n")

        # Based on the users input, will direct them to execute the requested functionality
        match option:
            case '1':
                getAllStudents()
            case '2':
                info = input("(First Name) (Last Name) (Email) (Date) [SPACE SEPERATED]: ")
                info_list = info.split(" ")
                addStudent(info_list[0], info_list[1], info_list[2], info_list[3])
                print("Successfully added student!")
            case '3':
                info = input("(Student Id) (Email) [SPACE SEPERATED]: ")
                info_list = info.split(" ")
                updateStudentEmail(int(info_list[0]), info_list[1])
                print("Successfully updated student!")
            case '4':
                info = int(input("(Student Id): "))
                deleteStudent(info)
                print("Successfully deleted student!")
            case '5':
                exit()


    # commits the changes to the database, effectively updating the database if needed
    connect.commit()
    # closes the connection between the application and the database
    connect.close()



if __name__ == "__main__":
    main()