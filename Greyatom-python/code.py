# --------------
# Code starts here

# Create the lists 
class_1 = ['Geoffery Hinton', 'Andrew Ng', 'Sebastin Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason' , 'Carla Gentry', 'Corinna Cortes']
# Concatenate both the strings
new_class = class_1 + class_2
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
# Append the list
new_class.append('Peter Warden')
print(new_class)
# Print updated list


# Remove the element from the list

# Print the list



# Create the Dictionary
courses = {'Math': 65 , 'English': 70 , 'History': 80 , 'French': 70 ,'Science': 60}
print(courses)


# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`
total = sum(courses.values())
# Print the total
print(total)
# Insert percentage formula
percentage = (total*100/500)


# Print the percentage
print(percentage)



# Create the Dictionary
mathematics = {'Geoffery Hinton': 78, 'Andrew Ng':95, 'Sebastin Raschka':65,'Yoshua Bengio':50,'Hilary Mason':70 , 'Corinna Cortes': 66, 'Peter Warden':75}
print(mathematics)
topper = max(mathematics,key = mathematics.get)
print(topper)

# Given string
topper = "Andrew Ng"
topper.split()

# Create variable first_name 
first_name = topper.split()[0]
print(first_name)
# Create variable Last_name and store last two element in the list
last_name = topper.split()[1]
print(last_name)
# Concatenate the string
full_name = last_name + ' ' + first_name
# print the full_name
print(full_name)
# print the name in upper case
certificate_name = full_name.upper()
print(certificate_name)
# Code ends here


