def get_all_dot_positions(xsize, ysize):
    return [(x,y) for x in range(1, xsize-1) for y in range(1, ysize-1)]
#before it was range(0 and xsize 0) and same for y so we changed it to 1

def create_grid_string(dots, xsize, ysize):
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            if (x, y) in dots:
                grid += "."
            else:
                grid +="#"
        grid += "\n"
    return grid

positions = get_all_dot_positions(5, 5)
print(create_grid_string(positions, 5, 5))

#the program is lines of dots- not our expected output
