import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*']
print("Password generator application")
s=int(input("No.of letters you want:"))
p=int(input("No of numbers you want:"))
q=int(input("No of symbols you want:"))
password_list=[]
for i in range(1,s+1):
    char=random.choice(letters)
    password_list+=char
for j in range(1,p+1):
    char1=random.choice(numbers)
    password_list+=char1
for k in  range(1,q+1):
    char2=random.choice(symbols)
    password_list+=char2
print(password_list)
random.shuffle(password_list)
print(password_list)
password=" "
for i in password_list:
    password+=i
print(password)    
         
