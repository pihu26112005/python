
#Iterable: An iterable is any Python object , meaning you can go through its elements one by one.
           #there are two common ways to make an object iterable: 
                                                    # by implementing the __iter__() and __next__() methods (to create an iterator) or
                                                    # by implementing the __getitem__() method

# Iterator:
        #An iterator is an object that represents a stream of data, and it provides a way to access elements one at a time

my_iterable = [1, 2, 3]
my_iterator = iter(my_iterable)  # Create an iterator from an iterable
print(next(my_iterator))  # Outputs: 1
print(next(my_iterator))  # Outputs: 2
print(next(my_iterator))  # Outputs: 3
#or
print(my_iterator.__next__)  # Outputs: 1
print(my_iterator.__next__)  # Outputs: 2
print(my_iterator.__next__)  # Outputs: 3
