import random
import enchant
import codecs
# from fold_to_ascii import fold

enDict = enchant.Dict("en_US")

wordsToBlankOut = []
blankedWords = []

def blankOutWord(word):
    # print(len(word))
    numCharToBlank = int(len(word) * .5)
    startOrEnd = random.randint(0, 1)
    # 0 = start, 1 = end
    # print(numCharToBlank)
    # print(startOrEnd)

    newWord = ""
    
    # print('\n')
    # if start then append numCharToBlank _'s then append word[numCharToBlank:]
    # else append word[0:len(word) - numCharToBlank] then numCharToBlank _'s
    if startOrEnd == 0:
        newWord += '*' * numCharToBlank
        newWord += word[numCharToBlank:]
    else:
        newWord += word[0:len(word) - numCharToBlank]
        newWord += '*' * numCharToBlank

    return str(newWord)

file = codecs.open('input.txt', 'r', 'UTF-8')
lines = file.readlines()
for line in lines:
    # # DEBUG: line
    #     print(line.strip())
    # # DEBUG: line

    # # DEBUG: words in line
    # words = line.split()
    # print(words)
    # # DEBUG: words in line

    # # DEBUG: alphabetic words in line
    # words = line.split()
    # words = [word for word in words if word.isalpha()]
    # print(words)
    # print(len(words))
    # # DEBUG: alphabetic words in line

    # # DEBUG: alphabetic words and words with length of at least 5 letters in line
    # words = line.split()
    # words = [word for word in words if word.isalpha() and len(word) >= 5]
    # print(words)
    # print(len(words))
    # # DEBUG: alphabetic words in line

    # DEBUG: blank out random percentage of words in line
    words = line.split()
    numWords = len(words)

    if numWords < 1:
        continue

    # # DEBUG: inner
    # print(line.strip('\n'))
    # # DEBUG: inner

    words = [word for word in words if word.isalpha() and len(word) >= 6 and enDict.check(word)]
    numWords = len(words)
    numWordsToBlankOut = int(numWords * .5)
    newWords = random.sample(words, numWordsToBlankOut)
    wordsToBlankOut += newWords
    # print(numWords)
    # print(numWordsToBlankOut)

    # # DEBUG: inner
    # print(wordsToBlankOut)
    # # DEBUG: inner

    # print('\n')
    # print(blankOutWord(words[0]))
    # print('\n')

    # # DEBUG: inner
    # for word in wordsToBlankOut:
    #     print(blankOutWord(word))
    # print('\n')
    # # DEBUG: inner

    for word in newWords:
        blankedWords.append(blankOutWord(word))

    # DEBUG: blank out random percentage of words in line
    
file.close()

with codecs.open('input.txt', mode='r', encoding='UTF-8') as file:
    data = file.read()

# print(data)
# print(wordsToBlankOut)
# print(blankedWords)
# print(len(wordsToBlankOut))
# print(len(blankedWords))

# print(data)

for index, oldWord in enumerate(wordsToBlankOut):
    newWord = blankedWords[index]
    data = data.replace(oldWord, newWord, 1)

# print(data)

output = codecs.open('output.txt', mode='w', encoding='UTF-8')
output.write(data)
output.close()