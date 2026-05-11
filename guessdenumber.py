import time

print("===================================")
print("   Welcome to Number Prediction")
print("===================================\n")
time.sleep(2)

print("Step 1: choose any number between 1 to 10")
time.sleep(2)

print("Step 2: Multiply with 5")
time.sleep(2)

print("Step 3: Do addition with 5")
time.sleep(2)

print("Step 4: Multiply with 2")
time.sleep(2)

print("Step 5: Do addition with 2")
time.sleep(2)

print("Step 6: Share your end results -final total")
time.sleep(2)

finalvalue = input("Enter final value : " )
# Validation: Only integers allowed

if finalvalue.isdigit():
#validation check1
    if len(str(finalvalue)) <= 2:
    #pick first digit
       total_digit = int(str(finalvalue)[0])
       selectednumber = total_digit - 1
       print("Selected number between 1 to 10 is ", selectednumber)
    else:
       print("Choosen number not falls between 1 to 10. Please try again")
else:
   print("Please enter only integer values ")
    
