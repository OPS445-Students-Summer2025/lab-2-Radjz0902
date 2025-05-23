#!/usr/bin/env python3

import sys

# Check if exactly 2 arguments are provided (excluding script name)
if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "name age")
    sys.exit(0)  # <-- Exit gracefully with 0 (not 1)

name = sys.argv[1]
age = sys.argv[2]


print("Hi " + name + ", you are " + age + " years old.")
