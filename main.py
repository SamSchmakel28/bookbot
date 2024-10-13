def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_count(file_contents)
        chr_dict = count_characters(words)

        num_words = len(words)
        print_report(chr_dict, num_words)

def word_count(str):
    words = str.split()
    return(words)

def count_characters(text):
    chr_dict = {}
    for i in range(0,len(text)):
        for j in range(0, len(text[i])):
            letter = text[i][j].lower()

            # Check if key exists. If it does, add 1 to its value. Otherwise, create it.
            if letter in chr_dict:
                chr_dict[letter] = chr_dict[letter] + 1
            else:
                chr_dict[letter.lower()] = 1

    return(chr_dict)

def print_report(info_dict, int_words):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{int_words} words found in the document\n")

    info_list = list(info_dict.items())
    info_list = sorted(info_list, key=lambda tup: tup[1], reverse=True)

    for line in info_list:
        if line[0].isalpha():
            print(f"The '{line[0]}' character was found {line[1]} times")
    
    print("--- End report ---")

main()