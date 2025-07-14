student = {}

studentname = input("Enter your students name: ")
student("Name") = studentname

studentage = input("Enter your students age: ")
student("Age") = studentage

studentgrade = input("Enter you'r students grade: ")
student("Grade") = studentgrade

hobies = []
hobby = input("Enter your students hobby; Type 'done' when done: ").lower()
hobies.append(hobby)

while hobby != "done":
    hobby = input("Enter your students hobby; Type 'done' when done: ").lower()

student["Hobbies"] = hobies

print(student)