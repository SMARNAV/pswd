import words
import secret_number
import hashlib
import sys
import random

random.seed(a=sys.argv[1]+secret_number.secret)

b = []

for x in range(1,5):
    b.append(random.choice(words.list))
b.append("A")
print('#'.join(b))
