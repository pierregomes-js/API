def main():
    resto = d % n
    while resto != 0:
        d = n
        n = resto
        resto = d % n

        return

    print(mdc(24, 15))


main()