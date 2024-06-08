def bookintotext():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    print(bookintotext())
    countallwords()

def countallwords():
    booktext = bookintotext()
    words = booktext.split()
    print(len(words))

#def charactertally():
    

main()

