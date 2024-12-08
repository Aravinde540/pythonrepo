import sys
while True:
    print("1.enter a decimal value to convert in to binary, octal, hexadecimal ")
    print("2.enter  a binary value to convert in to decimal ,octal and hexadecimal")
    print("3.enter a octal value  to convert in to decimal ,binary and hexadecimal")
    print("4.enter a hexa value to convert in to  decimal , binary and octal ")
    print("5.to exit ")
    bse=int(input("enter any  value "))
    match bse:
        case 1:
            n=int(input("enter decimal number"))
            b=bin(n)
            o=oct(n)
            h=hex(n)
            print("binary form of {} is {}".format(n,b))
            print("octal form of {} is {}".format(n,o))
            print("hexadecimal form of {} is {}".format(n,h))
        case 2:
            n=input("enter binary number ")
            d = int(n,2) # 15
            o = oct(d)
            h = hex(d)
            print("decimal form of {} is {}".format(n,d))
            print("octal form of {} is {}".format(n,o))
            print("hexa decimal form of {} is {}".format(n,h))
        case 3:
            n=input("enter octal number ")
            d=int(n,8)
            b = bin(d)
            h = hex(d)
            print("decimal form of {} is {}".format(n, d))
            print("binary decimal form of {} is {}".format(n, b))
            print("hexa decimal form of {} is {}".format(n, h))
        case 4:
            n=input("enter hexa decimal value ")
            d=int(n,16)
            b=bin(d)
            o=oct(d)
            print("decimal form of {} is {}".format(n, d))
            print("binary form of {} is {}".format(n,b))
            print("octal form of {} is {}".format(n, o))
        case 5:
            print("thanks for using our calculator ")
            sys.exit()
        case _:
            print("plz enter a valid option ")

