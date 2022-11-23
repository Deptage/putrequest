#https://play.picoctf.org/practice/challenge/68?category=2&page=1
import string

alphabet=list(string.ascii_lowercase)

def print_letter(num):
    print(alphabet[num-1],end="")

if __name__ == '__main__':
    string1=[16, 9, 3, 15, 3, 20, 6]
    string2=[20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14]
    for i in range(len(string1)):
        print_letter(string1[i])
    for i in range(len(string2)):
        print_letter(string2[i])
