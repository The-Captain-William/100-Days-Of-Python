def prime_checker(number):
    prime = True
    for x in range(2, number):
        if number % x == 0:
            prime = False
            break

        if prime == True:
            if number % x != 0 and number % number == 0:
                prime = True
                break

    if prime is True:
        print("It's a prime number.")
    if prime == False:
        print("It's not a prime number.")