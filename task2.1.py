#User Input Data Processor
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
count_last =len(last_name)
count_first = len(first_name)
if count_first  > 2:
    print(first_name)
if count_last > 2:
    print(last_name)
else:
    print (f"First and last name must have more than 2 charachters")

        
    
