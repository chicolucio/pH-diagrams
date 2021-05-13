import numpy as np 
import matplotlib.pyplot as plt


pH = np.arange(0, 14.1, 0.1)
hydronium_concentration = 10**(-pH)
pKa = 4.76
Ka = 10**(-pKa)

alpha_HA = hydronium_concentration / (hydronium_concentration + Ka)
alpha_A = Ka / (hydronium_concentration + Ka)

plt.plot(pH, alpha_HA)
plt.plot(pH, alpha_A)
plt.show()
