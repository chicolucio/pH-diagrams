# Acid-base diagrams

Table of contents:
1. [How to use](#how-to-use)
2. [Fractional composition diagrams](#fractional-composition-diagrams)
3. [pH-logc diagrams](#ph-logc-diagrams)


## How to use

On the sidebar of the home page, move the sliders to choose the value of each
$pK_a$. The aim of this interactive site is educational, so, to make things
simple, the following simplifications were made:

- only values between 0 and 14 are available. To be clear, it is perfectly
  possible to have negative $pK_a$ values and values greater than 14. But,
  for most cases this range is enough.
- the increase step is set to 0.5 on $pK_a$ sliders, and the concentration
  slider has logarithm scale, changing one order of magnitude each time.
- each added $pK_a$ is expected to be greater than or equal to the previous one.
  This is usually the case, but [some exceptions](https://en.wikipedia.org/wiki/Acid_dissociation_constant#Polyprotic_acids)
  are known which are commonly related with major changes in structure.
- only 4 $pK_a$ sliders available.

The source code under the hood of this website has none of the limitations above.
Custom pH and $pK_a$ ranges, arbitrary precision, unordered values... the
source code allows unlimited options.
The [source code can be found here](https://github.com/chicolucio/pH-diagrams)
with instructions to use.

## Fractional composition diagrams

*Fractional composition diagrams*, also known as *species distribution diagram*
or *speciation diagrams*, are used to visualize the solution composition of a
mono- or polyprotic acid as a function of pH.

The name comes from the fact that the vertical axis is the fraction of each
form of the acid. Considering a monoprotic acid $HA$, the forms are $HA$ and
$A^-$, with the following fractions:

$$
\begin{align*}
  \alpha_{HA} &= \frac{[H^+]}{[H^+] + K_a} \\
  \alpha_{A^-} &= \frac{K_a}{[H^+] + K_a} \\
\end{align*}
$$

Of course, the sum must be 1:

$$
\alpha_{HA} + \alpha_{A^-} = 1
$$

The general form of $\alpha$ for a polyprotic acid $H_nA$ is

$$
\begin{align*}
  \alpha_{H_nA}     &= \frac{[H^+]^n}{D} \\
  \alpha_{H_{n-1}A} &= \frac{K_1 [H^+]^{n-1}}{D} \\
  \alpha_{H_{n-j}A} &= \frac{K_1 K_2 \cdots K_j [H^+]^{n-j}}{D} \\
\end{align*}
$$

where $D = [H^+]^n + K_1 [H^+]^{n-1} + K_1 K_2 [H^+]^{n-2} + \cdots + K_1 K_2 K_3 \cdots K_n$.

### Examples

Let's see some examples. All diagrams are interactive, so one can zoom in and
out. First, the monoprotic acid, acetic acid:

![acetic acid]()

We can see the regions in which each form dominates. And it is easier to
understand thumb rules like *the buffer range is $pH = pKa \pm 1$*. The diagram
shows that around 4.76, the acetic acid $pK_a$, appreciable concentrations of
both species are present. Since buffers aim to maintain a more or less constant
pH, it is crucial to have both species.

The Henderson-Hasselbach equation below can be used to estimate the pH of a
buffer solution by approximating the actual concentration ratio as the ratio
of the analytical concentrations. Since the ratio is inside a logarithm, if one
species concentration is 10 times greater/lower than the other, we have the
$\pm 1$ boundaries:

$$
pH = pK_a + \log \frac{[\text{base}]}{[\text{acid}]}
$$

The following diagram is for fumaric acid, a diprotic acid. The $pK_a$ values
for this acid are 3.02 and 4.48. Because the values are not separated very much,
the fraction of $HA^-$ never gets very close to unity.

![fumaric acid]()

As a final example, we have the diagram for citric acid, a triprotic acid. The
$pK_a$ values are 3.13, 4.76 and 6.40. As can be seen, the constants are not
far apart, so only $H_3A$ and $A^{3-}$ have dominance regions with their
fractions getting close to unity.

![citric acid]()

## pH-logc diagrams

pH-$\log c_i$ diagrams present the interrelations between the logarithm of
all equilibrium concentrations $c$ of the species $i$ and the pH value of the
solution.

They make it possible to find the approximate pH of solutions of acids and bases
and buffers without any math calculations. These diagrams can also be used to
construct titration curves to extract the most important data, such as pH at the
equilibrium point.

For a given form $i$ of an acid with formal concentration $C$, the $\log c_i$
is simply:

$$
\log c_i = \log(\alpha_i C)
$$

### Examples

Let's see the diagrams for the same acids shown in the previous section.
All the diagrams consider a formal concentration of $0.1 \text{mol} \cdot \ell^{-1}$.
Starting with acetic acid ($pK_a = 4.76$):

![acetic acid logc]()

As can be seen, there are straight dotted lines crossing the diagram. These
are the $H^+$ and $OH^-$ log concentration lines. They are useful as references.

It is easy to see that the formal concentration is $0.1 \text{mol} \cdot \ell^{-1}$
because of the horizontal straight lines on low and high pH ranges locate
vertically in $-1.0$.
The diagonal parts of the lines have slopes of equal magnitude but opposite
sign. The slopes are $\pm 1$, corresponding to the slopes of the $[H^+]$ and
$[OH^-]$ lines.

The crossing point corresponds to the condition $[HA] = [A^-]$, when the pH is
the same as the $pK_a$. For a formal concentration $C$, in this point each
species concentration must be $\frac{C}{2}$. Mathematically,
$\log 0.5 \approx 0.3$, so one can see that the vertical location of the
crossing point is $\approx -1.3$.

Except for the special cases of extremely dilute solutions or very weak acids
in which the autoprotolysis of water is a major contributor to the hydronium
concentration, for an acid in pure water the relation $[H_3O^+] \approx [A^-]$
will hold. This way, pH can be found as the intersection between these curves
in the diagram. For the acetic acid diagram above, this intersection happens
at pH $\approx 2.88$.

An analogue reasoning can be used to find the pH of a solution of the
conjugate base in pure water. Consider a solution of sodium acetate in water.
As long as we can neglect the contribution of hydroxide ions from the
autoprotolysis of the solvent, the relation $[HA] \approx [OH^-]$ will hold.
The equivalence of these two concentrations corresponds to the intersection
between these curves in the diagram. For the acetic acid diagram above, this
intersection happens at pH $\approx 8.88$.

The same interpretation of the above monoprotic acid diagram can be extended
to polyprotic acids.
The following diagram is for fumaric acid, a diprotic acid. The $pK_a$ values
for this acid are 3.02 and 4.48.

![fumaric acid logc]()

Zooming in, one can see that $HA^-$ does not get to $\log C \approx -1.0$.
Compare with the fractional composition diagram above.

As a final example, we have the diagram for citric acid, a triprotic acid, below.
The $pK_a$ values are 3.13, 4.76 and 6.40. Again, compare with the fractional
composition diagram in the previous section.

![citric acid logc]()
