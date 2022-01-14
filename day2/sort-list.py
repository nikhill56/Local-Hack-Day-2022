n=int(input('Enter the number of list elements'))
lis=[]
for i in range(n):
    lis.append(input())

print('Unsorted list is')
for i in range(len(lis)):
    print(lis[i])
lis.sort()
print('Sorted list is')
for i in range(len(lis)):
    print(lis[i])
