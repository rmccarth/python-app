import sys

def stringify(item):
    return str(item)

def main():
    try:
        if sys.argv[1] != None:
            print(stringify(sys.argv[1]))
    except:
        exit()
main()
