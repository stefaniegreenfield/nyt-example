def get_all_dot_positions(xsize, ysize):
    return [(x,y) for x in range(1, xsize-1) for y in range(1, ysize-1)]

def create_grid_string(dots, xsize, ysize):
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            #print("in the inner loop") to see if we get this far and we do because this prints
            grid += "." if (x, y) in dots else "#"
            #print(grid) this prints also so we know the problem is after this
        grid += "\n" #was missing the + in front of the =
    #print(grid) to see if the for loop is returning anything but all it does is add more blank lines
    return grid

positions = get_all_dot_positions(5, 5)
print(create_grid_string(positions, 5, 5))
