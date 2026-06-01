#from string import ascii_letters

#for i in ascii_letters:
#    for j in ascii_letters:
#        for k in ascii_letters:
#            for l in ascii_letters:
#                print(i, j, k, l)
# This code will print all possible combinations of 4 letters (from aaaa to zzzz).

from string import ascii_letters, digits, punctuation
# This code will print all possible combinations of 4 characters (from aaaa to zzzz, including digits and punctuation).
for i in ascii_letters + digits + punctuation:
    for j in ascii_letters + digits + punctuation:
        for k in ascii_letters + digits + punctuation:
            for l in ascii_letters + digits + punctuation:
                print(i, j, k, l)
