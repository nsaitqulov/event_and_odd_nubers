#A four-digit integer is given. Find the number of odd digits in it.
var_int=4555
s=0

a=var_int%10
s+=a%2
var_int//=10

b=var_int%10
s+=b%2
var_int//=10

c=var_int%10
s+=c%2
var_int//=10

d=var_int%10
s+=d%2
var_int//=10
#Create a variable "var_int" and assign it a four-digit integer value.
#Print the number of odd digits in the variable "var_int".
print(s)