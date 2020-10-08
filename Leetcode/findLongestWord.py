def findLongestWord(sentence):
    words = sentence.split(" ")
    max = 0
    for word in words:
        length = len(word)
        if (length > max):
            max = length
    print(max)

sentence1 = "The quick red fox jumped over the lazy brown dog."
findLongestWord(sentence1)