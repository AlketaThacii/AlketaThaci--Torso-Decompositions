def lexo_grafin(rruga):


    brinjet = []
    nyjet = set()

    with open(rruga, "r", encoding="utf-8") as skedari:
        for numri_rreshtit, rreshti in enumerate(skedari, start=1):
            rreshti = rreshti.strip()

            if not rreshti:
                continue

            pjeset = rreshti.split()

            if len(pjeset) != 2:
                raise ValueError(
                    f"Rreshti {numri_rreshtit}: "
                    "duhet të përmbajë saktësisht dy ID të nyjeve."
                )

            try:
                nyja1, nyja2 = map(int, pjeset)
            except ValueError:
                raise ValueError(
                    f"Rreshti {numri_rreshtit}: "
                    "ID-të e nyjeve duhet të jenë numra të plotë."
                )

            if nyja1 < 0 or nyja2 < 0:
                raise ValueError(
                    f"Rreshti {numri_rreshtit}: "
                    "ID-të e nyjeve nuk mund të jenë negative."
                )

            if nyja1 == nyja2:
                raise ValueError(
                    f"Rreshti {numri_rreshtit}: "
                    "nuk lejohen brinjët vetëlidhëse."
                )

            brinjet.append((nyja1, nyja2))
            nyjet.add(nyja1)
            nyjet.add(nyja2)

    if not brinjet:
        raise ValueError("Grafi nuk përmban asnjë brinjë.")

    if len(brinjet) != len(set(
        (min(a, b), max(a, b)) for a, b in brinjet
    )):
        raise ValueError("Grafi përmban brinjë të përsëritura.")

    numri_nyjeve = max(nyjet) + 1

    return numri_nyjeve, brinjet
