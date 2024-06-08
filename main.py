bookpath = "books/frankenstein.txt"

def main():
    #print(bookintotext(bookpath))
    print(f"--- Begin report of {bookpath} ---")
    print("")
    print(f"There are {countallwords()} words")
    print("")
    report()
    print("--- End report ---")

def bookintotext(book):
    with open(book) as f:
        return f.read()    

def countallwords():
    booktext = bookintotext(bookpath)
    words = booktext.split()
    return len(words)
    

def charactertally():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    booktext = bookintotext(bookpath)
    lowertext = booktext.lower()
    tallycount = {}
    for alphabet in alphabet:
         tallycount[alphabet] = lowertext.count(alphabet)
    return tallycount


def report():
    tallycount = charactertally()
    sortedtally = dict(sorted(tallycount.items(), key=lambda item:item[1], reverse = True))
    sortedlist = list(sortedtally)
    for i in range(0,len(sortedlist)):
        print(f"The {sortedlist[i]} character was found {sortedtally[sortedlist[i]]} times")
    
    


        


main()

