p = 23 # A prime number p is taken
print("The value of p : ", p) 

g = 9 # A primitve root for p, g is taken 
print("The value of g : ", g) 

# Alice will choose the private key a  
a = 4 # a is the chosen private key  
print("The private key a for Alice : ", a)
x = g**a % p # gets the generated key 
  
# Bob will choose the private key b 
b = 3 # b is the chosen private key 
print("The private key b for Bob : ", b)
y = g**b % p # gets the generated key 

# generating the secret key after the exchange 
    # of keys 
ka = y**a % p # Secret key for Alice 
kb = x**b % p # Secret key for Bob 
  
print("Secret key for the Alice is : ", ka);
print("Secret Key for the Bob is : ", kb)