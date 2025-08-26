nums = (1 , 4, 9 ,16, 25, 36, 49, 64, 81, 100)
n = int(input("Which Number :"))
i=0

while i<len(nums):
    if (nums[i]==n):
        print("found at place", i)
    
    i+=1    
else:
     print("Does not Exist")