def markIsland(array, row, col, mark):
    
    if isInBounds(array,row,col) :              #checking if the position can be checked 
        if array[row][col] != 1:                #base case, there are no more connecting one's in the path
            return 
        
        array[row][col] = mark                  #one has been found, mark it as visited
        markIsland(array, row + 1, col, mark)   #visit the position below
        markIsland(array, row - 1, col, mark)   #visit the position above
        markIsland(array, row, col + 1, mark)   #visit the position right
        markIsland(array, row, col - 1, mark)   #visit the position left


def isInBounds(array, row, col):
    return ( (row > -1 and row < len(array)) and (col > -1 and col < len(array[row])) ) #checks if the position is in the array

def countIslandOnes(array):
    mark = 2                    #starting mark
    numIslands = 0              #keeps track of the number of islands
    
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == 1:                    #loop through array until a 1 is found
                markIsland(array, row, col, mark)       #mark up the 1 and its connecting ones (mark the island)
                mark += 1                               #increment mark in case the sizes of the island want to be calculated later
                numIslands += 1                         #an island has been found and marked, increment the island counter
                        
    print("{}{}{} ".format("There are ",numIslands, " \"1\" islands in the array")) #print the number of islands found

            
        

        
        
        
        
        
