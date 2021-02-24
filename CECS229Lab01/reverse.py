def reverse(r):
    str = ""
    for i in r:
        str = i + str
    return str
r = "abcds"

print ("The original: ", end="")
print (r)

print ("Reversed: ", end = "" )
print(reverse(r))