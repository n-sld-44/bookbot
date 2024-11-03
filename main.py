def number_of_words(text : str) -> int:
    words = text.split()
    return len(words)

def number_of_characters(text : str) -> dict:
    characters = dict()
    loweredText = text.lower()
    for c in loweredText:
        characters[c] = characters.get(c, 0) + 1
    return characters

def dict_to_list_of_dict(dictionnary : dict) -> list:
    listOfDict = list()
    for k,v in dictionnary.items():
        if k.isalpha():
            listOfDict.append(dict([(k,v)]))
    return listOfDict

def sort_on(dictionary : dict) -> int:
    return list(dictionary.values())[0]
    


def main():
    print("--Begin report of books/frankenstein.txt--")
    with open("books/frankenstein.txt") as file:
        file_contents = file.read()
        numberOfWords = number_of_words(file_contents)
        print(f'{numberOfWords} where found in the document')
        characters = number_of_characters(file_contents)
        listOfDict = dict_to_list_of_dict(characters)
        listOfDict.sort(reverse=True, key = sort_on)
        for d in listOfDict:
            k,v = list(d.items())[0]
            
            print(f"The '{k}' character was found {v} times")

main()