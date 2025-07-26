# find maximum number of function
def maximum_number(a,b):
    return a if a > b else b

print(maximum_number(4,6))

#
def maximum_number(a,b,c):
    return a if a > b  and  a > c else b if b > c else c

print(maximum_number(72,567,345))

#practice1
def max_function(a,b):
    return a if a < b else a

print(max_function(2,3))

#practice 2
def max_function(x,y,z):
    return x if x < y and y > z else x if x > z else z

print(max_function(4,5,6))
