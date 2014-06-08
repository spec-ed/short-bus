"""
Solution to problem presented at bottom.
Python3.3
"""

userInput = 0

while True:
    try:
        userInput = float(input("Enter hours worked: \n"))
    except ValueError:
        print ("That's not a number!!")
    else:        
        print ("Thank you, %s hours is a lot." % userInput)
        break
    finally:
        if userInput > 40:
            print ("You will be credited %s hours!" % (userInput + ((userInput - 40) * 1.5)))


"""
while True:
    try:
        h = (int)
        r = (int)
        if h > 40:
            r = 1.5
            print ('Pay' + h*r)
       

    except:
        print 'Enter number'
"""
