import psycopg
import datetime

host     = "localhost"
port     = "5432"
database = "School"
user     = "postgres"
password = "postgres"

# maybe make it a global so all functions can access thios
connect = psycopg.connect(f"host={host} port={port} dbname={database} user={user} password={password}")


# def connectDatabase():

#     connect = psycopg.connect(f"host={host} port={port} dbname={database} user={user} password={password}")
    
#     return connect

def getAllStudents():
    students = connect.cursor().execute("SELECT * FROM students").fetchall()
    for student in students:
        for col in student:
            print (col, end="\t")
        print()


def addStudent(first_name, last_name, email, enrollment_date):

    connect.cursor().execute("""INSERT INTO students (first_name, last_name, email, enrollment_date)
                                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(enrollment_date)s)""", {'first_name':first_name, 'last_name':last_name, 'email':email, 'enrollment_date':enrollment_date})


def updateStudentEmail(student_id, email):

    connect.cursor().execute(""" UPDATE students SET email = %(email)s WHERE student_id = %(student_id)s""",
                             {'student_id':student_id, 'email':email})
    
def deleteStudent(student_id):

    connect.cursor().execute(""" DELETE FROM students WHERE student_id = %(student_id)s""", 
                             {'student_id':student_id})

def printFunc(arr):

    for elem in arr:
        print(elem)



def main():
    # connection = connectDatabase()
    # getAllStudents()
    # print()
    # addStudent('Jim', 'Halpert', 'jimhalpert@dundermifflin.com', '2000-01-01')
    # updateStudentEmail(7, 'stinkyjimmy@gmail.com')
    # deleteStudent(4)
    # getAllStudents()

    flag = True
    while(flag):

        print("\n \n")
        print("1. getAllStudents()")
        print("2. addStudent()")
        print("3. updateStudentEmail()")
        print("4. deleteStudent()")
        print("5. exit")
        option = input("Choose an option from the following: ")
        print("\n \n")

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


    connect.commit()
    connect.close()



if __name__ == "__main__":
    main()