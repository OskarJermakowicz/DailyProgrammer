sentence = "I heard the pastor sing live verses easily. Deep episodes of Deep Space Nine came on the television only after the news. Digital alarm clocks scare area children."

def match(word1, word2):
    for i, l in enumerate(range(word2.__len__())):
        if word2[:word2.__len__() - i] in word1 and word1.endswith(word2[:word2.__len__() - i]):
            return word2[word2.__len__() - i:]
    return ""

def condense(s):
    res = ""
    words = s.split(' ')
    while words:
        if words.__len__() > 1:
            if match(words[0], words[1]):
                res += words[0] + match(words[0], words[1]) + " "
                words.pop(1)
            else:
                res += words[0] + " "
        else:
            res += words[0]
        words.pop(0)
    return res

res = condense(sentence)
while condense(res) != res:
    res = condense(res)

print(res)


