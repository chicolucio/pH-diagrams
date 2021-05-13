import numpy as np
import matplotlib.pyplot as plt


pH = np.arange(0, 14.1, 0.1)
hydronium_concentration = 10**(-pH)


class Acid:
    def __init__(self, pKa):
        self.pKa = pKa
        self.Ka = 10**(-pKa)

    def alpha(self):
        alpha_HA = hydronium_concentration / (hydronium_concentration + self.Ka)
        alpha_A = self.Ka / (hydronium_concentration + self.Ka)
        return alpha_HA, alpha_A

    def distribution_diagram(self):
        plt.plot(pH, self.alpha()[0])
        plt.plot(pH, self.alpha()[1])
        plt.show()


if __name__ == "__main__":
    acetic_acid = Acid(4.76)
    acetic_acid.distribution_diagram()
