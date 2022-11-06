import random
import time
from collections import deque

weather = [' ', 
    '\u2744', 
    '\u2745', 
    '\u2746']

terminal_height = 10
empty = [ '' for _ in range(terminal_height)]
historical_output = deque(empty, 
        maxlen=terminal_height)
        
while True:
    next_line = random.choices(weather, 
        weights=[0.96, 0.025, 0.01, 0.005],
        k=120)

    historical_output.appendleft(''.join(next_line))
 
    for line in historical_output:
        print(line)

    time.sleep(0.2)