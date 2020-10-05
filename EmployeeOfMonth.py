From Udemy Course


Qns:
  Checking for the working hours and finding the highest number of working and printing them.
 
Program:

def employee_check(work_hours):   #Creating a function called employee_check
  current_hours = 0               # initally setting to 0 and each when max value comes it can be stored in this variable
  employee_of_month =''
  for k,v in (work_hours):        # using for loop to iterate though the list
    print(f"Employee Name: {k}  ||" +" "+  f'Working Hours {v}')
    print("\n")
    if v > current_hours:         # condition checking 
      current_hours = v
      employee_of_month = k
    else:
      pass
  print(f"Congrats {employee_of_month}")
  print(f'Employee of Month: {employee_of_month}'+ "\n "+f'Hours worked: {current_hours}')    # printing the values
    

work_hours = [("Allen",100),("Billy",800),("John",200)].   # input
employee_check(work_hours)                                 # calling the function 
