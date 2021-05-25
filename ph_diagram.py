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
        self.pKa = np.array(pKa, dtype=float)
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
        return [np.log10(alpha * self.Ca) for alpha in self.alpha]

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

    def formulas(self):
        labels = []
        number_of_species = len(self.alpha)
        for i in range(1, number_of_species + 1):
            idx = number_of_species - i
            charge = number_of_species - (number_of_species + i - 1)
            if charge == 0:
                charge = ''
            if idx == 0:
                labels.append(f'$A^{{{charge}}}$')
            if idx == 1:
                labels.append(f'$HA^{{{charge}}}$')
            else:
                labels.append(f'$H_{{{idx}}}A^{{{charge}}}$')
        return labels

    def distribution_diagram(self):
        self.plot_params(ylabel=r'$\alpha$')
        labels = self.formulas()
        for i, alpha in enumerate(self.alpha):
            plt.plot(pH, alpha, label=labels[i])
        plt.legend(fontsize=16, bbox_to_anchor=(1, 1))
        plt.show()

    def pC_diagram(self):
        self.plot_params(ylabel=r'$\log c$')
        plt.plot(pH, -pH, color='black', linestyle='--', label='pH')
        plt.plot(pH, -pOH, color='black', linestyle='--', label='pOH')
        labels = self.formulas()
        for i, logc in enumerate(self.log_concentrations):
            plt.plot(pH, logc, label=labels[i])
        plt.ylim(-14, 0)
        plt.legend(fontsize=16, bbox_to_anchor=(1, 1))
        plt.show()


if __name__ == "__main__":
    acetic_acid = Acid([4.76], 0.1)
    acetic_acid.distribution_diagram()
    acetic_acid.pC_diagram()

    fumaric_acid = Acid((3.02, 4.48), 0.1)  # figure 10.3 Harris
    fumaric_acid.distribution_diagram()

    livro_figura_19 = Acid((3.0, 8.0), 0.1)
    livro_figura_19.pC_diagram()

    livro_figura_25 = Acid((2, 5, 12), 0.1)
    livro_figura_25.pC_diagram()
    # http://ion.chem.usu.edu/~sbialkow/Classes/3600/Overheads/H3A/H3A.html
    tyrosine = Acid((2.17, 9.19, 10.47), 0.1)  # exercise 10.34 Harris
    tyrosine.distribution_diagram()

    CrIII_hydrolysis = (10**(-3.80), 10**(-6.40), 10**(-6.40), 10**(-11.40))
    CrIII_pKa = np.log10(CrIII_hydrolysis) * -1
    CrIII = Acid(CrIII_pKa, 0.1)
    CrIII.distribution_diagram()
    CrIII.pC_diagram()
