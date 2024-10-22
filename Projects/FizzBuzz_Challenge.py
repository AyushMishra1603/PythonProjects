#FizzBuzz Challenge
for number in range(1,101):
  #check if the number is divisible by 3 and 5
  if number%3==0 and number%5==0:
    print("FizzBuzz")
  #check if the number is divisible by 3
  elif number%3==0:
    print("Fizz")
  #check if the number is divisible by 5
  elif number%5==0:
    print("Buzz")
  else:
    print(number)
