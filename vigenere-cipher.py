# list of chars. in the English alphabet
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# function for catching errors
def catch_errors(text_input):
    if text_input.isnumeric() or text_input.islower() or not text_input.isalpha():
        print('Error: You need to put uppercase letters only! Try to run the program again.')
        quit()
# input variable for the message
# function init for message
# input variable for the key
# function init for key var.
# placeholder variables for the mod value and encrypted message
# while loop to correspond key chars. with message chars.
# remove extra chars. of key before adding the values of chars. of message var.
# for loop
# print result