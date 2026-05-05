import os

file_write = open("movies.txt", "a")
contenct_add = file_write.write("Inception")
file_write.close()


file = open("movies.txt", "r")
content = file.read()
file.close()
print(content)



import json

read_json = open("mo.json", "r")
content_j = json.load(read_json)
print(content_j)
read_json.close()