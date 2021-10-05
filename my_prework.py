def hello_name(user_name): 
    print("hello_" + (user_name).upper())
hello_name("Username!")


odd_numbers = list(range(1,100,2))
print(odd_numbers)


def max_num_in_list(a_list):
    print(max(a_list))   
max_num_in_list(list(range(1,6)))


def is_leap_year(a_year):
    if a_year % 4 == 0:
        print ("This is a leap year")
    elif a_year % 400 == 0:
        print("This is a leap year")
    elif a_year % 100 != 0:
        print("This is not a leap year")
is_leap_year((2021))




     