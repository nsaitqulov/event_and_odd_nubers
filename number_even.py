#A four-digit integer is given. Find the number of even digits in it.
var_int=3452
#Create a variable "var_int" and assign it a four-digit integer value.
a1=3452%10
var_int+=1
var_int//10

a2=var_int%10
var_int+=1
var_int//10

a3=var_int%10
var_int+=1
var_int//10

a4=var_int%10
var_int+=1
var_int//10
#Print the number of even digits in the variable "var_int".
print(a1%2+a2%2+a3%2+a4%2)