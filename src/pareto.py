def hypervolume_2d(pikat, pika_referuese):

    if not pikat:
        return 0

    pikat = sorted(pikat)

    siperfaqja = 0

    for i, (x, y) in enumerate(pikat):
        x_pasues = (
            pikat[i + 1][0]
            if i + 1 < len(pikat)
            else pika_referuese[0]
        )

        siperfaqja += (
            (x_pasues - x) *
            (pika_referuese[1] - y)
        )

    return siperfaqja



def zgjedh_zgjidhjet_hypervolume(
    zgjidhjet,
    numri_nyjeve,
    kufiri=20
):

    zgjidhjet = sorted(zgjidhjet, key=lambda p: p[0])

    while len(zgjidhjet) > kufiri:
        humbjet = []

        for i, (threshold, width, order) in enumerate(zgjidhjet):

            threshold_pasues = (
                zgjidhjet[i + 1][0]
                if i + 1 < len(zgjidhjet)
                else numri_nyjeve
            )

            width_paraprak = (
                zgjidhjet[i - 1][1]
                if i > 0
                else numri_nyjeve
            )

            humbja = (
                (threshold_pasues - threshold) *
                (width_paraprak - width)
            )

            humbjet.append((humbja, i))

        _, indeksi = min(humbjet)
        zgjidhjet.pop(indeksi)

    return zgjidhjet
