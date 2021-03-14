list = []

while True:
    num = input("Enter a number: ")
    if num == "done": 
        break
    else:
    	try:
			num = int(num)
			list.append(num)
    	except:
        	print("Invalid input")
            
largest = max(list)
smallest = min(list)
   
print("Maximum is", largest)
print("Minimum is", smallest)
