from hashlib import sha256

file_name_1 = input("Enter the first file name")
file_name_2 = input("Enter the second file name")

with open(file_name_1, "rb") as file:
    c1 = file.read()
with open(file_name_2, "rb") as file:
    c2 = file.read()

assert sha256(c1).hexdigest() == sha256(c2).hexdigest()

