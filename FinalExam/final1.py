def replacement(text):
    result = ""
 
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + 1-65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + 1 - 97) % 26 + 97)
        else:
            result += char
    return result

text = input("Enter a string:")

print (replacement(text))