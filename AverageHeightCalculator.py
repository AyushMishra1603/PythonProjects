 #🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  n += 1
TotalHeight=0
for Height in student_heights:
  TotalHeight += Height 
Average = round(TotalHeight/n)
print(f"Average height of Students is {Average}")
