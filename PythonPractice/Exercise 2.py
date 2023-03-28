import random


"""Exercise 2(Password generator)"""


s = "abdefgkjdmflgodmsokdw0123456789ABCDEFKIOLKFKLOPBVCM!@#$%^&*()?"

passlen = 8

p = "".join(random.sample(s,passlen))

print(p)
