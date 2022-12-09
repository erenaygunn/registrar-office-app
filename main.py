flag = True

while flag:
    students = open("./files/student.txt", "r")
    courses = open("./files/course.txt", "r")

    # Simple Menu
    print("1: List all the courses. \n"
          "2: List all the courses that have at least one student registered. \n"
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

    if action == 1:  # Listing courses
        print("Course Code |  Course Name")
        print("-----------------------------")

        for line in courses:  # Iterates through every line
            newline = line.strip("\n")  # Removes line-breaks
            items = newline.split(";")  # Separates course code, name, instructor and students as list items.
            print(items[0], ":  ", items[1])

        courses.close()  # Closes the file so that it can be re-opened after this if statement.
        print()

        act = int(input("0:Go back. \n"  # This act menu helps current action to keep running,
                        "1:Exit. \n"  # It has its own flag as 'act' variable, user selects actions.
                        "Choose action:"))  # It will be used multiple times in this program.

        if act == 1:
            flag = False

    elif action == 2:  # Listing courses with at least one student
        print("Course Code |      Course Name            | Student Count")
        print("--------------------------------------------------------")
        for line in courses:
            newline = line.strip("\n")
            items = newline.split(";")

            if int(items[3]) > 0:  # Checks student count, if it's greater than 0, prints course.
                print(items[0], ":  ", items[1], "|", items[3])

        print()
        courses.close()

        act = int(input("0:Go back. \n"
                        "1:Exit. \n"
                        "Choose action:"))
        if act == 1:
            flag = False

    elif action == 3:  # Adding new course
        act = 2  # Flag for loop

        while act == 2:
            with open("./files/course.txt", "a") as f:
                code = input("Enter course code: ")
                name = input("Enter course's name: ")
                instructor = input("Enter instructor's name: ")
                students = int(input("Enter students' count: "))
                f.write("\n")
                f.write(f"{code};{name};{instructor};{students}")
                print("Course successfully added. \n")

            act = int(input("0:Go back. \n"
                            "1:Exit. \n"
                            "2:Add another course. \n"
                            "Choose action:"))
            if act == 1:
                flag = False

    elif action == 4:  # Search course by code
        act = 2

        while act == 2:
            code = (input("Enter course code: \n"))
            exist = False

            with open("./files/course.txt", "r") as courses:
                for line in courses:
                    newline = line.strip("\n")
                    items = newline.split(";")
                    if items[0] == code:  # Searches the course with the code user entered.
                        print(items[0], ":", items[1], " / Instructor: ", items[2], " /  Students: ", items[3],
                              "\n")
                        exist = True  # If this is not set true, it will print that course doesn't exist.
                        break

                if not exist:
                    print("There is no such course. \n")
            act = int(input("0:Go back. \n"
                            "1:Exit. \n"
                            "2:Search another course. \n"
                            "Choose action: \n"))
            if act == 1:
                flag = False

    elif action == 5:  # Search course by name
        act = 2

        while act == 2:
            name = (input("Search courses by name: "))
            exist = False

            with open("./files/course.txt", "r") as courses:
                for line in courses:
                    newline = line.strip("\n")
                    items = newline.split(";")
                    if name in items[1]:
                        print(items[0], ":  ", items[1])
                        exist = True

                if not exist:
                    print("No courses found. \n")
                print()

                act = int(input("0:Go back. \n"
                                "1:Exit. \n"
                                "2:Search another course. \n"
                                "Choose action:"))
                if act == 1:
                    flag = False

    elif action == 6:  # Register student to course
        act = 2

        while act == 2:
            course_exist = False
            student_exist = False
            code = input("Enter course code: ")
            st_id = input("Enter student id: ")

            # This increases course's student count by 1
            with open("./files/course.txt", "r") as f:
                newline = []  # This will store modified text file
                for course_line in f.readlines():
                    new_course = course_line.strip("\n")
                    elements = new_course.split(";")

                    if elements[0] == code:  # Checks course code
                        newline.append(
                            course_line.replace(elements[3], str(int(elements[3]) + 1)))  # Increases count
                        course_exist = True

                    else:
                        newline.append(course_line)

            with open("./files/course.txt", "w") as f:
                for line in newline:  # Writes entire modified text in file
                    f.writelines(line)

            # This adds course code at the end of the student's information.
            with open("./files/student.txt", "r") as f:
                newline = []
                for student in f.readlines():
                    new_student = student.strip("\n")
                    elements = new_student.split(";")

                    if elements[0] == st_id:  # Checks student id.
                        newline.append(student.strip("\n") + "," + code + "\n")  # If it is same, adds course
                        student_exist = True

                    else:
                        newline.append(student)

            with open("./files/student.txt", "w") as f:
                for line in newline:  # Writes entire modified text again
                    f.writelines(line)

            if student_exist and not course_exist:
                print("Course doesn't exist!\n")

            elif not student_exist and course_exist:
                print("Student doesn't exist!\n")

            elif student_exist and course_exist:
                print("Student successfully registered.\n")

            else:
                print("Course and student not found. Try again.\n")

            act = int(input("0:Go back. \n"
                            "1:Exit. \n"
                            "2:Register another student. \n"
                            "Choose action:"))
            if act == 1:
                flag = False

    elif action == 7:  # Lists students and their courses
        act = 2

        while act == 2:
            with open("./files/student.txt", "r") as students:
                for line in students:
                    newline = line.strip("\n")
                    items = newline.split(";")
                    print(items[1])
                    print(f"[{items[2]}]\n")

            act = int(input("0:Go back. \n"
                            "1:Exit. \n"
                            "Choose action:"))
            if act == 1:
                flag = False

    elif action == 8:  # List top 3 crowded courses
        items = courses.read().split("\n")  # Separates each line into a list element

        sorted_items = []
        for item in items:  # This creates nested list so that student count can be accessed.
            sorted_items.append(item.split(";"))

        # This loop sorts courses depending on student count.
        for i in range(len(sorted_items)):
            for j in range(i + 1, len(sorted_items)):
                if int(sorted_items[i][3]) > int(sorted_items[j][3]):
                    sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]
        print(f"1. {sorted_items[-1][1]}: {sorted_items[-1][3]} students \n"
              f"2. {sorted_items[-2][1]}: {sorted_items[-2][3]} students \n"
              f"3. {sorted_items[-3][1]}: {sorted_items[-3][3]} students \n")

        act = int(input("0:Go back. \n"
                        "1:Exit. \n"
                        "Choose action:"))
        if act == 1:
            flag = False

    elif action == 9:  # List top 3 students with most courses
        items = students.read().split("\n")  # Separates each line into a list element

        sorted_items = []
        for item in items:  # This creates nested list so that courses can be accessed.
            sorted_items.append(item.split(";"))

        for i in sorted_items:
            try:
                course_count = len(i[2].split(","))  # This calculates the course count of each student
                i.append(str(course_count))  # Adds course count to the nested list

            # This exception is for students with no registered courses.
            except IndexError:
                i.append(str(0))
                i.append(str(0))
                i.append(str(0))

        # This loop sorts students depending on course counts.
        for i in range(len(sorted_items)):
            for j in range(i + 1, len(sorted_items)):
                if int(sorted_items[i][3]) > int(sorted_items[j][3]):
                    sorted_items[i], sorted_items[j] = sorted_items[j], sorted_items[i]
        print(f"1. {sorted_items[-1][1]}: {sorted_items[-1][3]} courses \n"
              f"2. {sorted_items[-2][1]}: {sorted_items[-2][3]} courses \n"
              f"3. {sorted_items[-3][1]}: {sorted_items[-3][3]} courses \n")

        act = int(input("0:Go back. \n"
                        "1:Exit. \n"
                        "Choose action:"))
        if act == 1:
            flag = False

    elif action == 0:
        flag = False
    else:
        print("Please choose between the given numbers only.\n")
