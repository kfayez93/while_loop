'''

1. Print all the numbers between 1 : 200 (for loop / while loop)
2. Print "Python" if number is divisible by 3
3. Print "Verse" if number is divisible by 5
4. Print "PythonVerse" if number is divisible by both 3 and 5

'''

iterator = 1
while(iterator <= 200):
    if iterator % 3 == 0 and iterator % 5 == 0:
        print("PythonVerse")
    elif iterator % 3 == 0:
        print("Python")
    elif iterator % 5 == 0:
        print("Verse")
    else:
        print(iterator)
    iterator = iterator + 1