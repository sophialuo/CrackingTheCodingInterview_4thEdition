#8.6
#Implement the "paint fill" function that one might see on many image editing programs.
#That is, given a screen (represented by a 2-D array of Colors), a point, and a new color,
#fill in the surrounding area until you hit a border of that color
#slight personal modification:
#input: grid with 1s that make a border, starting point that is a tuple
#ouput: grid filled with 2s that fills an enclosed area of 1s
def paint_fill(pic, start):
    #implement
    rows = len(pic)
    cols = len(pic[0])
    visited = [[False for c in range(cols)] for r in range(rows)] 
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        x = vertex[0]
        y = vertex[1]
        if not visited[x][y] and pic[x][y] != 1:
            visited[x][y] = True
            pic[x][y] = 2
            if x-1 > 0:
                queue.append((x-1,y))
            if x+1 < rows:
                queue.append((x+1,y))
            if y-1 > 0:
                queue.append((x,y-1))
            if y+1 < cols:
                queue.append((x,y+1))
    return pic
    
#test case
test_pic = [[0,0,0,0,0,0],
            [0,1,1,0,1,1],
            [1,0,0,1,0,1],
            [1,0,0,0,0,1],
            [1,1,0,0,1,0],
            [0,1,0,1,1,0],
            [0,1,0,0,1,0],
            [0,1,0,0,1,0]]    
test_start = (0,0)
paint_fill(test_pic, test_start)

