# The function should return True if the number is between 10 and 20 (inclusive), but it doesn't. Find the bug.

num = input("Number: ")

int(num)

def is_between(num):

     if num > 10 and num < 20:

          return True

     return False

if True:
     print("This number is between 10 and 20")

     if False:
          print("This number is not between 10 and 20")