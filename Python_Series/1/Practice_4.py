#x^2+x-4=0 has two distinct solutions

#Coefficients
a = 1
b = 1
c = -4

#Quadratic Formula
x = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
y = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

#Prints out the solutions.
print('Two solutions are' + str(x) + ' and ' + str(y) + '.')
