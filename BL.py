#! python3

# Program to Add Bullets to the Text

import pyperclip               
text = pyperclip.paste()      
lines = text.split('\n')  
for i in range(len(lines)):    
    lines[i] = '* ' + lines[i]  
text = '\n'.join(lines)      
pyperclip.copy(text)           
print('Text is added with Bullets[*].')
