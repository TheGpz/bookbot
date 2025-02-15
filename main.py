#Ouvre le doc
with open("books/frankenstein.txt") as f:
    file_contents = f.read()

#Compte les mots
def count_words(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count
    print(f"\nCe texte contient {word_count} mots.")

#Compte les caractères (dont symboles et espaces)
def count_characters(file_contents):
    character_count = {}
    lowered_file_contents = file_contents.lower()
    for character in lowered_file_contents:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    print(character_count)
    return character_count

def sort_on(character_count):
    return character_count["Num"]


count_characters(file_contents)

    

