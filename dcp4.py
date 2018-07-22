'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place
'''

list1=[int(x) for x in input().split()]
list1=sorted(list1)
list1=set(list1)
list1=list(list1)
if(1 in list1):
    for i in range(1,len(list1)-1):
        if(list1[i+1]-list1[i])!=1:
            print(i+1)
            break
else:
    print("1")


