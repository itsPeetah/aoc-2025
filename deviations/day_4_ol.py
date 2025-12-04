
# Explained for readability
accessible_rolls = [
    sum([
        1 # roll is accessible
        if (rolls[columns * y + x] if (x >= 0 and x < columns) and (y >= 0 and y < len(rolls) // columns) else 0) > 0 # if the item is a roll (@)
        and sum([(rolls[columns * (y+j) + (x+i)] if ((x+i) >= 0 and (x+i) < columns) and ((y+j) >= 0 and (y+j) < len(rolls) // columns) else 0) for i, j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]) < 4 # if the roll has less than 4 neighbours
        else 0 # roll is not accessible
        for y, x in [ (y, x) for x in [x for x in range(columns )] for y in range(len(rolls) // columns)] # loop over the entire array using cols and rows instead of index
    ]) # sum result (i.e. the accessible rolls)
        for rolls, columns # use a generator to make the parsing result available to the sum without having to parse the input every time they're needed
        in [([0 if c == "." else 1 for c in open("input/day4.txt").read().strip() if c != "\n"], open("input/day4.txt").read().find("\n"))] # parsing (array of rolls and row length)
    ][0] # access only result and no parsing result


o=[sum([1 if(r[c*y+x]if(x>=0 and x < c)and(y>=0 and y<len(r)//c)else 0)>0 and sum([(r[c*(y+j)+(x+i)]if((x+i)>=0 and(x+i)<c)and((y+j)>=0 and(y+j)<len(r)//c)else 0)for i,j in[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]])<4 else 0 for y,x in[(y,x)for x in[x for x in range(c)]for y in range(len(r)//c)]])for r,c in[([0 if c=="."else 1 for c in open("input/day4.txt").read().strip()if c!="\n"],open("input/day4.txt").read().find("\n"))]][0]

print("Expected result:", 1480, "\nResult:", o)