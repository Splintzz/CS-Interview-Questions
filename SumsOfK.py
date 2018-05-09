def findSumsOf(array, k):
    loopVar = 0                                                 #used to loop through array
    cols = k//2 + 1                                             #number of columns = number of possibilities to add to k = k/2 + 1
    
    odd = k%2 == 1                                              #k is either even or odd
        
    midValue = k//2                                             #mid value is k/2
        
    gridMap = [[0 for x in range(cols)] for y in range(2)]      #will map the sums
    
#     [00][1][2][3][4][5]          [00][01][2][3][4][5]         <- example what the grid will look like
#     [10][9][8][7][6][5]          [11][10][9][8][7][6]         #This way makes it possible to do in linear time
    
    
    while(loopVar < len(array)):
        if array[loopVar] < midValue:                                                           # if number less than mid value
            gridMap[0][array[loopVar]] = array[loopVar]                                         #number goes in top section of map
            
        elif array[loopVar] > midValue and array[loopVar] <= k:                                 #if number is between 0 - k
            gridMap[1][k - array[loopVar]] = array[loopVar]                                     #number goes in bottom section
            print("{} {}".format(gridMap[0][k-array[loopVar]], gridMap[1][k - array[loopVar]])) #can now print sum pair
            
        elif array[loopVar] == midValue:                                                        #if number is the mid value
            if odd:
                gridMap[0][midValue] = midValue                                                 #if k is odd, the mid value does not add with itself to become k
                
            else:                                                                               #k is even
                if gridMap[0][midValue] == 0:                                                   #if the top half of the grid does not have a value already
                    gridMap[0][midValue] = midValue                                             #put the mid value there
                else:
                    gridMap[1][midValue] = midValue                                             #else, put the value on the bottom half
                    print("{} {}".format(gridMap[0][midValue], gridMap[1][midValue]))           #can now print sum pair
        loopVar+=1               
                    
              
array = [1,2,3,4,5,6,7,8,9,10,13,0]
findSumsOf(array, 13)

