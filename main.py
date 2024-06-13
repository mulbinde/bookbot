def main():
    bpath = "books/frankenstein.txt"
    text = gettext(bpath)
    numw = cwords(text)
    charc=cchar(text)
    abc="abcdefghijklmnopqrstuvwxyz"
    print(f"{numw} words found in the document")
    for i in abc:
        print(f"{charc[i]} times letter {i} in the document")


def cwords(text):
    words = text.split()
    return len(words)


def gettext(path):
    with open(path) as f:
        return f.read()

def lowerc(s):
    return s.lower()

def cchar(s):
    dict={}
    sl=lowerc(s)
    for i in sl:
        if not i in dict: dict[i]=1
        else: dict[i]+=1
    return dict

main()