
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