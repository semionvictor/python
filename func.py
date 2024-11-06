# def get_person(name,age,lifetime_function):
#     lifetime = lifetime_function(age)
#     return f"yout name is {name},you are {age} years old,you have lived for {lifetime}months"

# def get_lifetime(age):
#     return age * 12


# statement = get_person("chiboy",10, get_lifetime)
# print(statement)
# map
# ages = [12,2,10,20,30,50]
# def calculate_month(age):
#     return age *12
# monthages = map(calculate_month,ages)
# print(monthages)
# list_ages =list(monthages)
# print(list_ages)
# # # map,filter,reduce'
# numbers = [10,13,15,4,6,17,20]
# def filter_even_numbers(numbers):
#     if numbers % 2 == 0:
#         return True
#     else:
#         return False
# even_numbers =filter(filter_even_numbers,numbers)
# list_numbers = list(even_numbers)
# print(list_numbers)
# # reduce
# from functools import reduceff
# numbers = [10,20,30,40,50,60,70]
# def reducer (acc,number):
#     print(acc)
#     return acc + number
# result = reduce (reducer,numbers)
# print(result)

# names = ["kyrian","chiboy","swat"]
# def operation_function(name):

#     return name +"s"
# result = map(operation_function, names)
# print(list(result))

numbers = [10,13,13,4,25,20,12]

def filter_odd_numbers(number):
    return number %2 != 0

odd_numbers = lambda number : number %2 != 0
result = filter(filter_odd_numbers, numbers)
print(list(result))
# odd_numbers = filter(filter_odd_numbers, numbers)
# print(list(odd_numbers))