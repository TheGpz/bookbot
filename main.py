#Ouvre le doc
filepath = "books/frankenstein.txt"
with open(filepath) as f:
    file_contents = f.read()

#Compte les mots
def count_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    print(f"{word_count} words found in the document")
    return word_count

#Compte les caractères (dont symboles et espaces)
def count_characters(file_contents):
    character_count = {}
    lowered_file_contents = file_contents.lower()
    for character in lowered_file_contents:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count

#Classe la liste par occurences
def sort_on(dict):
    return dict["num"]

#Classification des caractères alphabétiques
def classify_characters(character_count):
    character_list = []
    for character, count in character_count.items():
        character_dict = {"char": character, "num": count}
        if character.isalpha() == True:
            character_list.append(character_dict)
    character_list.sort(reverse=True, key=sort_on)
    return character_list

def generate_report(file_contents):
    print(f"--- Begin report of {filepath} ---")
    word_count = count_words(file_contents)
    character_count = count_characters(file_contents)
    sorted_chars = classify_characters(character_count)

    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")


#MAIN EXECUTION
generate_report(file_contents)