print("hello")
# here are the comments i have defined

a = 3
print(a)

str = "Hello world"
print(str)

b,c,d = 5,6.4, "Great"

str = "Hello world"
print(str)
# data types in python
#print("value is" +b)
print("{} {}". format("value is " , b))
print(type(b))
print(type(c))
print(type(d))

# list datatype and its operation to manipulates
values = [1,2, "rahul", 4,5]
# list is the data type that allows multiple values and can be different data types
print(values[0])    # 1
print(values[3])    #4
print(values[-1])   #5
print(values[1:3])  #2 rahul 4
values.insert(3, "Shetty")
print(values)
values.append("end")
print(values)

values[2] = "RAHUL" #updating
del values[0]
print(values)

# tuple - same as list data type but immutable

val = [1,2, "rahul", 4.5]
print(val[1])

val[2] = "RAHUL"
print(val)