# main.py

from .message_formatter import rectangle_message

# --- Main Program ---

# Take input from the user
user_message = input("Enter your message: ")

# Call the rectangle_message function to decorate it
decorated = rectangle_message(user_message)

# Print the final decorated message
print(decorated)
