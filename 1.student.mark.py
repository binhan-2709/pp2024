#Function to input student information
def input_students():
    num_students = int(input("Enter the number of students: "))
    students_info = []  #List to store the tuples of student information
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student Date of Birth (DD/MM/YYYY): ")

        #Create a tuple for each student (ID, name, DoB)
        student_tuple = (student_id, student_name, student_dob)

        #Add the tuple to the list 
        students_info.append(student_tuple)

    return students_info
    

#Function to store student information in a dictionary
def store_student_info(students_info):
    students_dict = {}  #Dictionary to store student info by ID
    for student in students_info:
        student_id, student_name, student_dob = student
        students_dict[student_id] = {
            "name": student_name,
            "dob": student_dob
        }
    return students_dict

#Function to input course information
def input_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses_info = []  #List to store course information as tuples
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        #Create a tuple for each course (ID, name)
        course_tuple = (course_id, course_name)

        #Adding the tuple to the list
        courses_info.append(course_tuple)
    
    return courses_info

#Function to input student marks for a selected course
def input_marks_for_course(students, courses):
    marks = {}  #Dictionary to store marks with (student_id, course_id) as key
    for course in courses:
        course_id, course_name = course  #Unpacking the course tuple
        for student in students:
            student_id, student_name, student_dob = student
            mark = float(input(f"Enter marks for {student_name} ({student_id}) in course {course_name}: "))
            marks[(student_id, course_id)] = mark  #Store marks with tuple key (student_id, course_id)
    return marks

#Function to list all courses
def list_courses(courses):
    print("\nCourses: ")
    for course in courses: 
        print(f"ID: {course[0]}, Name: {course[1]}")

#Function to list all students
def list_students(students):
    print("\nStudents: ")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Date of Birth: {student[2]}")

#Function to show marks of a student in a given course
def show_student_marks(marks, students, courses):
    student_id = input("Enter student ID to view marks: ")
    course_id = input("Enter course ID to view marks: ")
    if (student_id, course_id) in marks:
        print(f"Marks for Student {student_id} in Course {course_id}: {marks[(student_id, course_id)]}")
    else: 
        print("No marks found for this student in the given course.")

#Main function to drive the program
def main():
    #Input number of students and courses
    students = input_students()
    courses = input_courses()

    #Input marks for all students in all courses
    marks = input_marks_for_course(students, courses)

    while True:
        #Display menu
        print("\nMenu:")
        print("1. List all courses")
        print("2. List all students")
        print("3. Show student marks for a given course")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            show_student_marks(marks, students, courses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()














