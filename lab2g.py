#!/usr/bin/env python3

# Author: Radjznairene Jallorina
# Author ID: 144342235
# Date Created: 2025/05/23

import sys

# If an argument is provided, use it; otherwise default to 3
if len(sys.argv) > 1:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")

