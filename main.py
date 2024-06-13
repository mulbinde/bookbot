def main():
    with open("books/frankenstein.txt") as f:
        cont =f.read()
    l=[]
    l=cont.split()
    c=len(l)
    print(c)    

main()