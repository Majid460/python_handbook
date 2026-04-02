# Given [1,2,3,4,5,6], keep only even numbers → [2,4,6].
list_a = [1, 2, 3, 4, 5, 6]

# for i in range(len(list_a)):
#     if list_a[i] % 2 == 0:
#         print(f"Number is even,{list_a[i]}")

res = [print(i) for i in list_a if i%2==0]

r = list(filter(lambda x:x%2==0,list_a))
print(r)



# Filter strings containing a letter



# Filter numbers greater than a threshold