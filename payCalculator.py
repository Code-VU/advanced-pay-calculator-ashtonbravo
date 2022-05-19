#def calculatePay():
    
    # This first line is provided for you

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
hrs= float(hours)
rte = float(rate)
normalPay= float(hrs * rate)
#print (fh, fr)
if hrs > 40: 
    #print("Overtime")
    overtimePay = (hrs-40) * (rate*0.5)
    totalPay= normalPay + overtimePay
    print(totalPay)
else:
    print (normalPay)
       # otp = (fh - 40.0) * (fr * 0.5)
        #print (reg,otp)
       # xp = reg + otp
    #else:
        #print("regular")
        #xp = fh * fr
  #  print("Pay:", xp)

    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()