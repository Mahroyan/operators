print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("maths :"))
english = int(input("english :"))
science = int(input("science :"))
urdu = int(input("urdu :"))

sum = math+english+science+urdu
percentage = (sum/400)*100

print(end="Your Percentage Marks = ")
print(percentage)