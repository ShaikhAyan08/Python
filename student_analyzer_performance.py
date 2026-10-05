maths = int(input("Enter the marks of Maths : "))
python = int(input("Enter the marks of Python : "))
dbms = int(input("Enter the marks of DBMS : "))
total_marks = maths + python + dbms
print("Total Marks : ",total_marks)
percentage = (total_marks / 300)*100
print("Percentage : ",percentage)

if (maths < 40 or python < 40 or dbms < 40) :
    print("Fail")
else :
    print("Pass")
