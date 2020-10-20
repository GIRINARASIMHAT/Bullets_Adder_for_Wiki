#! python3


# Program to Add Bullets to the Text


import pyperclip                # importing the module pyperclip.

text = pyperclip.paste()        # The text is copied from the computer's clipBoard into the variable called 'text'.

lines = text.split('\n')        # Splitting the text into lines, when we find a newline delimitter[\n] and storing into a variable 'lines'.

for i in range(len(lines)):     # Adding Bullets[*] to all the lines by accessing the each line using a 'for' loop.
    lines[i] = '* ' + lines[i]  
    
text = '\n'.join(lines)         # Now the lines are stored back to 'text' variable with newline delimitter[\n].

pyperclip.copy(text)            # Finally pasting the text back to the Computer's clipboard.


print('Text is added with Bullets[*].')