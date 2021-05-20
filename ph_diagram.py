import numpy as np
import matplotlib.pyplot as plt
from operator import mul
from functools import reduce

pH = np.arange(0, 14.1, 0.1)
hydronium_concentration = 10**(-pH)
pKw = 14
pOH = pKw - pH
hydroxide_concentration = 10**(-pOH)


class Acid:
    def __init__(self, pKa, acid_concetration):
        self.pKa = np.array(pKa)
        self.Ka = 10**(-self.pKa)
        self.Ca = acid_concetration

    @property
    def alpha(self):
        numerators = []
        for i in range(0, self.pKa.size + 1):
            numerators.append(reduce(mul, self.Ka[0:i], hydronium_concentration**(self.pKa.size-i)))
        alphas = [numerator/sum(numerators) for numerator in numerators]
        return alphas

    @property
    def log_concentrations(self):
        log10_HA = np.log10(self.alpha[0] * self.Ca)
        log10_A = np.log10(self.alpha[1] * self.Ca)
        return log10_HA, log10_A

    def plot_params(self, ylabel, axis=None, xlabel='pH'):
        if axis is None:
            fig, ax = plt.subplots(nrows=1, ncols=1, tight_layout=True)
        else:
            ax = axis
        ax.grid(b=True, axis='both', which='major', linestyle='--', linewidth=1.5)
        ax.minorticks_on()
        ax.grid(b=True, axis='both', which='minor', linestyle=':', linewidth=1.0)
        ax.tick_params(axis='both', labelsize=14, length=6, which='major', width=1.5)
        ax.set_xlabel(xlabel, fontsize=16)
        ax.set_ylabel(ylabel, fontsize=16)
        ax.set_axisbelow(True)

    def distribution_diagram(self):
        self.plot_params(ylabel=r'$\alpha$')
        labels = []
        for i in range(1, len(self.alpha) + 1):
            idx = len(self.alpha)-i
            charge = len(self.alpha) - (len(self.alpha) + i - 1)
            charge = str(charge)
            labels.append(fr'$H_{idx}A^{charge}$')

        for i, alpha in enumerate(self.alpha):
            plt.plot(pH, alpha, label=labels[i])
            # TODO labels
        plt.legend(fontsize=16)
        plt.show()

    def pC_diagram(self):
        self.plot_params(ylabel=r'$\log c$')
        plt.plot(pH, -pH)
        plt.plot(pH, -pOH)
        plt.plot(pH, self.log_concentrations[0])
        plt.plot(pH, self.log_concentrations[1])
        plt.show()


if __name__ == "__main__":
    acetic_acid = Acid([4.76], 0.1)
    acetic_acid.distribution_diagram()
    # acetic_acid.pC_diagram()
    fumaric_acid = Acid((3.02, 4.48), 0.1)  # figure 10.3 Harris
    fumaric_acid.distribution_diagram()

    # http://ion.chem.usu.edu/~sbialkow/Classes/3600/Overheads/H3A/H3A.html
    tyrosine = Acid((2.17, 9.19, 10.47), 0.1)  # exercise 10.34 Harris
    tyrosine.distribution_diagram()

    CrIII_hydrolysis = (10**(-3.80), 10**(-6.40), 10**(-6.40), 10**(-11.40))
    CrIII_pKa = np.log10(CrIII_hydrolysis) * -1
    CrIII = Acid(CrIII_pKa, 0.1)
    CrIII.distribution_diagram()
