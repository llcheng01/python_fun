def checkWinner(codeList, shoppintCart):
    isSame = 1

    for val in codeList:
        first = shoppingCart.index(val[0])
        subCart = shoppingCart[first:len(val)+1]

        for l, c in zip(val, subCart):
            if (l == 'anything'):
                contine

            if (l!=c):
                isSame = 0
                break

    return isSame
