from functools import reduce
from itertools import cycle
from operator import mul

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from chempy import Substance

pH = np.arange(0, 14.1, 0.1)
hydronium_concentration = 10 ** (-pH)
pKw = 14
pOH = pKw - pH
hydroxide_concentration = 10 ** (-pOH)


class Acid:
    """
    A class used to represent an acid

    Attributes
    ----------
    pKa : np.array
        array with each pKa of the acid
    Ka : np.array
        array with each Ka of the acid
    Ca : float
        analytical concentration of the acid
    alpha : list
        alpha values for each acid form
    log_concentrations : list
        log ci for each acid form

    Methods
    -------
    formulas(ouput)
        generates formulas for each acid form in raw string, LaTeX, or HTML
    plot(plot_type, backend, output_plotly, ax, legend, title)
        plots the distribution diagram or logc diagram using as backend
        Matplotlib or Plotly
    """

    def __init__(self, pKa, acid_concentration):  # noqa
        """
        Parameters
        ----------
        pKa : tuple
            the acid pKa's
        acid_concentration : float
            acid analytical concentration
        """
        self.pKa = np.array(pKa, dtype=float)
        self.Ka = 10 ** (-self.pKa)
        self.Ca = acid_concentration

    @property
    def alpha(self):
        """
        Returns
        -------
        list
            alpha values for each acid form
        """
        numerators = []
        for i in range(0, self.pKa.size + 1):
            numerators.append(
                reduce(
                    mul, self.Ka[0:i], hydronium_concentration ** (self.pKa.size - i)
                )
            )
        alphas = [numerator / sum(numerators) for numerator in numerators]
        return alphas

    @property
    def log_concentrations(self):
        """
        Returns
        -------
        list
            log ci values for each acid form
        """
        return [np.log10(alpha * self.Ca) for alpha in self.alpha]

    def plot_params(self, ylabel, ax=None, xlabel="pH"):
        """
        Matplotlib plot parameters

        Parameters
        ----------
        ylabel : str
        ax : Matplotlib axes
        xlabel : str

        Returns
        -------
        Matplotlib axes
        """
        ax.grid(b=True, axis="both", which="major", linestyle="--", linewidth=1.5)
        ax.minorticks_on()
        ax.grid(b=True, axis="both", which="minor", linestyle=":", linewidth=1.0)
        ax.tick_params(axis="both", labelsize=14, length=6, which="major", width=1.5)
        ax.set_xlabel(xlabel, fontsize=16)
        ax.set_ylabel(ylabel, fontsize=16)
        ax.set_axisbelow(True)
        return ax

    def formulas(self, output):
        """
        Generates formulas for each acid form in raw string, LaTeX, or HTML

        Parameters
        ----------
        output : str
            Raw string if 'raw'; LaTeX if 'latex'; HTML if 'html'

        Raises
        ------
        ValueError
            If no valid output.

        Returns
        -------
        list
            List of strings in the chosen output type
        """

        labels = []
        number_of_species = len(self.alpha)
        for i in range(1, number_of_species + 1):
            idx = number_of_species - i
            charge = number_of_species - (number_of_species + i - 1)
            if charge == 0:
                charge = ""
            elif charge == -1:
                charge = "-"
            else:
                pass

            if idx == 0:
                labels.append(f"B{charge}")
            elif idx == 1:
                labels.append(f"HB{charge}")
            else:
                labels.append(f"H{idx}B{charge}")

        if output == "raw":
            return [formula.replace("B", "A") for formula in labels]

        elif output == "latex":
            temp = [Substance.from_formula(formula).latex_name for formula in labels]
            return [formula.replace("B", "A") for formula in temp]

        elif output == "html":
            temp = [Substance.from_formula(formula).html_name for formula in labels]
            return [formula.replace("B", "A") for formula in temp]

        else:
            raise ValueError("Invalid output type")

    def _distribution_diagram_matplotlib(self, ax=None, legend=True, title=""):
        if ax is None:
            fig, ax = plt.subplots(facecolor=(1.0, 1.0, 1.0), constrained_layout=True)
        self.plot_params(ax=ax, ylabel=r"$\alpha$")
        labels = self.formulas(output="latex")
        for i, alpha in enumerate(self.alpha):
            ax.plot(pH, alpha, label=f"${labels[i]}$")
        if legend:
            ax.legend(fontsize=16, bbox_to_anchor=(1, 1))
        ax.set_title(title)
        return ax

    def _pC_diagram_matplotlib(self, ax=None, legend=True, title=""):  # noqa
        if ax is None:
            fig, ax = plt.subplots(facecolor=(1.0, 1.0, 1.0), constrained_layout=True)
        self.plot_params(ax=ax, ylabel=r"$\log c$")
        ax.plot(pH, -pH, color="black", linestyle="--", label="pH")
        ax.plot(pH, -pOH, color="black", linestyle="--", label="pOH")
        labels = self.formulas(output="latex")
        for i, logc in enumerate(self.log_concentrations):
            ax.plot(pH, logc, label=f"${labels[i]}$")
        ax.set_ylim(-14, 0)
        if legend:
            ax.legend(fontsize=16, bbox_to_anchor=(1, 1))
        ax.set_title(title)
        return ax

    def _distribution_diagram_plotly(self, output=False, title=""):
        fig = go.Figure()
        labels = self.formulas(output="html")
        for i, alpha in enumerate(self.alpha):
            fig.add_trace(
                go.Scatter(
                    x=pH,
                    y=alpha,
                    mode="lines",
                    line=dict(width=3),
                    name=labels[i],
                    hovertemplate="pH: %{x:.2f}, &#945;: %{y:.3f}",
                )
            )
        fig.update_layout(
            title=title,
            title_x=0.5,
            xaxis={"title": "pH"},
            yaxis={"title": "α"},
            # template='plotly_dark',
            yaxis_tickformat=".1f",
            xaxis_tickformat=".1f",
            margin=dict(autoexpand=True, t=30, b=30, l=30, r=30),
            legend=dict(orientation="h", yanchor="top", y=-0.2, xanchor="left"),
            modebar=dict(orientation="v"),
        )
        if output:
            fig.write_html(
                "output_distribution.html",
                auto_open=True,
                include_mathjax="cdn",
                config={
                    "modeBarButtonsToAdd": [
                        "v1hovermode",
                        "hovercompare",
                        "toggleSpikelines",
                    ]
                },
            )
        else:
            return fig

    def _pC_diagram_plotly(self, output=False, title=""):  # noqa
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=pH,
                y=-pH,
                mode="lines",
                opacity=0.5,
                name="pH",
                hoverinfo="skip",
                line=dict(color="darkgray", width=1, dash="dash"),
            )
        )
        fig.add_trace(
            go.Scatter(
                x=pH,
                y=-pOH,
                mode="lines",
                opacity=0.5,
                name="pOH",
                hoverinfo="skip",
                line=dict(color="darkgray", width=1, dash="dashdot"),
            )
        )
        labels = self.formulas(output="html")
        palette = cycle(px.colors.qualitative.Plotly)
        for i, logc in enumerate(self.log_concentrations):
            fig.add_trace(
                go.Scatter(
                    x=pH,
                    y=logc,
                    mode="lines",
                    line=dict(width=3, color=next(palette)),
                    name=labels[i],
                    hovertemplate="pH: %{x:.2f}, logC: %{y:.3f}",
                )
            )
        # TODO yaxis with absolute values (label change to -logc)
        fig.update_layout(
            title=title,
            title_x=0.5,
            xaxis={"title": "pH"},
            yaxis={"title": "logC", "range": [-14, 0]},
            # template='plotly_dark',
            yaxis_tickformat=".1f",
            xaxis_tickformat=".1f",
            margin=dict(autoexpand=True, t=30, b=30, l=30, r=30),
            legend=dict(orientation="h", yanchor="top", y=-0.2, xanchor="left"),
            modebar=dict(orientation="v"),
        )

        if output:
            fig.write_html(
                "output_pC.html",
                auto_open=True,
                include_mathjax="cdn",
                config={
                    "modeBarButtonsToAdd": [
                        "v1hovermode",
                        "hovercompare",
                        "toggleSpikelines",
                    ]
                },
            )
        else:
            return fig

    def plot(
        self,
        plot_type="distribution",
        backend="matplotlib",
        output_plotly=False,
        ax=None,
        legend=True,
        title="",
    ):
        """
        Method to select the plot type and backend

        Parameters
        ----------
        plot_type : str, optional
            'distribution' or 'pC' (default is distribution)
        backend : str, optional
            'matplotlib' or 'plotly' (default is matplotlib)
        output_plotly : bool, optional
            If backend is plotly, generates a html file with the chosen
            plot type. Ignored if backend is matplotlib.
            If false, the function returns a plotly figure (default is False).
        ax : None, optional
            If a Matplotlib axes object is passed, the plot will be shown in it.
            If None, a figure with an axis will be created (default is None)
        legend : bool, optional
            Show legend when backend is Matplotlib (default is True)
        title : str, optional
            Title to be shown above the plot (default is '')

        Raises
        ------
        ValueError
            If invalid type or invalid backend

        Returns
        -------
            A plotly figure or a matplotlib axis.
        """

        if plot_type == "distribution" and backend == "matplotlib":
            return self._distribution_diagram_matplotlib(
                ax=ax, legend=legend, title=title
            )
        elif plot_type == "distribution" and backend == "plotly":
            return self._distribution_diagram_plotly(output_plotly, title)
        elif plot_type == "pC" and backend == "matplotlib":
            return self._pC_diagram_matplotlib(ax=ax, legend=legend, title=title)
        elif plot_type == "pC" and backend == "plotly":
            return self._pC_diagram_plotly(output_plotly, title)
        else:
            raise ValueError("Invalid type and/or plot backend")
