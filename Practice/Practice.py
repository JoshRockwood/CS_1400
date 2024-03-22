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

###############

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

###############

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

###############

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


###############


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


###############


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


################

def dic_gen(n):
    d = dict()
    for i in range(1, n+1):
        d[i] = i * i
    return d


def main():
    n = 5
    d = dic_gen(n)
    print(d)


if __name__ == "__main__":
    main()

##################

v = {'a': 5, 'b': (2, 3, 4), 'c': [{'d': 10, 'e': 20}]}
# To access the value 10 need to access dictionary first
v['c'][0]['d']

###############

# WRITE YOUR CODE HERE


# test code below
if __name__=="__main__":
  cities = {
    'London' : 'England',
    'Mumbai' : 'India',
    'Lausanne' : 'Switzerland',
    'Estes Park' : 'Colorado'
  }


def key_position(d, k):
  keys = list(d.keys())

  if k in keys:
    return keys.index(k)
  else:
    return 'Key not found'

print(key_position(cities, 'Boston'))

###############

if __name__ == "__main__":
  example_dict = {
    1 : ['red', 'blue', 'green'],
    'Josh Jung' : (9, 10),
    3 : {0 : 0},
    9000 : 'impale mat a'
  }

def find_key(d, v):
  keys = list(d.keys())
  values = list(d.values())
  index = values.index(v)
  return keys[index]

key = find_key(example_dict, v)
print(key)

###############

if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
  }

def move_to_bottom(d, k):
  if k not in d:
    return 'The key is not in the dictionary'
  else:
    value = d.pop(k)
    d[k] = value
    return d

print(move_to_bottom(example_dict, 4))

###############

if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: (4, 5)
    }


def swap(d):
    keys = d.keys()
    values = d.values()
    swapped_tuples = zip(values, keys)
    value_types = [type(elem) for elem in values]

    if type({}) in value_types or type([]) in value_types:
        return 'Cannot swap the keys and values for this dictionary'
    else:
        new_dict = dict(swapped_tuples)
        return new_dict


swapped = swap(example_dict)
print(swapped)

###############

if __name__ == "__main__":
  example_dict = {
    1 : 'one',
    2 : 'two',
    3 : [4, 5]
  }

def is_nested(d):
  values = d.values()
  value_types = [type(elem) for elem in values]
  if type(()) in value_types or type([]) in value_types or type({}) in value_types:
    return True
  else:
    return False

print(is_nested(example_dict))

###############

if __name__ == "__main__":
    import sys
    import json

    file1 = sys.argv[1]
    file2 = sys.argv[2]


def compare(f1, f2):
    with open(f1) as file1, open(f2) as file2:
        data1 = json.load(file1)
        data2 = json.load(file2)
        if data1 == data2:
            return 'The dictionaries are equal'
        else:
            count1 = len(data1)
            count2 = len(data2)
            if count1 > count2:
                return 'Dictionary 1 is longer than dictionary 2'
            elif count2 > count1:
                return 'Dictionary 2 is longer than dictionary 1'
            else:
                return 'Dictionary 1 and dictionary 2 have the same length'


print(compare(file1, file2))

###############