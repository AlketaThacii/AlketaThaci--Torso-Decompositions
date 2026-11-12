import sys
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

def elimino_nyjen(fqinjet, nyja):
    fqinjte_e_nyjes = list(fqinjet[nyja])

    for i in range(len(fqinjte_e_nyjes)):
        for j in range(i + 1, len(fqinjte_e_nyjes)):
            nyja1 = fqinjte_e_nyjes[i]
            nyja2 = fqinjte_e_nyjes[j]

            fqinjet[nyja1].add(nyja2)
            fqinjet[nyja2].add(nyja1)


    for fqinji in fqinjte_e_nyjes:
        fqinjet[fqinji].discard(nyja)

    fqinjet[nyja].clear()


def llogarit_gjeresine(fqinjet, renditja, t):
    graf_pune = [set(fqinjet_e_nyjes) for fqinjet_e_nyjes in fqinjet]
    gjeresia = 0

    for pozita, nyja in enumerate(renditja):
        shkalla = len(graf_pune[nyja])

        if shkalla > 500:
            return 501

        if pozita >= t:
            gjeresia = max(gjeresia, shkalla)

        elimino_nyjen(graf_pune, nyja)

    return gjeresia

def llogarit_te_gjitha_gjeresite(fqinjet, renditja):
    graf_pune = [set(fqinjet_e_nyjes) for fqinjet_e_nyjes in fqinjet]
    shkallet = []

    for nyja in renditja:
        shkalla = len(graf_pune[nyja])

        if shkalla > 500:
            return [501] * len(renditja)

        shkallet.append(shkalla)
        elimino_nyjen(graf_pune, nyja)

    gjeresite = [0] * len(renditja)
    gjeresia_me_e_madhe = 0

    for pozita in range(len(renditja) - 1, -1, -1):
        gjeresia_me_e_madhe = max(
            gjeresia_me_e_madhe,
            shkallet[pozita]
        )
        gjeresite[pozita] = gjeresia_me_e_madhe

    return gjeresite

def krijo_renditje_min_shkalle(fqinjet):
    graf_pune = [set(fqinjet_e_nyjes) for fqinjet_e_nyjes in fqinjet]
    nyjet_mbetura = set(range(len(graf_pune)))
    renditja = []

    while nyjet_mbetura:
        nyja = min(
            nyjet_mbetura,
            key=lambda n: (len(graf_pune[n]), n)
        )
        if len(graf_pune[nyja]) > 500:
            renditja.extend(sorted(nyjet_mbetura))
            break
    
        renditja.append(nyja)
        elimino_nyjen(graf_pune, nyja)
        nyjet_mbetura.remove(nyja)

    return renditja

skedaret = {
    "small": "data/small.gr",
    "medium": "data/medium.gr",
    "large": "data/large.gr"
}

niveli = sys.argv[1] if len(sys.argv) > 1 else "small"

if niveli not in skedaret:
    raise SystemExit("Shkruaj: py main.py small, medium ose large")

numri_nyjeve, brinjet = lexo_grafin(skedaret[niveli])

print("Grafi i zgjedhur:", niveli)


fqinjet = krijo_fqinjet(numri_nyjeve, brinjet)

print("Numri i nyjeve:", numri_nyjeve)
print("Numri i brinjëve:", len(brinjet))
print("Tri brinjët e para:", brinjet[:3])
print("Fqinjët e nyjës 0:", sorted(fqinjet[0]))

graf_prove = [{1, 2}, {0}, {0}]

elimino_nyjen(graf_prove, 0)

print("Grafi pas heqjes së nyjës 0:", graf_prove)

graf_gjeresie = [
    {1, 2},
    {0},
    {0, 3},
    {2}
]

renditja_prove = [0, 1, 2, 3]
t_prove = 1

rezultati = llogarit_gjeresine(
    graf_gjeresie,
    renditja_prove,
    t_prove
)

print("Gjerësia e grafit të provës:", rezultati)

renditja_fillestare = list(range(numri_nyjeve))
pragu = 0

gjeresia_fillestare = llogarit_gjeresine(
    fqinjet,
    renditja_fillestare,
    pragu
)

print(f"Gjerësia fillestare e {niveli}:", gjeresia_fillestare)

renditja_min = krijo_renditje_min_shkalle(fqinjet)

gjeresia_min = llogarit_gjeresine(
    fqinjet,
    renditja_min,
    pragu
)

print(f"Gjerësia me renditjen e re e {niveli}:", gjeresia_min)

gjeresite = llogarit_te_gjitha_gjeresite(
    fqinjet,
    renditja_min
)

pikat_pareto = []
gjeresia_me_e_mire = float("inf")

for t, gjeresia in enumerate(gjeresite):
    if gjeresia < gjeresia_me_e_mire:
        pikat_pareto.append((t, numri_nyjeve - t, gjeresia))
        gjeresia_me_e_mire = gjeresia

if len(pikat_pareto) > 20:
    indekset = {
        round(i * (len(pikat_pareto) - 1) / 19)
        for i in range(20)
    }
    pikat_pareto = [
        pikat_pareto[i]
        for i in sorted(indekset)
    ]
    
print("Pikat (pragu, madhësia e torso-s, gjerësia):")
print(pikat_pareto)