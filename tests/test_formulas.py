from src.ph_diagrams import Acid

acetic_acid = Acid((4.76,), 0.1)
fumaric_acid = Acid((3.02, 4.48), 0.1)
tyrosine = Acid((2.17, 9.19, 10.47), 0.1)


def test_monoprotic_raw_formula():
    assert acetic_acid.formulas(output="raw") == ["HA", "A-"]


def test_monoprotic_latex_formula():
    assert acetic_acid.formulas(output="latex") == ["HA", "A^{-}"]


def test_monoprotic_html_formula():
    assert acetic_acid.formulas(output="html") == ["HA", "A<sup>-</sup>"]


def test_diprotic_raw_formula():
    assert fumaric_acid.formulas(output="raw") == ["H2A", "HA-", "A-2"]


def test_triprotic_raw_formula():
    assert tyrosine.formulas(output="raw") == ["H3A", "H2A-", "HA-2", "A-3"]
