nums = (1,4,9,6,25,36,49,64,81,100)
for val in nums:
    print(val)

print("End")



i = int(input("Number To be Found"))
for dgt in nums:
    if(dgt == i):
        print(i," Found")
        break
    print(dgt)
else:
    print("Does not Exist")