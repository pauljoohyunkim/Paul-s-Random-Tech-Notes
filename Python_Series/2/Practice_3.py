#Copy the string into the code.
numstring = '44,24,-5,12,262,603029,-10,20390,591029,-20201,402,1930,291039,59102,3910,2,-102,-0.39,-1'
#Split them by ','
numstring = numstring.split(',')

#Using the hint
for i in range(len(numlist)):
  numlist[i] = float(numlist[i])

#Printing the average
print(sum(numlist) / len(numlist))
