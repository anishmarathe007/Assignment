from numberToWord import convert

try:
    print("Hello and Welcome. I am a Number to Word Converter.")


    ui = 'yes'

    while ui != 'no' :
            inputNum = input("Enter the Number which you want to convert to Words\n");
            if len(inputNum) > 21 :
                    print("Exceeded the limit for processing. Please Enter it again.")
            elif not inputNum.isalpha():
                ip = int(inputNum)
                if(ip<0) :
                    print("Entered number is negative. But I can still process that number\n")
                    ip = (-ip)
                    print('Minus ' + convert(ip))
                    print("Do you want to convert some more numbers? (Enter yes : to continue or no : to exit)")
                    ui = input()
                else:
                    print(convert(ip))
                    print("Do you want to convert some more numbers? (Enter yes : to continue or no : to exit)")
                    ui = input()
            else:
                print("You have entered a string! Which is not allowed!")
except Exception as e:
    print(e)
