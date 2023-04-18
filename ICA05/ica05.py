# Q1: Create the following data structures using list comprehensions

# a) Create a list named l consisting of the numbers from 1 to 9 and print it.
l = [i for i in range(1,10)]
print("Q1a: l=", l)

# b) Create a dictionary named d that maps the words one, through nine to the numbers 1 thru 9 and print it.
words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
d = {words[i]: i+1 for i in range(0,9)}
print("Q1b: d=", d)

# Q2: Create lists using list comprehensions and print them.

# a) Create a list named olist that contains all the odd number values of the list l and print it.
olist = [x for x in l if x % 2 == 1 ]
print("Q2a: olist=", olist)

# b) Create a list named elist that contains all the even number values of the list l and print it.
elist = [x for x in l if % 2 == 0]
print("Q2b: elist=", elist)
