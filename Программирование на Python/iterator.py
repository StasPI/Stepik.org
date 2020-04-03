from random import random


class RandomIterator():
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


for x in RandomIterator(10):
    print(x)

# №2
# class DubleElementListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0

#     def __next__(self):
#         if self.i < len(self.lst):
#             self.i += 2
#             return self.lst[self.i - 2], self.lst[self.i - 1]
#         else:
#             raise StopIteration


# class MyList(list):
#     def __iter__(self):
#         return DubleElementListIterator(self)


# for pair in MyList([1, 2, 3, 4]):
#     print(pair)

# №3

# def random_generator(k):
#     for i in range(k):
#         yield random()


# gen = random_generator(3)
# for i in gen:
#     print(i)
