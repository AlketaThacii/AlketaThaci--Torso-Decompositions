def lexo_grafin(rruga):
    brinjet = []

    with open(rruga, "r", encoding="utf-8") as skedari:
        for rreshti in skedari:
            numrat = rreshti.split()

            if len(numrat) == 2:
                nyja1 = int(numrat[0])
                nyja2 = int(numrat[1])
                brinjet.append((nyja1, nyja2))

    numri_nyjeve = max(max(brinja) for brinja in brinjet) + 1

    return numri_nyjeve, brinjet

def krijo_fqinjet(numri_nyjeve, brinjet):
    fqinjet = [set() for _ in range(numri_nyjeve)]

    for nyja1, nyja2 in brinjet:
        fqinjet[nyja1].add(nyja2)
        fqinjet[nyja2].add(nyja1)

    return fqinjet

numri_nyjeve, brinjet = lexo_grafin("data/small.gr")
fqinjet = krijo_fqinjet(numri_nyjeve, brinjet)

print("Numri i nyjeve:", numri_nyjeve)
print("Numri i brinjëve:", len(brinjet))
print("Tri brinjët e para:", brinjet[:3])
print("Fqinjët e nyjës 0:", sorted(fqinjet[0]))