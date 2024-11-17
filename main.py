#read_file
def read_file(inputfile):
    try:
        inputText=""
        with open(inputfile,"r", encoding='utf-8') as file:
            for line in file:
                inputText+=line
            return inputText
    except FileExistsError:
        print(f"Error: {inputfile} finns inte!")
        return ""
    
#word_list_count
def word_list_count(inputText):
    wordList = []
    words = inputText.strip().split(" ")
    #print(words)
    for word in words:
        #print(word)
        if len(wordList) == 0:
            wordCount = words.count(word)
            wordList.append(
                {"Word":word,"Antal":wordCount}
            )
        else:
            if not any(entry['Word'] == word for entry in wordList):
                wordCount = words.count(word)
                wordList.append(
                    {"Word":word,"Antal":wordCount}
                )
    #print(wordList)
    return wordList

#save_the_results
def save_the_results(wordList,outputFile):
    with open(outputFile,"w", encoding='utf-8') as file:
        index = 0
        file.write('Första femton raderna ur result.txt:\n')
        for wordObj in wordList:
            if index == 15:
                break
            file.write(f"{wordObj['Word']} - {wordObj['Antal']}\n")
            index += 1
def save_the_most_frequent(wordList,inputFile):
    wordlist_sort = sorted(wordList, key= lambda x:x['Antal'], reverse=True)
    with open("most_frequent.txt","a", encoding='utf-8') as file:
        file.write('Följande rad bör vara sista raden i most_frequent.txt:\n')
        file_name = inputFile.split('/')[-1]
        file.write(f"{file_name}: {wordlist_sort[0]['Word']} - {wordlist_sort[0]['Antal']}\n")
#main 
def main():
    isRunning = True
    while isRunning:
        try:
            inputFile = input("Mata in vilken fil du vill läsa:")
            outputFile = input("Mata in vilken fil du vill spara till:")
            inputText = read_file(inputFile)    
            wordList = word_list_count(inputText)
            save_the_results(wordList,outputFile)
            save_the_most_frequent(wordList,inputFile)
            
        except Exception:
            print("Error")
            isRunning = False
main()
