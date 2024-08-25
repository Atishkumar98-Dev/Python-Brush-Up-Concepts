# this is set used in list
l = [1,2,3,3,3,4,4,4,5]
list1 = set(l)
print(list1)

# this is list
list_of_numbers = [1,2,3,4,4,5,5,5,5,6,6,]
h = list(list_of_numbers)
print(h)

library_1 = {'harry puttar', 'Harry kuttar', 'leend harry'}
library_2 = {'harry puttar', 'fakir', 'uselesstext'}

Book = library_1.union(library_2)
print(Book)

library_1 = {'harry puttar', 'Harry kuttar', 'leend harry'}
library_2 = {'harry puttar', 'fakir', 'uselesstext'}

Both_Books = library_1.intersection(library_2)
print(Both_Books)

library_1 = {'harry puttar', 'Harry kuttar', 'leend harry'}
library_2 = {'harry puttar', 'fakir', 'uselesstext'}

Not_Common_Both_Books = library_2.difference(library_1)
print(Not_Common_Both_Books)
