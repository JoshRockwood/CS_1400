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

import sys

test_file = sys.argv[1]

line_count = 0
char_count = 0

with open(test_file, "r") as input_file:
    line = input_file.readline()
    while line != "":
        line_count += 1
        char_count += len(line)
        line = input_file.readline()

print("{} lines".format(line_count))
print("{} characters".format(char_count))

import sys, csv

test_file = sys.argv[1]

total1 = 0
total2 = 0
total3 = 0
total4 = 0
row_count = 0

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file)
    for num1, num2, num3, num4 in reader:
        row_count += 1
        total1 += int(num1)
        total2 += int(num2)
        total3 += int(num3)
        total4 += int(num4)

print("{} {} {} {}".format(total1/row_count, total2/row_count, total3/row_count, total4/row_count))

import sys

test_file = sys.argv[1]

with open(test_file, "r") as input_file:
    lines = input_file.readlines()
    lines.reverse()
    for line in lines:
        print(line)

import sys, csv

test_file = sys.argv[1]

oldest_age = 0
oldest_name = ""

with open(test_file, "r") as input_file:
    reader = csv.reader(input_file, delimiter="\t")
    next(reader)
    for name, age, career in reader:
        if int(age) > oldest_age:
            oldest_age = int(age)
            oldest_name = name
print("The oldest person is {}.".format(oldest_name))


import sys, csv

test_file = sys.argv[1]
cities = []

with open (test_file, "r") as input_file:
    reader = csv.reader(input_file)
    next(reader)

    for city, country, latitude, longitude in reader:
        if int(latitude) < 0:
            cities.append(city)

print("The following cities are in the Southern Hemisphere: ", end="")
for city in cities:
    if city == cities[-1]:
        print(city + ".")
    else:
        print(city + ", ")

import csv

with open("student_folder/csv/superheroes.csv", "w") as output_file:
  writer = csv.writer(output_file, lineterminator="\n")
  writer.writerow(["Superhero", "Power"])

  print("Enter 'stop' to quit the program")

  name = input("Enter the superhero's name: ")
  power = input("Enter their superpower: ")

  while True:
    writer.writerow([name, power])
    name = input("Enter the superhero's name: ")
    if name == "stop":
      break
    power = input("Enter their superpower: ")