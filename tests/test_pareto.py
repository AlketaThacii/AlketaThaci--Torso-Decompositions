from src.pareto import (
    hypervolume_2d,
    zgjedh_zgjidhjet_hypervolume
)

def test_hypervolume_2d():
    pikat = [(1, 4), (3, 2)]
    referenca = (5, 5)

    assert hypervolume_2d(pikat, referenca) == 8


def test_hypervolume_pa_pika():
    assert hypervolume_2d([], (5, 5)) == 0


def test_zgjedhja_e_maksimumi_20_zgjidhjeve():
    zgjidhjet = [
        (i, 30 - i, list(range(5)))
        for i in range(25)
    ]

    rezultati = zgjedh_zgjidhjet_hypervolume(
        zgjidhjet, 30, 20
    )

    assert len(rezultati) == 20


def test_nuk_ndryshohen_zgjidhjet_origjinale():
    zgjidhjet = [
        (0, 4, [0, 1]),
        (2, 3, [0, 1]),
        (4, 1, [0, 1])
    ]

    kopja = zgjidhjet.copy()

    zgjedh_zgjidhjet_hypervolume(
        zgjidhjet, 5, 2
    )

    assert zgjidhjet == kopja
