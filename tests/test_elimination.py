import pytest

from src.elimination import (
    krijo_fqinjet,
    elimino_nyjen,
    llogarit_gjeresite,
    llogarit_gjeresine,
)


def test_krijo_fqinjet():
    fqinjet = krijo_fqinjet(3, [(0, 1), (1, 2)])

    assert fqinjet == [{1}, {0, 2}, {1}]


def test_krijo_fqinjet_me_nyje_te_izoluar():
    fqinjet = krijo_fqinjet(3, [(0, 1)])

    assert fqinjet == [{1}, {0}, set()]


def test_elimino_nyjen_krijon_fill_in():
    fqinjet = [{1, 2}, {0}, {0}]

    elimino_nyjen(fqinjet, 0)

    assert fqinjet == [set(), {2}, {1}]


def test_elimino_nyjen_me_shume_fqinje():
    fqinjet = [
        {1, 2, 3},
        {0},
        {0},
        {0}
    ]

    elimino_nyjen(fqinjet, 0)

    assert fqinjet[0] == set()
    assert fqinjet[1] == {2, 3}
    assert fqinjet[2] == {1, 3}
    assert fqinjet[3] == {1, 2}


def test_llogarit_gjeresite():
    fqinjet = [
        {1, 2},
        {0},
        {0, 3},
        {2}
    ]

    renditja = [0, 1, 2, 3]

    assert llogarit_gjeresite(fqinjet, renditja) == [2, 1, 1, 0]


def test_llogarit_gjeresine_me_prag():
    fqinjet = [
        {1, 2},
        {0},
        {0, 3},
        {2}
    ]

    renditja = [0, 1, 2, 3]

    assert llogarit_gjeresine(fqinjet, renditja, 1) == 1


def test_gjeresia_pa_kufizim_500():
    fqinjet = [set() for _ in range(503)]

    for nyja in range(502):
        fqinjet[nyja].add(nyja + 1)
        fqinjet[nyja + 1].add(nyja)

    renditja = list(range(503))

    assert llogarit_gjeresite(fqinjet, renditja)[0] == 1


def test_refuzon_renditje_te_pavlefshme():
    fqinjet = [{1}, {0}]

    with pytest.raises(ValueError):
        llogarit_gjeresite(fqinjet, [0, 0])


def test_refuzon_numer_te_pavlefshem_nyjesh():
    with pytest.raises(ValueError):
        krijo_fqinjet(2, [(0, 2)])


def test_refuzon_prag_te_pavlefshem():
    fqinjet = [{1}, {0}]

    with pytest.raises(ValueError):
        llogarit_gjeresine(fqinjet, [0, 1], 2)
        

def test_gjeresia_me_shume_se_500_fqinje():
    numri_nyjeve = 503
    brinjet = [(0, i) for i in range(1, numri_nyjeve)]

    fqinjet = krijo_fqinjet(numri_nyjeve, brinjet)
    renditja = list(range(numri_nyjeve))

    gjeresite = llogarit_gjeresite(fqinjet, renditja)

    assert gjeresite[0] == 502