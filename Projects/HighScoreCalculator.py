# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
each_score =0
max_score = 0
for score in student_scores:
  each_score = score
  if max_score < score:
    max_score = each_score
  
print(f"The highest score in the class is:{max_score}")
