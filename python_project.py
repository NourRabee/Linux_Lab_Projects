#NourRabee'_1191035

class Management_System:
    # list that contains all the registered students' ID
    _recordList = []
    # list that contains the taken courses for each student
    _takenCourses = []
    # list that contains all computer engineering program courses
    _courses = ['ENCS1201', 'ENCS1202', 'ENCS1400', 'ENCS2201', 'ENCS2202', 'ENCS2400', 'ENCS5321', 'ENCS5322',
                'ENCS5323', 'ENCS5331', 'ENCS5332', 'ENCS5333', 'ENCS5342', 'ENCS5343', 'ENCS5321', 'ENCS5322',
                'ENCS5323', 'ENCS5331', 'ENCS5332', 'ENCS5333', 'ENCS5341', 'ENCS5342', 'ENCS5343', 'ENCS5121',
                'ENCS5131', 'ENCS5131', 'ENCS5141', 'ENCS5324', 'ENCS5325', 'ENCS5326', 'ENCS5327', 'ENCS5334',
                'ENCS5335', 'ENCS5336', 'ENCS5344', 'ENCS5345', 'ENCS5346', 'ENCS5347', 'ENCS5348', 'ENCS5349',
                'ENCS5399', 'ENCS2110', 'ENCS2340', 'ENCS2380', 'ENCS3130', 'ENCS3310', 'ENCS3320', 'ENCS3330',
                'ENCS3340', 'ENCS3390', 'ENCS4110', 'ENCS4130', 'ENCS4210', 'ENCS4300', 'ENCS4310', 'ENCS4320',
                'ENCS4330', 'ENCS4370', 'ENCS4380', 'ENCS5140', 'ENCS5150', 'ENCS5200', 'ENCS5300', 'ENEE2103',
                'ENEE2304', 'ENEE2307', 'ENEE2312', 'ENEE2360', 'ENEE3309', 'ENEE4113']

    # list that contains each student's info (year, semester, courses and grades)
    _temp = []
    # list that the overall avg for each registered student
    _overall_avg = []
    # lists that contain that average hours per each semester 1, 2, and 3
    _avg_sem1 = []
    _avg_sem2 = []
    _avg_sem3 = []
    _grades = []
    _takenHours = []

    @property
    def taken_hours(self):
        return self._taken_hours

    @property
    def overall_avg(self):
        return self._overall_avg

    # function that counts number of lines in a file
    def linesInFile(self, sID):
        count = 0
        with open(sID + ".txt", 'r') as file:
            for line in file:
                count += 1
        return count

class Admin(Management_System):
    # instance methods
    def addNewRecordFile(self):

        while True:
            try:
                sID = int(input("Please enter the student ID\n"))
                ID = str(sID)
                File = open(ID + ".txt", "x")
            except FileExistsError:
                print("Error: This student already exists!\n")
                continue
            except ValueError:
                print("ID must be an integer\n")
                continue
            else:
                print("Adding a new student has done successfully!")
                Management_System._recordList.append(ID)
                print(Management_System._recordList)
                File.close()
                break

    def getInfo(self):
        added = True
        while added:
            try:
                sID = int(input("Please enter the student ID\n"))
                ID = str(sID)

            except ValueError:
                print("ID number must be integer only!!\n")
                continue

            else:
                if ID in Management_System._recordList:
                    # asking the user to enter the year
                    while True:
                        FILE = open(ID + ".txt", "a")
                        year = input("Please enter the year\n")
                        if "-" not in year:
                            print(
                                "Oops, wrong format. Make sure that you insert the year as required! Example: "
                                "2021-2022\n")
                            continue
                        else:
                            FILE.write(year)
                            FILE.close()
                            print("Adding year has done successfully!\n")
                            break

                    # asking the user to enter the semester
                    while True:
                        try:
                            FILE = open(ID + ".txt", "a")
                            semester = int(input(
                                "Please enter the semester\n(1) for the first semester\n(2) for the second "
                                "semester\n(3) for the summer semester\n"))
                            sem = str(semester)
                        except ValueError:
                            print("Pay attention, semester is a number\n")
                            continue
                        else:
                            if semester != 1 and semester != 2 and semester != 3:
                                print("Invalid Number\n")
                                continue
                            else:
                                FILE.write("/" + sem + " " + ";" + " ")
                                FILE.close()
                                print("Adding Semester has done successfully!\n")
                                break

                    # asking the user to enter the grades and courses
                    while True:
                        FILE = open(ID + ".txt", "a")
                        n = int(input("How many courses and grades do you want to enter?\n"))
                        str1 = ""

                        for x in range(n):
                            valid = True
                            while valid:
                                courses = input("Please enter the course:\n")
                                # checking if the input course contains ENEE and ENCS
                                if 'ENEE' in courses:
                                    pass  # Do nth
                                elif 'ENCS' in courses:
                                    pass
                                else:
                                    print("Error!! Courses must only be from ENEE and ENCS only!!\n ")
                                    continue
                                # Checking if this course is one of the computer engineering courses or not
                                if courses in Management_System._courses:
                                    pass
                                else:
                                    print("Error!! This course is not one of the Computer Engineering program!!")
                                    continue

                                grades = int(input("Please enter the course grade:\n"))

                                if x == n - 1:
                                    # if we reach to the last iteration execute the following command
                                    str1 += (" " + courses + " " + str(grades))

                                else:
                                    str1 += (" " + courses + " " + str(grades) + ",")

                                valid = False

                        FILE.write(str1 + "\n")
                        FILE.close()
                        added = False
                        break

                else:
                    print("This student is not registered\n")
                    break

    def update(self):
        while True:
            try:
                ID = int(input("Please enter the student ID that you want to update its info:\n"))
                sID = str(ID)
            except ValueError:
                print("ID must be an integer\n")
                continue
            else:
                if sID in Management_System._recordList:
                    courseName = input("Please enter the course code you want to update its grade:\n")
                    # Read in the file
                    with open(sID + ".txt", "r") as file:
                        filedata = file.read()
                        if courseName in filedata:
                            oldGrade = input("Please enter the grade you want to change:\n")
                            newGrade = input("Please enter the new grade:\n")
                            # Replace the target string
                            filedata = filedata.replace(courseName + " " + oldGrade, courseName + " " + newGrade)

                            # Write the file out again
                            with open(sID + ".txt", "w") as file:
                                file.write(filedata)
                                break
                        else:
                            print("This student is not registered in this course!\n")
                            continue
                else:
                    print("This student is not registered\n")
                    break

    def student_statistics(self):
        while True:
            try:
                ID = int(input("Please enter the student ID :\n"))
                sID = str(ID)
            except ValueError:
                print("ID must be an integer\n")
                continue
            else:
                if sID in Management_System._recordList:

                    # Calculating the average per semester and the overall average

                    FILE = open(sID + ".txt", "r")
                    countLines = Management_System.linesInFile(self, sID)
                    Lines = FILE.readlines()
                    totalHours = 0
                    overallAvg = []

                    for line in Lines:
                        data = re.sub('\n', ' ', line)  # replace new line by space
                        new_data = re.sub('[/;, ]', ',', data)  # replace all the characters with (,)
                        list2 = new_data.split(",")
                        temp = []
                        # remove all empty strings from the list
                        for string in list2:
                            if string != "":
                                # remove all strings that contain 1,2 or 3 from the list
                                if string != "2" and string != "3" and string != "1":

                                    if "-" not in string:
                                        temp.append(string)
                        x = 0
                        multi = []
                        sum_of_hours_per_semester = 0
                        for i in temp:
                            if 'ENEE' in i:
                                sum_of_hours_per_semester += int(i[5])
                                x += int(i[5])
                            elif 'ENCS' in i:
                                sum_of_hours_per_semester += int(i[5])
                                x += int(i[5])
                            else:
                                x = x * int(i)
                                multi.append(str(x))
                                x = 0
                        totalHours += sum_of_hours_per_semester

                        sum = 0
                        for i in multi:
                            sum += int(i)
                        semester_avg = sum / sum_of_hours_per_semester
                        overallAvg.append(semester_avg)
                        print("Semester average: ", semester_avg)

                        no_int = [y for y in temp if not (y.isdigit() or y[0] == '-' and y[1:].isdigit())]
                        Management_System._takenCourses.extend(no_int)

                    print("Taken Hours are: ", totalHours, "hrs")
                    # Subtract list of takenCourses from list of courses to have the remaining courses
                    remaining_courses = set(Management_System._courses) - set(Management_System._takenCourses)
                    print("Remaining courses: ", remaining_courses)

                    y = 0
                    for i in overallAvg:
                        y += float(i)

                    if countLines == 1:
                        overall_avg = y / 1  # if the file contains only one line= one semester, then the semester average = the overall average
                    else:
                        overall_avg = y / totalHours
                    print("Overall average is: ", overall_avg)
                    print("\n")
                    overallAvg.clear()
                    Management_System._takenCourses.clear()
                    break
                else:
                    print("This student is not registered yet!\n")
                    break

    def global_statistics(self):
        counter = 0
        for x in Management_System._recordList:
            sID = x
            FILE = open(sID + ".txt", "r")
            countLines = Management_System.linesInFile(self, sID)
            Lines = FILE.readlines()
            totalHours = 0
            overallAvg_per_student = []

            for line in Lines:

                data = re.sub('\n', ' ', line)  # replace new line by space
                new_data = re.sub('[/;, ]', ',', data)  # replace all the characters with (,)
                list2 = new_data.split(",")
                temp = []

                temp2 = []
                sem1 = []
                sem2 = []
                sem3 = []

                for string in list2:
                    if string != "":
                        if "-" not in string:
                            temp2.append(string)

                for i in temp2:
                    if i[0] == '1':
                        sem1 = temp2.copy()
                        hours_per_sem1 = 0
                        for y in sem1:
                            if 'ENEE' in y:
                                hours_per_sem1 += int(y[5])
                            elif 'ENCS' in y:
                                hours_per_sem1 += int(y[5])
                        Management_System._avg_sem1.append(hours_per_sem1)

                    elif i[0] == '2':
                        sem2 = temp2.copy()
                        hours_per_sem2 = 0
                        for y in sem2:
                            if 'ENEE' in y:
                                hours_per_sem2 += int(y[5])
                            elif 'ENCS' in y:
                                hours_per_sem2 += int(y[5])
                        Management_System._avg_sem2.append(hours_per_sem2)

                    elif i[0] == '3':
                        sem3 = temp2.copy()
                        hours_per_sem3 = 0
                        for y in sem3:
                            if 'ENEE' in y:
                                hours_per_sem3 += int(y[5])
                            elif 'ENCS' in y:
                                hours_per_sem3 += int(y[5])
                        Management_System._avg_sem3.append(hours_per_sem3)

                temp2.clear()
                # remove all empty strings from the list
                for string in list2:
                    if string != "":
                        # remove all strings that contain 1,2 or 3 from the list
                        if string != "2" and string != "3" and string != "1":

                            if "-" not in string:
                                temp.append(string)
                                # remove all the strings that contain the string 'ENEE' and 'ENCS'
                                if 'ENCS' not in string:
                                    if 'ENEE' not in string:
                                        Management_System._grades.append(string)
                x = 0
                sum_of_hours_per_semester = 0
                multi = []
                for i in temp:
                    if 'ENEE' in i:
                        sum_of_hours_per_semester += int(i[5])
                        x += int(i[5])
                    elif 'ENCS' in i:
                        sum_of_hours_per_semester += int(i[5])
                        x += int(i[5])
                    else:
                        x = x * int(i)
                        multi.append(str(x))
                        x = 0
                totalHours += sum_of_hours_per_semester

                sum = 0
                for i in multi:
                    sum += int(i)
                semester_avg = sum / sum_of_hours_per_semester
                overallAvg_per_student.append(semester_avg)

            y = 0
            for i in overallAvg_per_student:
                y += int(i)
            if countLines == 1:
                overall_avg = y / 1
            else:
                overall_avg = y / totalHours

            Management_System._overall_avg.append(str(overall_avg))
            overallAvg_per_student.clear()
            counter += 1

        # calculate all overall student avg
        sum = 0
        for x in Management_System._overall_avg:
            sum += float(x)
        overall_avg_forAll_students = float(sum / counter)
        print("**The Overall average for all students is: ", overall_avg_forAll_students)

        # calculate the avg hours per semester 1
        sum1 = 0
        for x in Management_System._avg_sem1:
            sum1 += float(x)
        avg_sem1 = float(sum1 / counter)
        print("**The average hours per semester 1 is: ", avg_sem1)

        # calculate the avg hours per semester 2
        sum2 = 0
        for x in Management_System._avg_sem2:
            sum2 += float(x)
        avg_sem2 = float(sum2 / counter)
        print("**The average hours per semester 2 is: ", avg_sem2)

        # calculate the avg hours per semester 3
        sum3 = 0
        for x in Management_System._avg_sem3:
            sum3 += float(x)
        avg_sem3 = float(sum3 / counter)
        print("**The average hours per semester 3 is: ", avg_sem3)
        print("\n")

        # Sorting the grade list
        sorted_grades = sorted(Management_System._grades)
        plt.hist(sorted_grades, edgecolor='black')
        plt.grid(color='green', linestyle='--', linewidth=0.5)  # adding vertical and horizontal lines in background
        plt.xlabel("Students' Grades", fontsize=15)
        plt.ylabel("Count", fontsize=15)
        plt.title("Distribution of Students' Grades")
        plt.show()

        Management_System._overall_avg.clear()
        Management_System._avg_sem1.clear()
        Management_System._avg_sem2.clear()
        Management_System._avg_sem3.clear()
        Management_System._grades.clear()

    def searching(self):
        counter = 0
        Management_System._overall_avg.clear()
        Management_System._takenHours.clear()

        for x in Management_System._recordList:
            sID = x
            FILE = open(sID + ".txt", "r")
            countLines = Management_System.linesInFile(self, sID)
            Lines = FILE.readlines()
            totalHours = 0
            overallAvg_per_student = []

            for line in Lines:

                data = re.sub('\n', ' ', line)  # replace new line by space
                new_data = re.sub('[/;, ]', ',', data)  # replace all the characters with (,)
                list2 = new_data.split(",")
                temp = []

                # remove all empty strings from the list
                for string in list2:
                    if string != "":
                        # remove all strings that contain 1,2 or 3 from the list
                        if string != "2" and string != "3" and string != "1":
                            if "-" not in string:
                                temp.append(string)

                x = 0
                sum_of_hours_per_semester = 0
                multi = []
                for i in temp:
                    if 'ENEE' in i:
                        sum_of_hours_per_semester += int(i[5])
                        x += int(i[5])
                    elif 'ENCS' in i:
                        sum_of_hours_per_semester += int(i[5])
                        x += int(i[5])
                    else:
                        x = x * int(i)
                        multi.append(str(x))
                        x = 0
                totalHours += sum_of_hours_per_semester
                Management_System._takenHours.append(str(totalHours))

                sum = 0
                for i in multi:
                    sum += int(i)
                semester_avg = sum / sum_of_hours_per_semester
                overallAvg_per_student.append(semester_avg)

            y = 0
            for i in overallAvg_per_student:
                y += int(i)
            if countLines == 1:
                overall_avg = y / 1
            else:
                overall_avg = y / totalHours
            Management_System._overall_avg.append(str(overall_avg))
            overallAvg_per_student.clear()

            counter += 1

        while True:
            answer = input("Search based on:\n[1] Average\n[2] Taken hours\n[3] Exit\n")
            if answer == '1':
                # creating a dictionry, keys => IDs and the values are the overall averages
                zip_iterator = zip(Management_System._recordList, Management_System._overall_avg)
                x = dict(zip_iterator)

                inp = input("Please enter the avg:\n")

                result1 = {
                    key: value
                    for (key, value) in x.items() if value > inp
                }
                # list all the keys that is greater than inp
                keys = list(result1.keys())
                print("The IDs that have greater average are: ", keys)

                result2 = {
                    key: value
                    for (key, value) in x.items() if value < inp
                }
                # list all the keys that is less than inp
                keys = list(result2.keys())
                print("All the IDs that have less average are: ", keys)

                result3 = {
                    key: value
                    for (key, value) in x.items() if value == inp
                }
                # list all the keys that is equal to the inp
                keys = list(result3.keys())
                print("All the IDs that have the same average are: ", keys)

            elif answer == '2':
                # creating a dictionry, keys => IDs and the values are the taken hours
                zip_iterator = zip(Management_System._recordList, Management_System._takenHours)
                x = dict(zip_iterator)

                inp = input("Please enter the taken hours:\n")

                result1 = {
                    key: value
                    for (key, value) in x.items() if value > inp
                }
                # list all the keys that is greater than inp
                keys = list(result1.keys())
                print("The IDs that have greater total hours are: ", keys)

                result2 = {
                    key: value
                    for (key, value) in x.items() if value < inp
                }
                # list all the keys that is less than inp
                keys = list(result2.keys())
                print("All the IDs that have less total hours are: ", keys)

                result3 = {
                    key: value
                    for (key, value) in x.items() if value == inp
                }
                # list all the keys that is equal to the inp
                keys = list(result3.keys())
                print("All the IDs that have the same total hours are: ", keys)

            elif answer == '3':
                break
            else:
                print("invalid input!!\n")
                continue


class Student(Management_System):
    # instance methods
    def student_statistics(self):
        Admin.student_statistics(self)

    def global_statistics(self):
        Admin.global_statistics(self)


# ======================= *** Main*** ==================================
import matplotlib.pyplot as plt
import re

while True:
    val = input("Login as: \n[1] Admin\n[2] Student\n[3] Exit \n")
    if val == '1':
        while True:
            choice = input(
                "*** ADMIN MENU ***\n[1] Add a new record file\n[2] Add a new semester with student course and "
                "grades\n[3] Update\n[4] Student statistics\n[5] Global statistics\n[6] Searching\n[7] Exit\n")

            if choice == '1':
                Admin.addNewRecordFile(1)
            elif choice == '2':
                Admin.getInfo(1)
            elif choice == '3':
                Admin.update(1)
            elif choice == '4':
                Admin.student_statistics(1)
            elif choice == '5':
                Admin.global_statistics(1)
            elif choice == '6':
                Admin.searching(1)
            elif choice == '7':
                break
            else:
                print("Invalid input! Please try again\n")
                continue

    elif val == '2':
        while True:
            choice = input("*** STUDENT MENU ***\n[1] Student statistics\n[2] Global Statistics\n[3] Exit\n")

            if choice == '1':
                Student.student_statistics(1)

            elif choice == '2':
                Student.global_statistics(1)

            elif choice == '3':
                break
            else:
                print("Invalid input! Please try again\n")
                continue

    elif val == '3':
        exit(0)

    else:
        print("Invalid input! Please try again\n")
        continue
