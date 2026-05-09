Numbers=[1,10,2,3,2,3,4,5,5,5,7,7,8,9,3,9,9,10]
orderd_unique=(set(Numbers))
print(orderd_unique)
for i in range(1,Numbers):
    num = int(input())
    if num > Max:
        Max = num
        print()