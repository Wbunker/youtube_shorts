import random
import time

regular_snowflake = '\u2744'
tight_snowflake = '\u2745'
heavy_snowflake = '\u2746'

historical_output = []
padding = -1
UP = '\033[F'

weather = [' ', regular_snowflake, tight_snowflake, heavy_snowflake]

while True:
    next_line = random.choices(weather, weights=[0.96, 0.025, 0.01, 0.005], k=120)

    historical_output.insert(0, ''.join(next_line))
    if len(historical_output) > 20:
        historical_output.pop()

    print(UP * 20)
    print(*historical_output)
    time.sleep(0.1)