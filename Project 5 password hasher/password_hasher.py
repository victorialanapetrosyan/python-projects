# Password hashing: transforming users' password into a irreversible string of characters using a hashing algorithm
# It is impossible to  reverse the process and recover the original password from its hash. This prevents attackers from easily obtaining plaintext passwords even if they gain access to the stored hashes.
# Salting: To further enhance security, a unique random string (salt) is attached to each password before hashing
# we need to import the bcrypt module to encrypt passwords
import bcrypt
# the password needs to be converted to bytes in order to pass it in the hashpw method
password = b'password'

# the bcrypt library already provides a hashing function
# add salt to the password with gensalt() method
hash = bcrypt.hashpw(password, bcrypt.gensalt())
print(hash)

# accepting password from user
entered_password = input('Enter password to login: ')
# you need to hash the entered password, then compare it to the actual hashed password
# convert entered password to bytes to hash it
entered_password = bytes(entered_password,encoding='utf-8')
# in bcrypt, there is a method checkpw() which allows you to compare the hashed entered password with the hashed stored password
# bcrypt.checkpw(): extracts the salt from the stored hash, re-runs the hashing process with the same salt and cost, compares internally
if bcrypt.checkpw(entered_password,hash):
    print('login successful')
else:
    print('invalid password')




