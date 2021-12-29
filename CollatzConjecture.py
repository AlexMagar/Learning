#defination
def collaz_sequence(num):
    """
    define variable with constant
    count to count the iteration
    total to store total sum of sequence
    average to store the value of sequence
    assign five = 5 to print five number in one row and so on
    """
    count = 0   
    total = 0
    five = 5
    average = 0
    while (num > 1):
        if (num % 2 == 0):      #enter the condition if number is even
            if(count == five):  #new line after evry five number
                five += 5
                print("\n")
            print(num, end=" ") #print the collatz sequence and add a space afer one number
            total += num        #get the total of sequence
            num = int(num / 2)  #implement collatz formula if nunmber is even
            count += 1          #increase count by 1

        elif (num % 2 != 0):    #enter the condition if number is odd
            if(count == five):
                five += 5
                print("\n")
            print(num, end=" ")
            total += num
            num = int((num * 3) + 1)    #apply collatz rule if number is odd
            count += 1
    print(num)                  #prtint last number of sequence which is "1"
    average = total / count     #calculate average of sequence
    print("\nIt took {} iteration to arrive at 1.".format(count))   #print how many times loop runs
    print('The average value is ', average) #print the average of sequence

#main function
if __name__=="__main__":

    num = int(input("Enter a positive number, or zero to quit: "))  #get positive number or zero  to exit
    while(True):   # True loop
        if(num == 0):   #check wheather number enter by user is zero or not
            print("\nHave a nice day!")
            break   #break from the while loop if number is zero
        collaz_sequence(num)    #pass the number to the function 
        num = int(input("\nEnter the next positive number, or zero to quit: ")) #ask again number to user


