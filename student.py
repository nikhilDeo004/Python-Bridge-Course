role=input("Enter your role (student/teacher): ")
age=int(input("Enter your age: "))
result = (role == "student" and age < 18) and "Eligible for Discount" or (role == "teacher" and age >= 18) and "Not Eligible for Discount"
print("Eligible : ",result)