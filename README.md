# UNIVERSITY REGISTRAR'S OFFICE APPLICATION

#####There are two main components in the application; courses and students.

  There are initially two text files; course.txt and students.txt. Format of the files are given below. 
  This application reads those files when it runs. The system will start with a menu and run 
  until exit option is selected. When the exit option is selected in menu, the updated versions 
  of course and student files(or others that might be needed) will be saved, so that, when the 
  application runs again, the operations done in the previous sessions are not lost.
  
*student.txt : it contains the 6 digit id, name and last name of a student, the list of course 
codes separated by comma for the courses this student registered to. Every column is 
separated by semicolon(;) in this file.

  117987;ibrahim Kaptan;CENG1234,CENG2345
  124876;Ayse Yılmaz;CENG1234

*course.txt : it contains course code, course name, instructor name and student count fields. 
Student count gives the number of students registered in the course. Every column is 
separated by semicolon(;) in this file.
  
  CENG1234;Data Structures and Algorithms;Mark Twain;2
  CENG2345;Programming Languages;Mark Lutz;8
  
#####It has these features:
  *List all the courses.
  *List all the course that have at least one student registered.
  +Add a new course.
  *Search a course by course code.
  *Search a course by name.
  *Register a student to a course.
  *List all the students their registered courses.
  *List top 3 most crowded courses.
  *List top 3 students with the most course registrations.
  
