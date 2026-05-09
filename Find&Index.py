s ='hello how are you sam'#this is the string that we created 
x = s.find('o')# this is used to find the first occurrence of the character or substring
#used to find the index also where the element first appears in the string 
print(x)#syntax find(sub,start,end)
# if there is no such element it will return -1
#if the element is not available in the string it will return -1
s1 = 'Hey man'
x1 =s1.find('R')#this will return -1 as R is not present in the string
print(x1)
#if we want to find the last occurrence of the character or substring we can use rfind()
s2 = 'hello how are you samarth'
x2 = s2.rfind('o',1,20)#we just gives the start and end index
print(x2)#starts from the right side of the string
# we can also use index() function to find the first occurrence of the character or substring
s3 = 'hello how are you samarth'
x3 = s3.count('o')#this will count the number of occurrences of the character or substring
print(x3)
# if the element is not present in the string it will raise a value error
s4 = 'hello how are you samarth'
x4 = s4.index('h')#this will return the index of the first occurrence of the character or substring         
print(x4)
#x4 = s4.index('z')#this will raise a value error as z is not present in the string
#print(x4)  