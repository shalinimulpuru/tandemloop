# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7 


def num_series(nums):
    c=[]
    for i in range(1,2*nums,2):
            c.append(i)
    print(* c)

nums = int(input("enter a number:"))
num_series(nums)




