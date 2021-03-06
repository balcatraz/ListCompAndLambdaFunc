""" 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda n: ((n % 2) == 0), list1))
print(result)

result = list(filter(lambda n: ((n % 2) == 1), list1))
print(result)

""" 2)
find which days of the week have exactly 6 characters.
"""

weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


result = list(filter(lambda n: (len(n) == 6), weekdays))
print(result)


""" 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

"""

list2 = ["orange", "red", "green", "blue", "white", "black"]

result = list(filter(lambda n: (n != "orange" and n != "black"), list2))
print(result)

""" 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 """

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

result = list(filter(lambda n: (n not in list2), list1))
print(result)

""" 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

"""

list1 = ["red", "black", "white", "green", "orange"]

result = list(filter(lambda n: ("ack" in n), list1))
print(result)

result = list(filter(lambda n: ("abc" in n), list1))
print(result)

""" 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
"""

check = lambda s: any(
    [str(s).isupper, str(s).islower, str(s).isnumeric(), len(str(s)) > 8]
)

""" 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""
