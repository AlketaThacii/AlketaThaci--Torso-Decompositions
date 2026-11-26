def krijo_fqinjet(numri_nyjeve, brinjet):

    if numri_nyjeve < 0:
        raise ValueError("Numri i nyjeve nuk mund të jetë negativ.")

    fqinjet = [set() for _ in range(numri_nyjeve)]

    for nyja1, nyja2 in brinjet:
        if not (0 <= nyja1 < numri_nyjeve):
            raise ValueError(f"ID e pavlefshme e nyjës: {nyja1}")

        if not (0 <= nyja2 < numri_nyjeve):
            raise ValueError(f"ID e pavlefshme e nyjës: {nyja2}")

        if nyja1 == nyja2:
            raise ValueError("Nuk lejohen brinjë vetëlidhëse.")

        fqinjet[nyja1].add(nyja2)
        fqinjet[nyja2].add(nyja1)

    return fqinjet


def elimino_nyjen(fqinjet, nyja):

    if not 0 <= nyja < len(fqinjet):
        raise IndexError("ID e nyjës është jashtë kufijve.")

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


def llogarit_gjeresite(fqinjet, renditja):
    
    if sorted(renditja) != list(range(len(fqinjet))):
        raise ValueError("Renditja duhet të përmbajë çdo nyje saktësisht një herë.")

    graf_pune = [set(fqinjet_e_nyjes) for fqinjet_e_nyjes in fqinjet]
    shkallet = []

    for nyja in renditja:
        shkallet.append(len(graf_pune[nyja]))
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


def llogarit_gjeresine(fqinjet, renditja, pragu):

    if not isinstance(pragu, int) or not 0 <= pragu < len(renditja):
        raise ValueError("Pragu duhet të jetë numër i vlefshëm i pozitave.")

    gjeresite = llogarit_gjeresite(fqinjet, renditja)
    return gjeresite[pragu]
