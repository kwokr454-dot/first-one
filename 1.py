import random
def challenge():
    challenge=["lower","same","higher"]
    number=random.randint(1,10)
    selected_challenge=random.randint(0,len(challenge) - 1)
    selected = challenge[selected_challenge]
    if selected=="lower":
        print("you have to guess a number that is lower than the selected number")
        numberg=int(input("type in your guess"))
        if numberg < number:
            print("you win and the number was", number)
        else:
            print("you lose")
    elif selected=="same":
        print("you have to guess a number that is the same as the selected number")
        numberg=int(input("type in your guess"))
        if numberg==number:
            print("you got it right")
        else:
            print("you got it wrong, it was ", number)
            
    else:
        print("you have to guess a number that is higher than the selected number")
        numberg=int(input("type in your guess"))
        if numberg>number:
            print("you got it right")
        else:
            print("you got it wrong, it was ", number)

challenge()
