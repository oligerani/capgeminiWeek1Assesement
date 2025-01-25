def word_counter(statement):
   
    words = statement.split()
    word_count = {}
    for word in words:
        word = word.lower()  
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count


statement = input("Enter a sentence: ")
result = word_counter(statement)
for word, count in result.items():
    print(f"'{word}': {count}")

