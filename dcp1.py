'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.'''

list=[int(x) for x in input().split(" ")]
k=int(input())
def test(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (k==list[i]+list[j]):
                return True
    return False
print(test(list))
