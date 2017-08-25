def kvadrat(dimenzije, simbol="#"):
    for i in range(dimenzije):
        if i == 0 or i == dimenzije-1:
            print(simbol *dimenzije)
        else:
            print(simbol + " " *(dimenzije-2) + simbol)

kvadrat(5)
remote master

# Modifikacije na lokalnoj grani
#New content added on branch