def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input("Enter Rate:")
    fh = float(hrs)
    fr = float (rate)
    #print (fh,fr)
    if fh > 40 :
        #print("Overtime")
        otp = (fh - 40.0) * (fr * 0.5)
        #print(reg,otp)
        xp = reg + otp
    else:
        #print("Regular")
        xp = fh * fr
    print("Pay:", xp)
    

    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()