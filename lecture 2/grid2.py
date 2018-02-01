def get_all_dot_positions(xsize, ysize):
    return [(x,y) for x in range(1, xsize-1) for y in range(1, ysize-1)]

def create_grid_string(dots, xsize, ysize):
    for y in range(ysize):
        grid = ""
        for x in range(xsize):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
        #print (grid) to see that the program does print but only gives us the last line because the empty string is inside the for loop thus reassigning it with every run through until the last one. Have to put gride="" not in the for loop
    return grid

positions = get_all_dot_positions(5, 5)
print(create_grid_string(positions, 5, 5))
