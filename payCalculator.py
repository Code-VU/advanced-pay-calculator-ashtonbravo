def calculatePay():
    
    # This first line is provided for you
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
  
    #print (hrs,rate)
    if hrs > 40 :
        print("Overtime")
        Overtime = (hrs - 40.0) * (hrs * 0.5)
        #print(reg,otp)
        Pay = reg + otp
    else:
        #print("Regular")
        Pay = hrs * rate
    print("Pay:", Pay)
    

    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()