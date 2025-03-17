excluded_words = {"and", "but", "or", "nor", "for", "so", "yet", "a", "an", "the", "of"}

def count_unique_words(sentence):
    words = sentence.split()  
    word_count = {}

    for word in words:
        clean_word = word.strip(".,!?;:()")  
        if clean_word and clean_word.lower() not in excluded_words:
            word_count[clean_word] = word_count.get(clean_word, 0) + 1

    lowercase_words = sorted([w for w in word_count if w.islower()])
    uppercase_words = sorted([w for w in word_count if w.istitle()])

    total_words = sum(word_count.values())
    for word in lowercase_words + uppercase_words:
        print(f"{word.ljust(10)} - {word_count[word]}")
    
    print(f"Total words filtered: {total_words}")

sentence = input("Enter a string statement:\n")
count_unique_words(sentence)
