sentence = input("Enter a sentence: ")
for ch in sentence:
    if ch.isalpha():
        print("Letter: ", ch, ord(ch))
    elif ch.isdigit():
        print("Digit: ", ch)
    elif ch.isspace():
        print("Whitespace")
    else:
        print("Not a letter or digit:", ch)
        