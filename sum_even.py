#A four-digit integer is given. Find the sum of even digits in it.
var_int=4589
#Create a variable "var_int" and assign it a four-digit integer value.
sum_even=0
#Create a variable "sum_even" and assign it 0.
a1=var_int%10
sum_even+=(a1+1)%2*a1
var_int//=10

a2=var_int%10
sum_even+=(a2+1)%2*a2
var_int//=10

a3=var_int%10
sum_even+=(a3+1)%2*a3
var_int//=10

a4=var_int%10
sum_even+=(a4+1)%2*a4
var_int//=10
#Find the sum of the even digits in the variable "var_int".
print(sum_even)