sentence = input("Enter line to count: ")

letter_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
total = 0

for ch in sentence.lower():
    if ch.isalpha():
        count = 0
        for i in alphabet:
            if ch == i:
                letter_counts[count]+=1
                count = 0
            else:
                count += 1  

for element in range(0, len(letter_counts)):
    total = total + letter_counts[element]

for i,n in zip(alphabet, letter_counts):
    print("Letter: ", i, "Count: ", n, "Frequency: " , n/total) 