file = open("myfile.txt","w")
file = open("myfile.txt","a")
file = open("myexample.txt","r")


age =21
x=4
y=3
result=x+y

file.write("My name is Rita\n")
file.write("I am "+ str(age) + " years\n") 
file.write("The sum of "+ str(x) + " and "+ str(y) + " is " + str(result) + " \n")
file.writelines(["Apple\n","Orange\n","Banana\n"])

file.close()