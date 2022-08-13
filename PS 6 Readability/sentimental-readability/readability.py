from cs50 import get_string


def main():
    text = get_string("Text: ")

    L = ((avg_num_letters(text) * 100) / avg_num_words(text))
    S = ((avg_num_sentence(text) * 100) / avg_num_words(text))
    #print(f"L: {L}")
    #print(f"S: {S}")

    coleman_liau = 0.0588 * L - 0.296 * S - 15.8
    #print(f"Coleman-Liau Index: {coleman_liau}")

    if coleman_liau < 1:
        print("Before Grade 1")
    elif coleman_liau >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {round(coleman_liau)}")


def avg_num_letters(text):
    c = 0
    for letters in text:
        if letters.isalpha():
            c += 1
    return c


def avg_num_words(text):
    c = 0
    for items in text:
        if items == " ":
            c += 1
    return (c + 1)


def avg_num_sentence(text):
    c = 0
    for items in text:
        if items in [".", "!", "?"]:
            c += 1
    return c

if __name__ == "__main__":
    main()