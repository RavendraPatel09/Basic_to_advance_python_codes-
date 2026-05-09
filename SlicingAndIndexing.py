l1=[1,2,3,4,5,6,7,8,9,10]
print(l1[:])
print(l1[2:5])
print(l1[:4])
print(l1[5:])
print(l1[::2])
print(l1[::-1])
print(l1[1:8:3])
#this operation will give every second element from index 1 to index 7
#slicing means that we can choose from where to start and where to end and also the step size
#it has three parts start:end:step
l2=[1,2,3,4,5,6,7,8,9,10]
l2[3]=5,6,7
print(l2)
#this operation will replace the element at index 3 with three elements 5,6,7
#this is now act as nested list at the index 3