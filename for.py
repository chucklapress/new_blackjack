#example of a string
string = 'string'
for c in string:
    print(c)
# example of a list
list = ['orange', 'car', 1, 19]
for item in list:
    print(item)
# example of tuples
tuples = ('Kia','Toyota', 'Honda')
for car in tuples:
    print(car)
    print(tuples)

#iterating dictonaries
def ages():
    ages = {'Chuck':52, 'Elizabeth':47, 'Summer':12}
    print(ages)

    for item in ages:
        print(item[4])

    for k, v in sorted(ages.items()):
        print(k,v)
        print(v)


ages()
# appending lists
list = [1,2,3,4,5,6]
list.append(7)
list.append(8)
list.pop(4)
print(list)
#merging lists
list_one = [1, 2, 3]
list_two = [4, 5, 6]
mergedlist = []
mergedlist.extend(list_one)
mergedlist.extend(list_two)
print(mergedlist)
mergedlist = list_one + list_two
print(mergedlist)

numbers = range(0, 9)

for number in numbers:
    print(number)
#list comprehensions
doubling_down = []
for number in numbers:
    if number % 2 == 1:
        doubling_down.append(number * 2)

print(doubling_down)

doubling_down = [number * 2 for number in numbers if number % 2 == 1]
print(doubling_down)
#joins
dash = "-"
sequence = ("a", "b", "c")
print(dash.join(sequence))

comma = ','
sequence = ('a','b','c')
print(comma.join(sequence))
#using .format
print('Hello {},{}, and {}'.format('Chuck','Summer','Elizabeth'))


