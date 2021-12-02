with open('./data.txt') as f:
    data = f.read().splitlines()


depth = 0
position = 0
# Part 2
aim = 0

def control_sub(action_and_sum: list[str]):
    for action in action_and_sum:
        if 'up' in action:
            up(int(action[len(action) - 1]))
        elif 'down' in action:
            down(int(action[len(action) - 1]))
        elif 'forward' in action:
            forward(int(action[len(action) - 1]))


def forward(num: int):
    global position
    # part 2
    global depth
    global aim
    a = aim * num
    depth += a
    position += num
    return position


def up(num: int):
    global depth
    # part 2
    global aim
    aim -= num
    # Part 1
    # depth -= num
    return depth


def down(num:int):
    global depth
    # part 2
    global aim
    aim += num
    # Part 1
    # depth += num
    return depth


control_sub(data)
print(position * depth)