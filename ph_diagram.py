import numpy as np
import matplotlib.pyplot as plt
from operator import mul
from functools import reduce
import plotly.graph_objects as go

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

    def distribution_diagram_plotly(self):
        fig = go.Figure()
        labels = self.formulas()
        for i, alpha in enumerate(self.alpha):
            fig.add_trace(go.Scatter(x=pH,
                                     y=alpha,
                                     mode='lines',
                                     line=dict(width=3),
                                     name=labels[i],
                                     hovertemplate="%{x:.2f}, %{y:.3f}"
                                    ))
        fig.update_layout(
            title='Distribution diagram',
            title_x=0.5,
            xaxis={'title': 'pH'},
            yaxis={'title': r'$\alpha$'},
            font={'size': 18},
            template='plotly_dark',
            yaxis_tickformat='.3f',
            xaxis_tickformat='.2f',
        )
        # fig.show()
        fig.write_html('output.html', auto_open=True, include_mathjax='cdn')

    def pC_diagram_plotly(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=pH, y=-pH, mode='lines', opacity=0.5,
                                 line=dict(color='black', width=1,
                                           dash='dash')))
        fig.add_trace(go.Scatter(x=pH, y=-pOH, mode='lines', opacity=0.5,
                                 line=dict(color='black', width=1,
                                           dash='dash')))
        labels = self.formulas()
        for i, logc in enumerate(self.log_concentrations):
            fig.add_trace(go.Scatter(x=pH,
                                     y=logc,
                                     mode='lines',
                                     name=labels[i],
                                     hovertemplate="%{x:.2f}, %{y:.3f}"
                                    ))
        # fig.show()
        fig.write_html('output.html', auto_open=True, include_mathjax='cdn')


if __name__ == '__main__':
    acetic_acid = Acid((4.76,), 0.1)
    acetic_acid.distribution_diagram_plotly()
    # acetic_acid.pC_diagram_plotly()
