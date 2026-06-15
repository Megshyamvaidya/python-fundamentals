# normal way
numbers=[1,2,3,4,5]
squares=[]
for i in numbers:
    squares.append(i*i)
print("Squares",squares)
# comprehensive  way
squares=[n*n for n in numbers]
print(squares)

# using conditions
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=[n for n in numbers if n%2==0]
print(evens)
greater=[n for n in numbers if n>5]
print(greater)
even_squares=[n*n for n in numbers if n%2==0]
print(even_squares)
names=["megshyam","rahul","priya","amit"]
upper_names=[name.upper() for name in names]
print(upper_names)
long_names=[name for name in names if len(name)>4]
print(long_names)
long_upper=[name.upper() for name in names if len(name)>4]
print(long_upper)
# for dictionaries
# normal way
numbers=[1,2,3,4,5]
sqaures_dict={}
for n in numbers:
    sqaures_dict[n]=n*n
print(sqaures_dict)
# comprehensive way
sqaures_dict={n:n*n for n in numbers }
print("Comprehensive way")
print(sqaures_dict)
users=['Megshyam','Rahul','Priya']
user_dict={name:len(name) for name in users}
print(user_dict)
# lambda functions
def square(n):
    return n*n
print(square(7))
square=lambda n:n*n
print(square(8))
# add two numbers
add=lambda a,b:a+b
print(add(8,9))
is_even=lambda n:n%2==0
print(is_even(7))
print(is_even(8))
full_name=lambda first,last:f"{first} {last}"
print(full_name("Megshyam","Vaidya"))
# map,filter functions
# list
numbers=[1,2,3,4,5]
squares=list(map(lambda n:n*n,numbers))
print(squares)
# filter
numbers=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda n:n%2==0,numbers))
print(evens)
# map or mapping
numbers=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda n:n*n,numbers))
doubled=list(map(lambda n:n*2,numbers))
print(squares)
print(doubled)

# filter

evens=list(filter(lambda n:n%2==0,numbers))
print(evens)
greater=list(filter(lambda n:n>5,numbers))
print(greater)

even_squares=list(map(lambda n:n*n,filter(lambda n:n%2==0,numbers)))
print(even_squares)