#code by Mariusz Hybiak
#code to solve the second mini RSA ctf
with open('output.txt', 'w') as f:
    for i in range(0, 10000):
        liczba=add(N*(i),C)
        m=iroot(liczba, 3)
        wynik=digits(m[0],16)
        if(len(wynik)%2==0):
            liczba2=bytes.fromhex(wynik)
            print(liczba2)
            f.write(str(liczba2))
