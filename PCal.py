def add(A, B):    
  
   return A + B  
def subtract(A, B):   
  
   return A - B   
def multiply(A, B):   
  
   return A * B  
def divide(A, B):   
    
   return A / B
ch = True 
cc = "yes"  
while(ch):  
    print ("Please select the operation.")    

    print ("click 1  for  Addition")       

    print ("click 2   for  Subtraction")  

    print ("click 3  for Multiplication")  

    print ("click 4  for  Divide")    
    
    choice = input("Please enter choice (1 / 2/ 3/ 4): ")    
    
    num_1 = int (input ("Enter the first number: "))    
    num_2 = int (input ("Enter the second number: "))    

    if choice == '1':    
        print (num_1, " + ", num_2, " = ", add(num_1, num_2))    
    
    elif choice == '2':    
        print (num_1, " - ", num_2, " = ", subtract(num_1, num_2))    
    
    elif choice == '3':    
        print (num_1, " * ", num_2, " = ", multiply(num_1, num_2))    
    elif choice == '4':    
        print (num_1, " / ", num_2, " = ", divide(num_1, num_2))    
    else:    
        print ("This is an invalid input") 

    cc = input("Do you want to Calculate again : yes or no : ")    
    if(cc == "yes"):
        ch = True
    elif(cc == "no"):
        ch = False
    else:
        print("You Enter Wrong choice! ")    
