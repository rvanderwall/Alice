from Strings import pad_string, unpad_string


def conjugate(sentence: str):
    sentence = pad_string(sentence)

    # swap conjugations
    #  This is mine and that is yours -->
    #  This is yours and that is mine
    idx = 0
    for key in conjugations.keys():
        first_person = key
        second_person = conjugations[key]
        sentence = sentence.replace(f" {first_person} ", f" CON_first_{idx} ")
        sentence = sentence.replace(f" {second_person} ", f" CON_second_{idx} ")
        idx += 1

    idx = 0
    for key in conjugations.keys():
        first_person = key
        second_person = conjugations[key]
        sentence = sentence.replace(f"CON_first_{idx}", second_person)
        sentence = sentence.replace(f"CON_second_{idx}", first_person)
        idx += 1

    for key in conjugation_fixes.keys():
        incorrect = key
        corrected = conjugation_fixes[key]
        sentence = sentence.replace(f" {incorrect} ", f" {corrected} ")

    return unpad_string(sentence)


conjugations = {
    "I": "you",
    "am": "are",
    "was": "were",
    "my": "your",
    "mine": "yours",
    "I'm": "you're",
    "I've": "you've",
    "I'll": "you'll",
    "me": "you",
    "myself": "yourself",
}

# array to post process correct our tenses of pronouns such as "I/me"
conjugation_fixes = {
    "me am": "I am",
    "am me":  "am I",
    "me can": "I can",
    "can me":  "can I",
    "me have": "I have",
    "me will": "I will",
    "will me": "will I"
}
