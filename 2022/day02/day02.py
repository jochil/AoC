rock = "A"
paper = "B"
scissor = "C"
lost = "X" 
draw = "Y" 
win = "Z" 

point_table = {
    rock: 1,
    paper: 2,
    scissor: 3,
    lost: 0,
    draw: 3,
    win: 6,
}

total_points_p1 = 0
total_points_p2 = 0

diff_ascii = ord("X") - ord("A")

def determine_move(elve, result) -> str:
    if result is lost:
        if elve is rock:
            return scissor
        if elve is paper:
            return rock 
        if elve is scissor:
            return paper 

    if result is win:
        if elve is rock:
            return paper 
        if elve is paper:
            return scissor 
        if elve is scissor:
            return rock

    return elve

def fight(f_a, f_b) -> str:
    if f_a is rock and f_b is paper:
        return lost
    elif f_a is rock and f_b is scissor:
        return win 
    elif f_a is paper and f_b is rock:
        return win
    elif f_a is paper and f_b is scissor:
        return lost
    elif f_a is scissor and f_b is rock:
        return lost
    elif f_a is scissor and f_b is paper:
        return win 
        
    return draw

def strategy_part_1(line) -> int:
    elve, me = line.split()
    # convert X,Y,Z to A,B,C
    me = chr(ord(me) - diff_ascii)
    result = fight(me, elve)
    return point_table[me] + point_table[result]

def strategy_part_2(line) -> int:
    elve, result = line.split()
    me = determine_move(elve, result)
    result = fight(me, elve)
    return point_table[me] + point_table[result]

if __name__ == "__main__":
    with open("input", "r") as file:
        for line in file.readlines():
            total_points_p1 += strategy_part_1(line)
            total_points_p2 += strategy_part_2(line)


    print("Total Points Part 1:", total_points_p1)
    print("Total Points Part 2:", total_points_p2)

