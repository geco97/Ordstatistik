#read_file
def read_file(inputfile):
    wordCount = {}
    with open(inputfile,"r", encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                wordCount[word] = wordCount.get(word,0) + 1
    return wordCount

#writeInOutputfile
def save_the_results(outputFile,wordlist):
    with open(outputFile,"w", encoding='utf-8') as file:
        sortedwordList = sorted(wordlist)
        for word in sortedwordList:
            file.write(f"{word} - {wordlist[word]}\n")

#readResultFile
def readResultFile(fileName):
    inputText=""
    with open(fileName,"r", encoding='utf-8') as file:
        lines = file.readlines()
        maxLines = lines[:15]
        for line in maxLines:
            inputText+=line
        print(inputText)

#findMostFrequentWord
def findMostFrequentWord(wordList,inputFile):
    max_count = max(wordList.values())
    mostFrequentWords = []
    for word, count in wordList.items():
        if count == max_count:
            mostFrequentWords.append(word)
    mostFrequentWord = min(mostFrequentWords)
    mostFrequentFile = 'most_frequent.txt'
    fileName = inputFile.split("/")
    with open(mostFrequentFile, 'a', encoding='utf-8') as file:
        fileName = fileName[-1]
        file.write(f'{fileName}: {mostFrequentWord} - {wordList[mostFrequentWord]}\n')

#readFile
def readFile(fileName):
    inputText=""
    with open(fileName,"r", encoding='utf-8') as file:
        for line in file:
            inputText+=line
        print(inputText)


def main ():
    inputFile = input("Mata in vilken fil du vill läsa:")
    outputFile = input("Mata in vilken fil du vill spara till:")
    wordList = read_file(inputFile)    
    save_the_results(outputFile,wordList)
    print(f'Första femton raderna ur {outputFile}:')
    readResultFile(outputFile)
    findMostFrequentWord(wordList,inputFile)
    print('Följande rad bör vara sista raden i most_frequent.txt:')
    readFile("most_frequent.txt")


main()