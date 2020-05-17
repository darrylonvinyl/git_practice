"""
Divisible by Ten

Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.
"""
#Write your function here
def divisible_by_ten(nums):
  can_divide_by_10 = len([num for num in nums if num % 10 == 0])
  return can_divide_by_10
#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

"""
Greetings

Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

Return the new list containing the greetings.
"""
#Write your function here
def add_greetings(names):
  greetings = []
  for i in names:
    greetings.append("Hello, "+i)
  return greetings
#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

"""
Delete Starting Even Numbers

Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!
"""
#Write your function here
def delete_starting_evens(lst):
  x = 0
  for num in lst:
    if num % 2 == 0:
      x += 1
      continue
    if num % 2 != 0:
      break
  return lst[x:]
#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

"""
Odd Indices

Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].
"""
#Write your function here
def odd_indices(lst):
  new_lst = []
  x = 1
  while x < len(lst):
    for item in lst:
      if x % 2 != 0:
        new_lst.append(lst[x])
      x += 1
  return new_lst
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

"""
Exponents

Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

exponents([2, 3, 4], [1, 2, 3])
the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.
"""
#Write your function here
def exponents(bases,powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

"""
Larger Sum

Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.
"""
#Write your function here
def larger_sum(lst1,lst2):
  sum_of_lst1 = 0
  sum_of_lst2 = 0
  for x in lst1:
    sum_of_lst1 += x
  for x in lst2:
    sum_of_lst2 += x
  if sum_of_lst1 == sum_of_lst2 or sum_of_lst1 > sum_of_lst2:
    return lst1
  else:
    return lst2
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

"""
Over 9000

Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.
"""
#Write your function here
def over_nine_thousand(lst):
  if len(lst) == 0:
    return 0
  sum_of_lst = 0
  for x in lst:
    if sum_of_lst < 9000:
      sum_of_lst += x
    elif sum_of_lst > 9000:
      return sum_of_lst
  return sum_of_lst
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

"""
Max Num

Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums
"""
#Write your function here
def max_num(nums):
  x = nums[0]
  for num in nums:
    if num > x:
      x = num
  return x
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

"""
Same Values

Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])
"""
#Write your function here
def same_values(lst1,lst2):
  new_lst = []
  for x in range(len(lst1)):
    if lst1[x] == lst2[x]:
      new_lst.append(x)
  return new_lst
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

"""
Reversed List

Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.
"""
#Write your function here
def reversed_list(lst1,lst2):
  rev_lst1 = []
  rev_index = -1
  for x in lst1:
    rev_lst1.append(lst1[rev_index])
    rev_index += -1
  if rev_lst1 == lst2:
    return True
  else:
    return False
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
