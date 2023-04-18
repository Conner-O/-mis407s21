
words_to_letters = {
    "alpha": "a", "bravo": "b", "charlie": "c", "delta": "d",
    "echo": "e", "foxtrot": "f", "golf": "g", "hotel": "h",
    "india": "i", "juliet": "j", "kilo": "k", "lima": "l",
    "mike": "m", "november": "n", "oscar": "o", "papa": "p",
    "quebec": "q", "romeo": "r", "sierra": "s", "tango": "t",
    "uniform": "u", "victor": "v", "whiskey": "w", "x-ray": "x",
    "yankee": "y", "zulu": "z"
}
sentence = input("Enter phonetic words separated by spaces:").lower()

phonetic = ""
hiddenMsg = ""

for letter in sentence:
    if letter != " ":
        phonetic += letter
    else:
        hiddenMsg += words_to_letters[phonetic]
        phonetic = ""
hiddenMsg += words_to_letters[phonetic]

print (hiddenMsg)

