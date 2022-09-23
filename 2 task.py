import sys

a = (sys.argv[1]) 

if type(a) == int:
    print("int")
elif type(a) == str:
    print("string")
elif type(a) == list:
    print("list")
else:
    print("I don't know :(")
