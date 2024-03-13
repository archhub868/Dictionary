# Create an empty dictionary to store person information
person_info = {}

# Get user input for name
name = input("Type Your name: ")
person_info["name"] = name

# Get user input for age (convert to integer)
while True:
  try:
    age = int(input("Enter Your age: "))
    person_info["age"] = age
    break
  except ValueError:
    print("Invalid input. Please enter an integer for age.")

# Get user input for favorite color
favorite_color = input("Enter Your favorite color: ")
person_info["favcolor"] = favorite_color

# Print the person's information dictionary
print("Your information is as follows:")
print(person_info)
