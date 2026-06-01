# Securing Data

### objectives

- discussing the storage of passwords to authenticate yourself.
- e.g. stroage of key pairs of `users:passwords.`
- hasing - technique for converting passwords into hash values.
- breakdown of how hashing operates:

Input -> | hash function | -> output
x -> | f | -> f(x)
password | x | -> hash

*Dictionary Attacks:*

- more work but understanding the computational overhead for finding the key pair of hash values to the passwords = more time-consuming.

*Brute-Force Attacks:*

*Rainbow Tables:*

- a library of hashtables dependent the amount of hash values = expensive, high hard drive use

- users with the same passwords, both hashes will display the same hash values.
- To prevent this, `salting` is done
- `salting` - modifying the hashing to increase the amount of input to create ambiguity within the hashing so not everyone with the same password becomes the same hash values.
  - if the same salt variables are used when hashing with the same password, you increase the vulnerability in determining the password and assocation with the hash values.

- modern hashes contain more bits, making it less possible for determining the passwords.

- `forgot password` - when the email provides a copy of your password, the link or website SHOULD NOT be used again.
    - why? 
    - because it doesn't follow good practices.
    - making it more vulnerable for hacking.



