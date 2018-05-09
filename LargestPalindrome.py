def getLargestPalindrome(string):
    stringLooper = 0                                            #used to loop through the string
    loopCount = 0                                               #used as the outer loop counter
    palindrome = ""                                             #will add letters to itself to be used to reprensent the palindrome
    largest = "__"                                              #used to compare size of palindromes
        
    while(loopCount < len(string)-2):                           #going up to length of the string minus two because no palindrome is less than 3
        
        while( stringLooper < len(string) ):                    #loop through whole string 
            palindrome += string[stringLooper]                  #add the next letter to the palindrome 
            
            if isPalindrome(palindrome):                        #check if the word is a palindrome
                if len(palindrome) > len(largest):              #if it is a palindrome, check if it's the largest found thusfar
                    largest = palindrome
            stringLooper += 1                                   #increment the string loop var
            
        palindrome = ""                                         #reset the palindrome  
        loopCount += 1                                          #increase loop count
        stringLooper = loopCount                                #make sure the starting letter is not the same 
        
    if len(largest) > 2:
        return largest
    return "NO PALINDROMES"                                     #if there was a palindrome found, return it
    
def isPalindrome(string):    
    
    mid = string[len(string)//2]                               #middle of string
        
    firstPart = ""                                             #first half of palindrome
    secondPart = ""                                            #second half of palindrome
    
    firstEnd = len(string)//2                                   #stopping point for first half of palindrome
    secondEnd = len(string)//2 - abs(len(string)%2 - 1)         #stopping point for second half of palindrome
        
    i = 0                                                       #loop variable
        
    while(i < firstEnd):                                        #concatenate the first half of the palindrome
        firstPart += string[i]
        i += 1
        
    i = len(string) - 1                                        #set counter to length - 1
    while(i > secondEnd):                                      #concatenate the second half of the palindrome
        secondPart += string[i]
        i -= 1
            
    return firstPart == secondPart                             #return true if the second half equals the first half 
    
def main():
    string = input("Enter a String : ")
    print(getLargestPalindrome(string))
        
if __name__ == "__main__":
    main()
    
    
    
    
        
        
                