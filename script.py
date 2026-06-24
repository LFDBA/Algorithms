import random
list = [None] * 10
for i in range(len(list)):
    list[i] = random.randint(1, 100)


#stalin
def stalin(list):
    i = 0
    #Go through items
    while i < len(list) - 1:
        #if left is larger than right
        if list[i] > list[i + 1]:
            #delete right
            del list[i + 1]
        #otherwise
        else:
            #move on
            i += 1

#difference between del and pop() in Python is that:
#pop() removes an element and returns its value, 
#while the del keyword removes the element without returning anything.


print(list, "\n")
stalin(list)
print(list)
