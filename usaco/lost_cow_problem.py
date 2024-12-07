"""

I did need to use AI to understand this, pretty embarassing for a bronze problem but hey I never said
i'm good at coding

"""


def lost_cow(x, y):
    total_distance = 0
    current_position = x
    step = 1

    while True:
        next_position = x + step
        if (current_position < y <= next_position) or (current_position > y >= next_position):
            # If Bessie is between the current position and the next position
            total_distance += abs(y - current_position)
            break
        else:
            # Add the distance to the next position
            total_distance += abs(next_position - current_position)

        # Update current position and step for the next iteration
        current_position = next_position
        step *= -2  # Reverse direction and double the step size

    return total_distance

with open('lostcow.in', 'r') as file:
    parts = file.read().strip().split(' ')
    global x
    global y
    x = int(parts[0])
    y = int(parts[1])

with open('lostcow.out', 'w') as file:
    file.write(str(lost_cow(x, y)))
