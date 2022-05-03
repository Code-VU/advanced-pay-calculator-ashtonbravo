def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    float = float(hrs)
    rate = input("Enter Rate:")
    float = float(rate)
  
    #print (hrs,rate)
    if h <= 40 :
        pay = h * rate
    elif h > 40 :
        pay = 40*rate + (h-40)*rate*1.5
    print ("Pay:", pay)



    

    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculatePay()