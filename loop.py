
# i=1
# while i<100:
#     print("Hello World!")
#     i=i+1;


# student_marks = {"umesh": -5 , "ram":50, "shyam":80};
# while True:
#     students_name=input("Enter Your Name:");
#     print(f"mark is {student_marks[students_name]}")





# Students marks
# students = {"ram": -22,"hari":42,"sita":52};
# while True:
#     students_name = input("Enter student name ");
#     print(f"The student marks is  {students[students_name]}")




# Function
# def info(fn,ln, age):
#     print(f'Hi {fn} {ln}. Your age {age}')
# info("ram", "thapa", 23)

# info(age=26, fn="ram", ln="thapa")



# Unlimited Arguments pass
# def add(*args):
#     sum= 0
#     for item in args:
#      sum = sum+item
#     print(sum);
# add(2,7,3,6);


# keyword with value unlimited
# def info(**kwargs):
#     print(kwargs)
#     for k,v in kwargs.items():
#         print(k,v)
#         print('********')
# info(name="ram", age=30)
# info(name="shyam", lastname="thapa", age=20, )




# return in Function
# def average(*args):
#     sum=0
#     for item in args:
#         sum = sum + item
#     mean = sum / len(args) 
#     return mean

# avg = average(1000, 25000,4000)
# if(avg<1000):
#     print("Poor")
# else:
#     print("Rich")


# Function inside Function
# def add(*args):
#     sum=0
#     for item in args:
#         sum = sum + item
#     return sum

# def average(*args):
#     total_sum=add(*args)
#     mean = total_sum / len(args)
#     return mean

# avg= average(25000,3500,2200)
# print(avg)



# def check_num(*args):
#         for num in args:
#             if(num%2)==0:
#                 print(f"{num} is even")
#             else:
#                 print (f"{num} is odd")


# while True:
#     enter_number=int(input("Enter a number: "))
#     check_num(enter_number)





# def is_even(args):
#             if(args%2)==0:
#                 return True
#             else:
#                 return False


# while True:
#     enter_number=int(input("Enter a number: "))
#     value = is_even(enter_number)
#     if(value):
#         print(f"{enter_number} is even")
#     else:
#         print(f"{enter_number} is odd")




# Calculator

# def addition(first_number, second_number):
#     return (first_number + second_number)

# def subtraction(first_number, second_number):
#     return (first_number-second_number)

# def multification(first_number, second_number):
#     return (first_number*second_number);


# def division(first_number, second_number):
#     return (first_number/ second_number)


# while True:
#     first_number= int(input("Enter First Number: "));
#     second_number = int(input("Enter second Number: "));
#     input_operator= (input("Enter Operating Sign: "))

#     if(input_operator=="+"):
#         add=addition(first_number, second_number);
#         print(f"The added final value is {add}")
#     elif(input_operator=="-"):
#         sub=subtraction(first_number, second_number)
#         if(sub<0):
#             sub=sub*-1
#             print(f"The subtracted final value is {sub}")

#     elif(input_operator=="*"):
#         mul=multification(first_number, second_number);
#         print(f"The multiplied final value is {mul}")
#     elif(input_operator=="/"):
#         if(first_number>=second_number):
#             div=division(first_number, second_number)
#             print(f"The divided final value is {div}")
#         else:
#             div=division(first_number, second_number)
#             print(f"The divided final value is {div}")





# my_list = range(1,11)
# for n in my_list:
#     print(n)


# even_list = []
# odd_list=[]


# def odd_even(my_list):
#     for  item in my_list:
#             if item%2==0:
#                 even_list.append(item)
#             else:
#                 odd_list.append(item)


# odd_even(my_list)






# Exceptional Handling
# while True:
#     try:
#         # Risky code
#         a= int(input("Enter fist number: "))
#         b= int(input("Enter second number: "))
#         print(f"{a} divided by {b} is {a/b}")
#     except:
#         # code to run when there is an error
#         print("Number cannot be divided by 0")




# while True:
#     try:
#         # Risky code
#         a= int(input("Enter fist number: "))
#         b= int(input("Enter second number: "))
#         print(f"{a} divided by {b} is {a/b}")
#     except Exception as e:
#         # code to run when there is an error
#         print(e)
#     finally:
#         print("Thank You for using")



# while True:
#     try:
#         # Risky code
#        Open Database
#        read database value
#     except Exception as e:
#         # code to run when there is an error
#         print(e)
#     else: 
#         Close database
#     finally:
#         print("Thank You for using")



