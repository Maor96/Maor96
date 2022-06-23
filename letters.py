# Frequency of letters - get string and retrurn how many each letter appears.

count1 = {}

str1 = input("Please write a word: ")

for i in str1:
    if i in count1:
        count1[i] += 1
    else:
        count1[i] = 1

print("There are str,", str(count1), " letters in your word.")