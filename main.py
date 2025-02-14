# TASK: Write a function that validates an email format.

# Define a function that takes a string parameter
def get_email(email):
    while True:
        # Check if '@' is in the email
        # Check if it ends with '.com' or '.net'
        if "@" in email and (email[-4:]==".com"or email[-4:]==".net"):# Extract the last four characters of the email
            return True
        else:
            return False
# Return True if valid, False otherwise
valid=get_email(input('please enter email: '))
# Prompt the user for an email input and call the function
# Display whether the email is valid
if valid==True:
    print("your email is valid")
else:
    print("your email is not valid")