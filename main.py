def bookintotext():
    with open("books/frankenstein.txt") as f:
        return f.read()

def main():
    print(bookintotext())
    countallwords()
    #print(charactertally())
    print(report())

def countallwords():
    booktext = bookintotext()
    words = booktext.split()
    print(len(words))
    

def charactertally():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    booktext = bookintotext()
    lowertext = booktext.lower()
    tallycount = {}
    for alphabet in alphabet:
         tallycount[alphabet] = booktext.count(alphabet)
    return tallycount

def report():
    tallycount = charactertally()
    sortedtally = dict(sorted(tallycount.items(), key=lambda item:item[1], reverse = True))
    #This will sort the dictionary but I can't figure out how to call the keys and values by index.
        


main()

