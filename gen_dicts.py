words = open("words.txt", 'r').read().splitlines()

lim_num_words = 20000

wordsToNums = {}
numsToWords = {}
i = 0
for word in words:
    print(word, word.lower())
    word = word.lower()
    wordsToNums[word] = i
    numsToWords[i] = word
    i += 1
    if i > lim_num_words:
        break

out = open("dicts.js", 'w')

out.write("""
export default {{
    "wordsToNums": {0},
    "numsToWords": {1}
}}
""".format(wordsToNums, numsToWords))

out.close()