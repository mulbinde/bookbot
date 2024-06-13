def main():
    bpath = "books/frankenstein.txt"
    text = gettext(bpath)
    numw = cwords(text)
    print(f"{numw} words found in the document")


def cwords(text):
    words = text.split()
    return len(words)


def gettext(path):
    with open(path) as f:
        return f.read()


main()