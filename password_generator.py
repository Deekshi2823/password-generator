import random
letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="1234567890"
symbols="!@#$%^&*+"
n_let=int(input("How many letters would you like in your password"))
n_num=int(input("How many numbers would you like in your password"))
n_sym=int(input("How many symbols would you like in your password"))
password=" "
for i in range(1,n_let+1):
  let=random.choice(letters)
  password+=let
for i in range(1,n_num+1):
  num=random.choice(numbers)
  password+=num
for i in range(1,n_sym+1):
  sym=random.choice(symbols)
  password+=sym
print(password)
