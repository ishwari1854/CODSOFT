print("this is task1")

while True:
  print("-----SIMPLE CALCULATOR-----")
  print("1.Addition")
  print("2.Subtraction")
  print("3.Multiplication")
  print("4.Division")

  choice = int(input("enter your choice(1/2/3/4):"))
  num1= float(input("enter first number:"))
  num2=float(input("enter second number:"))

  if choice== 1:
        print("result=",num1+num2)
  elif choice == 2:
      print("result =",num1-num2)

  elif choice ==3:
      print("result =",num1*num2)
      
  elif choice ==4:
        if num2==0:
                print("cannot divide by zero")
        else :
                print("result=", num1/num2)

  else:
    print("invalid choice")

  again = input("Do you want to calculate again? (yes/no): ")

  if again.lower() != 'yes':
        print("Thank you for using calculator!")
        break
