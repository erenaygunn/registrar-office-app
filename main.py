flag = True

while flag:
    students = open("./files/student.txt", "r")
    courses = open("./files/course.txt", "r")

    print("1: List all the courses. \n"
          "2: List all the course that have at least one student registered. \n"
          "3: Add a new course. \n"
          "4: Search a course by course code. \n"
          "5: Search a course by name. \n"
          "6: Register a student to a course. \n"
          "7: List all the students and their registered courses. \n"
          "8: List top 3 most crowded courses. \n"
          "9: List top 3 students with the most course registrations. \n"
          "0: Exit. \n")
    action = int(input("Enter the digit of action you want to perform: "))
    print()

    if action == 1:
        print("Course Code |  Course Name")
        print("-----------------------------")
        for line in courses:
            newline = line.strip("\n")
            items = newline.split(";")
            print(items[0], ":  ", items[1])
        courses.close()
        print()
        act = int(input("0:Go back. \n"
                        "1:Exit. \n"
                        "Choose action:"))
        if act == 1:
            flag = False

    elif action == 2:
        print("Course Code |      Course Name            | Student Count")
        print("--------------------------------------------------------")
        for line in courses:
            newline = line.strip("\n")
            items = newline.split(";")
            if int(items[3]) > 0:
                print(items[0], ":  ", items[1], "|", items[3])
        courses.close()
        act = int(input("0:Go back. \n"
                        "1:Exit. \n"
                        "Choose action:"))
        if act == 1:
            flag = False

    # elif action == 3:

