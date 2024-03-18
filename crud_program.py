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

def init_database():

    connect.execute(""" DROP TABLE IF EXISTS students""")

    connect.execute("""create table students
    (student_id			SERIAL, 
     first_name			TEXT not null, 
     last_name			TEXT not null, 
     email				TEXT not null UNIQUE,
	 enrollment_date	DATE,
     primary key (student_id)
    );""")

    connect.execute("""INSERT INTO students (first_name, last_name, email, enrollment_date) 
                    VALUES ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
                    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
                    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');""")

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

    init_database()

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
                info = input("(First Name) (Last Name) (Email) (Date)[YYYY-MM-DD] [SPACE SEPERATED]: ")
                info_list = [elem for elem in info.split(" ") if elem != ""]
                try:
                    addStudent(info_list[0], info_list[1], info_list[2], info_list[3])
                    print("Successfully added student!")
                except Exception as error:
                    print("We encountered an error. Make sure each argument exists, and the date is formatted accordingly.")
            case '3':
                info = input("(Student Id) (Email) [SPACE SEPERATED]: ")
                info_list = [elem for elem in info.split(" ") if elem != ""]
                try:
                    updateStudentEmail(int(info_list[0]), info_list[1])
                    print("Successfully updated student!")
                except Exception as error:
                    print("We encountered an error. Make sure each argument exists.")

            case '4':
                try:
                    info = int(input("(Student Id) [Integer]: "))
                    deleteStudent(info)
                    print("Successfully deleted student!")
                except Exception as error:
                    print("We encountered an error. Make sure each argument exists.")
            case '5':
                break


    # commits the changes to the database, effectively updating the database if needed
    connect.commit()
    # closes the connection between the application and the database
    connect.close()
    print("Terminated")



if __name__ == "__main__":
    main()