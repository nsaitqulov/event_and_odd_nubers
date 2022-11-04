#A four-digit integer is given. Find the sum of odd digits in it.
var_int=9222
sum_even=0
#Create a variable "var_int" and assign it a four-digit integer value.
a=var_int%10
sum_even+=a%2*a
var_int//=10

b=var_int%10
sum_even+=b%2*b
var_int//=10

c=var_int%10
sum_even+=c%2*c
var_int//=10

d=var_int%10
sum_even+=d%2*d
var_int//=10
#Create a variable "sum_even" and assign it 0.
#Find the sum of the odd digits in the variable "var_int".
print(sum_even)