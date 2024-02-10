greeting = "Good Morning"
a = 4
if a > 2:
    print("Condition matches")
    print("second line")
else:
    print("condition do not match")
print("if else condition code is completed")

# for loops

obj = [2,3,5,7,9]
for i in obj:
    print(i*2)

# sum of first natural number 1=2=3=4=5 = 15
summation = 0
for j in range(1,6): #range(i,j) -> i to j-1
    summation = summation + j
    print(j)