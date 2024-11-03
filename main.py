def number_of_words(text : str) -> int:
    words = text.split()
    return len(words)

def number_of_characters(text : str) -> dict:
    characters = dict()
    loweredText = text.lower()
    for c in loweredText:
        characters[c] = characters.get(c, 0) + 1
    return characters

def main():
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        print(file_contents)
        numberOfWords = number_of_words(file_contents)
        print(f'{numberOfWords=}') 
        characters = number_of_characters(file_contents)
        print(f'{characters=}')
main()