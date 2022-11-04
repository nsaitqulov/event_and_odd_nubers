#A four-digit integer is given. Find the number of odd digits in it.
var_int=5554

a=var_int%10
var_int//=10

b=var_int%10
var_int//=10

c=var_int%10
var_int//=10

d=var_int%10
var_int//=10
#Create a variable "var_int" and assign it a four-digit integer value.
#Print the number of odd digits in the variable "var_int".
print(a%2+b%2+c%2+d%2)