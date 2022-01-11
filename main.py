#Fundamental Data Types
# print(type(6)) ## int
# print(type(6 + 2)) ## int
# print(type(6 - 2)) ## int
# print(type(2 / 4)) ## float
# print(2 ** 3)
# print(8 % 7)


#math functions 
#print(round(3.4))
#print(abs(-45)) #absolute value means no negative numbers => 45

# birth_year = input('What year were you born?')
# your_age = 2021 - int(birth_year)
# print(f'You are {your_age} years old')

# user_name = input('What\'s your name? ')
# password  = input('Give me a password: ')


# print(f'Hello {user_name}, your password {"*" * len(password)} is {len(password)} ')


# test_list = [
#   'add',
#   'this',
#   'stuff'
# ]

# new_list = test_list[0:2]
# test_list[1] = 'remove'
# print(new_list)
# print(test_list)

#SHORT CIRCUIT
# value1 = True
# value2 = False
# if value1 or value2: 
#   print('evaluate true')
# else:
#   print('evaluate false')

#LOGICAL OPERATOR EXERCISE

# is_magician = False
# is_expert = False

# if is_magician and is_expert:
#   print('You are a master magician')
# elif is_magician and not is_expert:
#   print('at least you are getting there ')
# else:
#   print('you are need magic power')

# print(True == 1)  #True
# print('' == True) #False
# print([] == True) #False
# print(10 == 10.0) #True
# print([] == [])   #True\

# #LOOPING EXCERCISE
# my_list = [1,2,3,4,5,6,7,8,9,10]
# result = 0

# for i in my_list:
#   print(f'Result inside for {result}')
#   result += i

# print(f"Result outside for {result}")

# #ENUMERATE() EXERCISE
# for index, item in enumerate(list(range(100))):
#   if item == 50:
#     print(index , index)


# #Exercise!
# #Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]

# for row in picture:
#   row_string = ''
#   for char in row:
#     if char:
#       row_string += '*'
#     else:
#       row_string += ' '
#   print(row_string)

# # EXCERCISE CHECK DUPLICATE VALUES
# random_list = ['a', 'b', 'c', 'a', 'd', 'e', 'b', 'd', 'g','n',"n"]
# duplicate_list = []
# for value in random_list:
#   if random_list.count(value) > 1:
#     if value not in duplicate_list:
#       duplicate_list.append(value)
# print(duplicate_list)

# # Docstring in use

# def simple_sum ():
#   '''
#     This function adds two hardcoded number
#   '''
#   return 3 + 4;
# print(simple_sum.__doc__)

# HIGHEST EVEN EXERCISE

# def highest_even(li):
#   result = []
#   for n in li:
#     if n % 2 == 0:
#       result.append(n)
  
#   return max(result)
#   #TH CODE BELOW WAS MY SOLUTION BUT THE SOULTION ABOVE IS FAR MORE BETTER
#   # result.sort()
#   # return result[len(result)-1]

# print(highest_even([10,2,3,984,6,11,88]))

## DATA COMPREHENSIONS
# my_dict = {item: item**3 for item in [1,2,3,4]}
# print(my_dict)

# COPMREHENSION EXERCISE
random_list = ['a', 'b', 'c', 'a', 'd', 'e', 'b', 'd', 'g','n',"n"]
duplicate_list = list(set([value for value in random_list if random_list.count(value) > 1]))
# for value in random_list:
  # if random_list.count(value) > 1:
  #   if value not in duplicate_list:
  #     duplicate_list.append(value)
print(duplicate_list)

