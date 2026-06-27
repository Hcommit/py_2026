# Program to find the top 10 most frequent words in a book

file = open(r"C:\Users\Hardik Gupta\OneDrive\Desktop\book.txt", "r")
bookContent = file.read().lower()
file.close()

wordFrequency = {}

for word in bookContent.split():
    cleanWord = ''.join(char for char in word if char.isalnum())

    if cleanWord:
        if cleanWord in wordFrequency:
            wordFrequency[cleanWord] += 1
        else:
            wordFrequency[cleanWord] = 1

sortedWords = sorted(wordFrequency.items(),
                     key=lambda item: item[1],
                     reverse=True)

print("Top 10 words in the book:\n")

for word, frequency in sortedWords[:10]:
    print(word, ":", frequency)