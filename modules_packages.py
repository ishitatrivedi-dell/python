import math
import random 
random.seed(42)  # Set a seed for reproducibility
print(random.randint(1, 100))  # Generate a random integer between 1 and 100


print(random.choice([1,2,3,4,5]))  # Randomly select an element from the list

import random
 
random.seed(42)                  # set seed for reproducibility
random.random()                  # float in [0.0, 1.0)
random.uniform(1.5, 9.5)         # float in [a, b]
random.randint(1, 10)            # integer in [a, b] — both inclusive
random.randrange(0, 100, 5)      # like range() but picks one value
 
data = [1, 2, 3, 4, 5, 6, 7, 8]
random.choice(data)              # pick one element
random.choices(data, k=3)        # pick 3 with replacement
random.sample(data, k=3)         # pick 3 without replacement
random.shuffle(data)             # shuffle in place — modifies original




from math import pi, sqrt, factorial # from mtlab kaha se import ke bad kya import karna hai vo liikhenge 
math.sqrt(16)  # Output: 4.0
math.pow(2, 3)  # Output: 8.0
math.log(math.e)        # 1.0 — natural log
math.log(1000, 10)      # 3.0 — log base 10
math.log2(8)            # 3.0 — log base 2
math.sin(math.pi / 2)   # 1.0
math.cos(0)             # 1.0
math.factorial(6)        # 720
math.gcd(48, 18)         # 6 — greatest common divisor
math.floor(3.9)          # 3 — round down
math.ceil(3.1)           # 4 — round up
math.inf                 # infinity — useful for initializing minimum values
math.isnan(float('nan')) # True — check for not-a-number
