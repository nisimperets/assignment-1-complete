#---
def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    counter=0;
    for i in range(0, len(word)-1):
        #print(word[i])
        if  word[i]==word[i+1]:
            counter=counter+1;
            #print(counter)

    if counter == 3:
        return True
    else: return False


print(trifeca("AABCCC"))

print(trifeca("AABDCC"))

#-------------------------------------------------------------------------------------------------------------------



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

#------------------------------------------------------------------------------------------------------------

def compare_subjects_within_student(History,Math):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """

    if(len(History)>=len(Math)):
        ShorterArr=Math
    else:
        shorterArr = History
    for key, value in shorterArr.items(): #key = name, val = grade Arrey
        max_history=max(History[key][0],History[key][1])
        max_math=max(Math[key][0],Math[key][1])

        if(max_history>max_math):
            print(key +" HISTORY")

        if(max_history<max_math):
            print(key + " MATH")

        if (max_history==max_math):
            print(key + " MATH" +" History")





history_Grades={'jack': [90,92], 'tom': [39,77], 'liz': [70,90], 'jil': [39,77]}

math_Grades={'jack': [88,95], 'tom': [46,76], 'liz': [55,76], 'jil': [81,87],'ryan': [81,87]}
compare_subjects_within_student(history_Grades, math_Grades)