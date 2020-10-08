Source : From Coursera

QNS:
  You need to read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
  
Constraints:
  Use Regular Expression for this program.
  
 Program:
 
import re # importing the regular expression function 

finput = input("Enter the File:") 
fread = open(finput,"r") # getting the files from the user and reading it by using keyword "r"
totalval = 0 # initally setting a value to 0 (total sum)

for line in fread: 
    numlist = re.findall("[0-9]+",line) # creating a variable called numlist and using the regular expression keyword ("[0-9]+",line) extract the number that 
                                            available in file 
    if len(numlist) > 0:
        for item in numlist:
            totalval = totalval + int(item) #sum the numbers are that present in numlist
print(totalval)
