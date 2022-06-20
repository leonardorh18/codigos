

n = int(input("Que termo deseja encontrar: "))
ultimo=1
penultimo=1
done = False
if (n==1) or (n==2):
    print(f"{n} pertence a sequencia de fibonacci")
else:
    for count in range(2,n):
        termo = ultimo + penultimo
        if termo == n:
            print(f"{n} pertence a sequencia de fibonacci")
            done =  True
            break
        penultimo = ultimo
        ultimo = termo
        count += 1
    if not done:
        print(f"{n} não pertence a sequencia de fibonacci")
        