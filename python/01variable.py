fName = 'Arafat'; #camel case variable name
l_name = "Hossain"; #snake case variabel name
FullName = "Madhobi Lota"; #pascal case variable name  

# many value to multiple variables | Make sure the number of variables matches the number of values, or else will get an error.
fruit1 , fruit2 , fruit3 = 'Banana' , 'orange' , 'Mango';
print(fruit1);
print(fruit2);
print(fruit3);

#one value to multiple variables
car1 = car2 = car3 = 'premio';
print(car2)
print(car3)

mobile = 'Samsung'; # global variable

def func():
    price = 20000; # local variable
    global phone
    phone = "iPhone"; # global variable
    print(f"phonde name {mobile} and price: {price}");
func();

print(phone);