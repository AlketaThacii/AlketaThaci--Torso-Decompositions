import pytest

from src.graph import lexo_grafin


def test_lexo_grafin_sakte(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("0 1\n1 2\n2 3\n", encoding="utf-8")

    numri_nyjeve, brinjet = lexo_grafin(skedari)

    assert numri_nyjeve == 4
    assert brinjet == [(0, 1), (1, 2), (2, 3)]


def test_lejon_rreshta_bosh(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("0 1\n\n1 2\n", encoding="utf-8")

    numri_nyjeve, brinjet = lexo_grafin(skedari)

    assert numri_nyjeve == 3
    assert len(brinjet) == 2


def test_refuzon_grafin_bosh(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("", encoding="utf-8")

    with pytest.raises(ValueError):
        lexo_grafin(skedari)


def test_refuzon_id_negative(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("-1 2\n", encoding="utf-8")

    with pytest.raises(ValueError):
        lexo_grafin(skedari)


def test_refuzon_bringe_veteliidhese(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("1 1\n", encoding="utf-8")

    with pytest.raises(ValueError):
        lexo_grafin(skedari)


def test_refuzon_bringe_te_perseritura(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("0 1\n1 0\n", encoding="utf-8")

    with pytest.raises(ValueError):
        lexo_grafin(skedari)


def test_refuzon_rresht_me_me_shume_se_dy_id(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("0 1 2\n", encoding="utf-8")

    with pytest.raises(ValueError):
        lexo_grafin(skedari)


def test_refuzon_id_jo_numerik(tmp_path):
    skedari = tmp_path / "graf.gr"
    skedari.write_text("a 2\n", encoding="utf-8")

    with pytest.raises(ValueError):
        lexo_grafin(skedari)
