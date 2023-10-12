#!/usr/bin/env python3
import math

xyz = input("Chcete pocitat linearni teleso(l)/3d teleso(3d) ")

if xyz == "l" or xyz == "linearni":
    lteleso = input("Vyberte si teleso z nabidky (ctverec(1), obdelnik(2), kruh(3)): ")
    vzorec = input("Napiste co chcete pocitat(obsah(S), obvod(o)): ")

    if lteleso == "3" or lteleso == "kruh":
        r = float(input("rozmery polomeru - r "))
        if vzorec =="S":
            print(f"obsah je kruhu {math.pi*r**2}")
        elif vzorec == "o":
            print(f"obvod kruhu je {2*math.pi*r}")

    elif lteleso == "2" or lteleso == "obdelnik":
        a = float(input("rozmery strana a "))
        b = float(input("rozmery strana b "))
        if vzorec =="S":
            print(f"obsah obdelniku je {a*b}")
        elif vzorec == "o":
            print(f"obvod obdelniku je {2*(a+b)}")

    elif lteleso == "1" or lteleso == "ctverec":
        a = float(input("rozmery strana a "))
        if vzorec =="S":
            print(f"obsah ctverce je {a**2}")
        elif vzorec == "o":
            print(f"obvod ctverce je {4*a}")

elif xyz == "3d" or "3d teleso":
    vzorec = input("Napiste co chcete pocitat(objem (V), obsah(S), obvod(o)): ")
    dteleso = input("Vyberte si teleso z nabidky (krychle(1), kvadr(2), koule(3)): ")

    if dteleso == "3" or dteleso =="koule":
        r = float(input("rozmery polomeru - r "))
        if vzorec =="S":
            print(f"obsah koule je {4*math.pi*r**2}")
        elif vzorec == "V":
            print(f"objem koule je {4/3*math.pi*r}")

    elif dteleso == "1" or dteleso == "krychle":
        a = float(input("rozmery strana a "))
        if vzorec =="S":
            print(f"obsah kryhle je {6*a**2}")
        elif vzorec == "V":
            print(f"objem krychle je {a ** 3}")
        elif vzorec == "o":
            print(f"obvod krychle je {12*a}")

    elif dteleso == "2" or dteleso == "kvadr":
        a = float(input("rozmery strana a "))
        b = float(input("rozmery strana b "))
        c = float(input("rozmery strana c "))
        if vzorec =="S":
            print(f"obsah kvadru je {2*(a*b*c)}")
        elif vzorec == "V":
            print(f"objem kvadru je {a*b*c}")
        elif vzorec == "o":
            print(f"obvod kvadru je {4*(a+b+c)}")
