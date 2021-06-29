list_Of_Numbers=[] 
num=None 
print("Enter Integer Number or enter 'done' to stop the program") 
while True: 
    print("Enter Integer Number") 
    num=input() 
    if(num=="done"): 
        break 
    try: 
        num=int(num) 
        list_Of_Numbers.append(num) 
    except: 
        print("Invalid Integer") 
         
#print(list_Of_Numbers) 
print("Largest number is ",max(list_Of_Numbers)) 
print("Smalles number is ",min(list_Of_Numbers))