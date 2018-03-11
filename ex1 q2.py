
def check_palindrome():
    """
    Runs through all 6-digit numbers and checks the mentioned conditions.
    The function prints out the numbers that satisfy this condition.

    Note: It should print out the first number (with a palindrome in its last 4 digits),
    not all 4 "versions" of it.
    """

    #number_to_check=counter;
    for i in range(100000, 1000000):
        #print(str(i)[2:6])
        if(check_string_palindrome(str(i)[2:6])==True ):#convert int to sting// the last 4 digits are palindrom
            #print(str(i)[2:6])
            temp = i + 1 #first addition of one -> palindrom in last 5 digits
            if(check_string_palindrome(str(temp)[1:6])==True):
                #print(str(i)[1:6])
                temp = i + 2  # second addition of one -> palindrom in middle 4 digits
                if (check_string_palindrome(str(temp)[1:5]) == True):
                    #print(str(i)[1:5])
                    temp = i + 3  # third addition of one all digits palindrom
                    if (check_string_palindrome(str(temp)[0:6]) == True):
                        print(i)


def check_string_palindrome(String_Check_poly): #internal function to chack if palindrom
    for i in range(len(String_Check_poly)//2):
          if String_Check_poly[i] != String_Check_poly[-1-i]:
                  return False
    #print(String_Check_poly)
    return True





check_palindrome()

