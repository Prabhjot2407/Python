# List 
# A list in python is an ordered, mutable and indexed colletion that allows duplicates.
# it is written in square brackets[]
# it can store mixed data types(int, float, string etc).

# my_list = [10, 20, 30, 40, "prabh"]
# print(my_list)                        # HASHCODE VALUE
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

# Updating element
# my_list[4] = "Prabhjot"
# print(my_list)

# Adding elements
# my_list.append("Singh")
# print(my_list)

# my_list.insert(2, "Vishal")
# print(my_list)

# Removing elements
# my_list.remove(40)
# print(my_list)

# del my_list[4]      # Removes elment at specific index
# print(my_list)

# print(len(my_list))


# Using for loop
# nums = [5, 3, 2, 1, 9, 10, 15, 17]
# nums.sort()
# print("List in ascending order is ", nums)

# nums.sort(reverse = True)
# print("List in descending order is ", nums)

# nums.reverse()
# print(nums)


# nums = [5, 3, 2, 1, 9, 10, 15, 17]
# print(nums[1 : 3])
# print(nums[1 : 6 : 1])
# print(nums[1 : 7 : 2])


# Que
# nums = [10, 20, 4, 45, 78, 99, 20, 34, 78]
# def second_largest(nums):
#     a = list(set(nums))          # to remove duplicate elements
#     a.sort()
#     if len(a) < 2:
#         return None
#     return a[-2]

# print("Second largest is :", second_largest(nums))


#Que
# def reverse_list(ist):
#     return ist[ : : -1]
# nums = [1, 2, 3, 4]
# print("Reversed list is ", reverse_list(nums))


# # Que
# def find_pairs(ist, target):
#     pairs = []
#     for i in range(len(ist)):
#         for j in range(i+1, len(ist)):
#             if ist[i] + ist[j] == target:
#                 pairs.append((ist[i], ist[j]))
#     return pairs

# nums = [1, 5, 7, -1, 5]
# target = 6
# print("Pairs with sum ", target, "is", find_pairs(nums, target))
