'''def ask_for_input():
    number = input("Please enter a number: ")
    if int(number) % 2 == 0:
        print(str(number) + " is an even number.")
    else:
        print(str(number) + " is an odd number.")


ask_for_input()'''

'''#List Practice
mylist = [8, 3, 6, 3, 8]
newlist = []
newlist2 = []
newlist3 = []

for e in mylist:
    newlist.append(e + 1)
    newlist2.append(e * 2)
    if e % 2 != 0:
        newlist3.append(e)

print(mylist)
print(newlist)
print(newlist2)
print(newlist3)'''

'''#Alternative way for above list practice
mylist = [8, 3, 6, 3, 8]
newlist = [(e +1) for e in mylist]
newlist2 = [(e * 2) for e in mylist]
newlist3 = [e for e in mylist if e % 2 != 0]
print(newlist)
print(newlist2)
print(newlist3)'''

