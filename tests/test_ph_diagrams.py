import numpy as np

from src.ph_diagrams import Acid

FOLDER = "tests/golden_files/"


class TestAceticAcid:
    acetic_acid = Acid((4.76,), 0.1)

    def test_acetic_acid_alphas(self):
        assert np.allclose(
            self.acetic_acid.alpha,
            np.loadtxt(f"{FOLDER}acetic_acid_alphas.csv", delimiter=",", unpack=True),
        )

    def test_acetic_acid_logc(self):
        assert np.allclose(
            self.acetic_acid.log_concentrations,
            np.loadtxt(f"{FOLDER}acetic_acid_logc.csv", delimiter=",", unpack=True),
        )


class TestFumaricAcid:
    fumaric_acid = Acid((3.02, 4.48), 0.1)  # figure 10.3 Harris

    def test_fumaric_acid_alphas(self):
        assert np.allclose(
            self.fumaric_acid.alpha,
            np.loadtxt(f"{FOLDER}fumaric_acid_alphas.csv", delimiter=",", unpack=True),
        )

    def test_fumaric_acid_logc(self):
        assert np.allclose(
            self.fumaric_acid.log_concentrations,
            np.loadtxt(f"{FOLDER}fumaric_acid_logc.csv", delimiter=",", unpack=True),
        )


class TestGenericDiproticAcid:
    generic_diprotic = Acid((3.0, 8.0), 0.1)  # figure 19 Kahlert & Scholz

    def test_generic_diprotic_acid_alphas(self):
        assert np.allclose(
            self.generic_diprotic.alpha,
            np.loadtxt(
                f"{FOLDER}gen_diprotic_acid_alphas.csv", delimiter=",", unpack=True
            ),
        )

    def test_generic_diprotic_acid_logc(self):
        assert np.allclose(
            self.generic_diprotic.log_concentrations,
            np.loadtxt(
                f"{FOLDER}gen_diprotic_acid_logc.csv", delimiter=",", unpack=True
            ),
        )


class TestGenericTriproticAcid:
    generic_triprotic = Acid((2, 5, 12), 0.1)

    def test_generic_triprotic_acid_alphas(self):
        assert np.allclose(
            self.generic_triprotic.alpha,
            np.loadtxt(
                f"{FOLDER}gen_triprotic_acid_alphas.csv", delimiter=",", unpack=True
            ),
        )

    def test_generic_triprotic_acid_logc(self):
        assert np.allclose(
            self.generic_triprotic.log_concentrations,
            np.loadtxt(
                f"{FOLDER}gen_triprotic_acid_logc.csv", delimiter=",", unpack=True
            ),
        )


class TestTyrosine:
    tyrosine = Acid((2.17, 9.19, 10.47), 0.1)  # exercise 10.34 Harris

    def test_tyrosine_alphas(self):
        assert np.allclose(
            self.tyrosine.alpha,
            np.loadtxt(f"{FOLDER}tyrosine_alphas.csv", delimiter=",", unpack=True),
        )

    def test_tyrosine_logc(self):
        assert np.allclose(
            self.tyrosine.log_concentrations,
            np.loadtxt(f"{FOLDER}tyrosine_logc.csv", delimiter=",", unpack=True),
        )


class TestCrIII:
    CrIII_hydrolysis = (
        10 ** (-3.80),
        10 ** (-6.40),
        10 ** (-6.40),
        10 ** (-11.40),
    )  # exercise 10.35 Harris
    CrIII_pKa = np.log10(CrIII_hydrolysis) * -1
    CrIII = Acid(CrIII_pKa, 0.1)

    def test_CrIII_alphas(self):  # noqa
        assert np.allclose(
            self.CrIII.alpha,
            np.loadtxt(
                f"{FOLDER}CrIII_hydrolysis_alphas.csv", delimiter=",", unpack=True
            ),
        )

    def test_CrIII_logc(self):  # noqa
        assert np.allclose(
            self.CrIII.log_concentrations,
            np.loadtxt(
                f"{FOLDER}CrIII_hydrolysis_logc.csv", delimiter=",", unpack=True
            ),
        )
