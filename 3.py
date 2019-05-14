phrase = raw_input("Enter text to Cipher: ")
shift = int(raw_input("Please enter shift: "))
result = ("Encrypted text is: ")

for character in phrase: 
     #Loops through phrase and shows ascii numbers, example: hello is: 104,101,108,108,111
    x = ord(character)

     #adds a shift to each character so if shift is 1 'hello' becomes: ifmmp 105,102,109,109,112
    result += chr(x + shift)


print "\n",result,"\n"
