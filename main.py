
with open("text.txt",'r',encoding='utf8') as txt:
    data = txt.read()
word1 = input("Введіть 1 слово: ")
word2 = input("Введіть 2 слово: ")
k = False
if word1 in data:
    k = True
    data = data.replace(word1, word2)
if k == False:
    print("Something went wrong, file hasn`t these words")
with open("text.txt",'w',encoding='utf8') as result:
    result.write(data)
