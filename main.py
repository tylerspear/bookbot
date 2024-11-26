def count_words(text):
    word_count = len(text.split())
    return word_count

def count_chars(text):
    lower_text = text.lower()
    chars = {}
    for char in lower_text:
        if char in chars:
            chars[char] += 1
        elif char.isalpha():
            chars[char] = 1
    for char in chars:
        print(f"The '{char}' character was found {chars[char]} times")

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print(f"{count_words(file_contents)} words found in the document")
    print(count_chars(file_contents))
        

main()