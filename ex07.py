import sys
from string import punctuation
def main():
        if len(sys.argv) != 3:
            print("ERROR")
            return
        else:
            my_string = [c for c in sys.argv[1] if not c in punctuation]
            my_string = ''.join(my_string)
            res = my_string.split(' ')
            res = [c for c in res if not  len(c) <= int(sys.argv[2]) ]
            print(res)
main()
