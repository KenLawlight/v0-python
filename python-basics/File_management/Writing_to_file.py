file =open("output.txt","w")
file.write("Hello Python\n")
file.write("File handling is useful")
file.close()

print("********************")

name =input("Enter student name: ")

file =open("students.txt","a")
file.write(name +"\n")
file.close()


