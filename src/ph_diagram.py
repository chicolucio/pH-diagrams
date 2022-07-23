import numpy as np
import matplotlib.pyplot as plt
from operator import mul
from functools import reduce
import plotly.graph_objects as go
from chempy import Substance

pH = np.arange(0, 14.1, 0.1)
hydronium_concentration = 10**(-pH)
pKw = 14
pOH = pKw - pH
hydroxide_concentration = 10**(-pOH)


class Acid:
    def __init__(self, pKa, acid_concetration):  # noqa
        self.pKa = np.array(pKa, dtype=float)
        self.Ka = 10**(-self.pKa)
        self.Ca = acid_concetration

    @property
    def alpha(self):
        numerators = []
        for i in range(0, self.pKa.size + 1):
            numerators.append(reduce(mul,
                                     self.Ka[0:i],
                                     hydronium_concentration**(self.pKa.size-i)))  # noqa: E501
        alphas = [numerator/sum(numerators) for numerator in numerators]
        return alphas

    @property
    def log_concentrations(self):
        return [np.log10(alpha * self.Ca) for alpha in self.alpha]

    def plot_params(self, ylabel, ax=None, xlabel='pH'):
        ax.grid(b=True, axis='both', which='major',
                linestyle='--', linewidth=1.5)
        ax.minorticks_on()
        ax.grid(b=True, axis='both', which='minor',
                linestyle=':', linewidth=1.0)
        ax.tick_params(axis='both', labelsize=14,
                       length=6, which='major', width=1.5)
        ax.set_xlabel(xlabel, fontsize=16)
        ax.set_ylabel(ylabel, fontsize=16)
        ax.set_axisbelow(True)
        return ax

    def formulas(self, output):
        labels = []
        number_of_species = len(self.alpha)
        for i in range(1, number_of_species + 1):
            idx = number_of_species - i
            charge = number_of_species - (number_of_species + i - 1)
            if charge == 0:
                charge = ''
            elif charge == -1:
                charge = '-'
            else:
                pass

            if idx == 0:
                labels.append(f'B{charge}')
            elif idx == 1:
                labels.append(f'HB{charge}')
            else:
                labels.append(f'H{idx}B{charge}')

        if output == 'raw':
            return [formula.replace('B', 'A') for formula in labels]

        elif output == 'latex':
            temp = [Substance.from_formula(
                formula).latex_name for formula in labels]
            return [formula.replace('B', 'A') for formula in temp]

        elif output == 'html':
            temp = [Substance.from_formula(
                formula).html_name for formula in labels]
            return [formula.replace('B', 'A') for formula in temp]

        else:
            raise ValueError

    def _distribution_diagram_matplotlib(self, ax=None, legend=True):
        if ax is None:
            fig, ax = plt.subplots(facecolor=(1.0, 1.0, 1.0),
                                   constrained_layout=True)
        self.plot_params(ax=ax, ylabel=r'$\alpha$')
        labels = self.formulas(output='latex')
        for i, alpha in enumerate(self.alpha):
            ax.plot(pH, alpha, label=f'${labels[i]}$')
        if legend:
            ax.legend(fontsize=16, bbox_to_anchor=(1, 1))
        return ax

    def _pC_diagram_matplotlib(self, ax=None, legend=True):  # noqa
        if ax is None:
            fig, ax = plt.subplots(facecolor=(1.0, 1.0, 1.0),
                                   constrained_layout=True)
        self.plot_params(ax=ax, ylabel=r'$\log c$')
        ax.plot(pH, -pH, color='black', linestyle='--', label='pH')
        ax.plot(pH, -pOH, color='black', linestyle='--', label='pOH')
        labels = self.formulas(output='latex')
        for i, logc in enumerate(self.log_concentrations):
            ax.plot(pH, logc, label=f'${labels[i]}$')
        ax.set_ylim(-14, 0)
        if legend:
            ax.legend(fontsize=16, bbox_to_anchor=(1, 1))
        return ax

    def _distribution_diagram_plotly(self, output=False):
        fig = go.Figure()
        labels = self.formulas(output='html')
        for i, alpha in enumerate(self.alpha):
            fig.add_trace(go.Scatter(x=pH,
                                     y=alpha,
                                     mode='lines',
                                     line=dict(width=3),
                                     name=labels[i],
                                     hovertemplate='pH: %{x:.2f}, &#945;: %{y:.3f}'  # noqa: E501
                                     ))
        fig.update_layout(
            title='Distribution diagram',
            title_x=0.5,
            xaxis={'title': 'pH'},
            yaxis={'title': r'$\alpha$'},
            template='plotly_dark',
            yaxis_tickformat='.3f',
            xaxis_tickformat='.2f',
            legend=dict(orientation='h',
                        yanchor='top',
                        y=-0.2,
                        xanchor='left')
        )
        if output:
            fig.write_html('output_distribution.html',
                           auto_open=True, include_mathjax='cdn',
                           config={'modeBarButtonsToAdd': ['v1hovermode',
                                                           'hovercompare',
                                                           'toggleSpikelines']
                                   })
        else:
            return fig

    def _pC_diagram_plotly(self, output=False, title=''):  # noqa
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=pH, y=-pH, mode='lines', opacity=0.5,
                                 name='pH',
                                 hoverinfo='skip',
                                 line=dict(color='white', width=1,
                                           dash='dash')))
        fig.add_trace(go.Scatter(x=pH, y=-pOH, mode='lines', opacity=0.5,
                                 name='pOH',
                                 hoverinfo='skip',
                                 line=dict(color='white', width=1,
                                           dash='dash')))
        labels = self.formulas(output='html')
        for i, logc in enumerate(self.log_concentrations):
            fig.add_trace(go.Scatter(x=pH,
                                     y=logc,
                                     mode='lines',
                                     name=labels[i],
                                     hovertemplate='pH: %{x:.2f}, logC: %{y:.3f}'  # noqa: E501
                                     ))
        fig.update_layout(
            title='pC Diagram',
            title_x=0.5,
            xaxis={'title': 'pH'},
            yaxis={'title': 'logC', 'range': [-14, 0]},
            template='plotly_dark',
            yaxis_tickformat='.3f',
            xaxis_tickformat='.2f',
            legend=dict(orientation='h',
                        yanchor='top',
                        y=-0.2,
                        xanchor='left')
        )

        if output:
            fig.write_html('output_pC.html', auto_open=True,
                           include_mathjax='cdn',
                           config={'modeBarButtonsToAdd': ['v1hovermode',
                                                           'hovercompare',
                                                           'toggleSpikelines']
                                   })
        else:
            return fig

    def plot(self, plot_type='distribution',
             backend='matplotlib', output_plotly=False,
             ax=None, legend=True, title=''):
        if plot_type == 'distribution' and backend == 'matplotlib':
            return self._distribution_diagram_matplotlib(ax=ax, legend=legend)
        elif plot_type == 'distribution' and backend == 'plotly':
            return self._distribution_diagram_plotly(output_plotly, title)
        elif plot_type == 'pC' and backend == 'matplotlib':
            return self._pC_diagram_matplotlib(ax=ax, legend=legend)
        elif plot_type == 'pC' and backend == 'plotly':
            return self._pC_diagram_plotly(output_plotly, title)
        else:
            raise ValueError('Invalid type and/or plot backend')


if __name__ == '__main__':
    # An example
    tyrosine = Acid((2.17, 9.19, 10.47), 0.1)
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(16, 8),
                                   facecolor=(1, 1, 1))
    tyrosine.plot(ax=ax1, legend=False)
    tyrosine.plot(ax=ax2, plot_type='pC', legend=False)
    handles, labels = ax2.get_legend_handles_labels()
    fig.legend(loc='upper center', ncol=8,
               handles=handles, labels=labels, fontsize=16,
               bbox_to_anchor=(0.5, 1.0))
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()
