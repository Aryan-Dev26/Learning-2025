# m1 = input("Enter 1st movie : ")
# m2 = input("Enter 2nd movie : ")
# m3 = input("Enter 3rd movie : ")
# movies  = []
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)

# print(movies)

l1 = [1,2,3,2,1]
l2 = [1,2,3,4,5]

cl1 = l1.copy()
cl1.reverse()

cl2 = l2.copy()
cl2.reverse()

if(l1 == cl1):
    print("l1 is Palindrome")
else:
    print("l1 is not a Palindrome")


if(l2 == cl2):
    print("l2 is Palindrome")
else:
    print("l2 is not a Palindrome")



tup = ["C","D","A","A","B","B","A"]

cnt = tup.count("A")
print(cnt)
cl3 = tup.copy()
cl3.sort()
print(cl3)