def calculatePay():
    
    # This first line is provided for you
    


sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh= float(sh)
fr = float(sr)
#print (fh, fr)
if fh > 40: 
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    print (reg,otp)
    xp = reg + otp
else:
    print("regular")
    xp = fh * fr
print("Pay:", xp)


    

    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()