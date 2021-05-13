import numpy as np
import matplotlib.pyplot as plt


pH = np.arange(0, 14.1, 0.1)
hydronium_concentration = 10**(-pH)
pKw = 14
pOH = pKw - pH
hydroxide_concentration = 10**(-pOH)


class Acid:
    def __init__(self, pKa, acid_concetration):
        self.pKa = pKa
        self.Ka = 10**(-pKa)
        self.Ca = acid_concetration

    def alpha(self):
        alpha_HA = hydronium_concentration / (hydronium_concentration + self.Ka)
        alpha_A = self.Ka / (hydronium_concentration + self.Ka)
        return alpha_HA, alpha_A

    def log_concentrations(self):
        log10_HA = np.log10(self.alpha()[0] * self.Ca)
        log10_A = np.log10(self.alpha()[1] * self.Ca)
        return log10_HA, log10_A

    def distribution_diagram(self):
        plt.plot(pH, self.alpha()[0])
        plt.plot(pH, self.alpha()[1])
        plt.show()

    def pC_diagram(self):
        plt.plot(pH, -pH)
        plt.plot(pH, -pOH)
        plt.plot(pH, self.log_concentrations()[0])
        plt.plot(pH, self.log_concentrations()[1])
        plt.show()


if __name__ == "__main__":
    acetic_acid = Acid(4.76, 0.1)
    # acetic_acid.distribution_diagram()
    acetic_acid.pC_diagram()
