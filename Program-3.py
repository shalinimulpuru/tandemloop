# Problem-3: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5
#     5) input a = 5, then output : 1, 3, 5, 7, 9
#     6) input a = 6, then output : 1, 3, 5, 7, 9

def num_series(nums):
    series = nums if nums%2==1 else nums-1
    c=[]
    for i in range (1,2*series,2):
        c.append(i)
    print(* c)

nums = int(input())
num_series(nums)        

