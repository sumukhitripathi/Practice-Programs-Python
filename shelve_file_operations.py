import shelve

# Open shelve file
db = shelve.open("mydata")

# Storing data
db["name"] = "Sumukhi"
db["age"] = 21
db["course"] = "CSE"

# Retrieving data
print("Name:", db["name"])
print("Age:", db["age"])
print("Course:", db["course"])

# Close file
db.close()

with shelve.open("mydata") as db:
    db["marks"] = 98   # update value
    print("Updated Marks:", db["marks"])