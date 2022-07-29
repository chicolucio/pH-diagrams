import numpy as np

from src.ph_diagrams import Acid

FOLDER = "./tests/golden_files/"

acetic_acid = Acid((4.76,), 0.1)
np.savetxt(
    f"{FOLDER}acetic_acid_alphas.csv", list(zip(*acetic_acid.alpha)), delimiter=","
)
np.savetxt(
    f"{FOLDER}acetic_acid_logc.csv",
    list(zip(*acetic_acid.log_concentrations)),
    delimiter=",",
)

fumaric_acid = Acid((3.02, 4.48), 0.1)  # figure 10.3 Harris
np.savetxt(
    f"{FOLDER}fumaric_acid_alphas.csv", list(zip(*fumaric_acid.alpha)), delimiter=","
)
np.savetxt(
    f"{FOLDER}fumaric_acid_logc.csv",
    list(zip(*fumaric_acid.log_concentrations)),
    delimiter=",",
)

generic_diprotic = Acid((3.0, 8.0), 0.1)  # figure 19 Kahlert & Scholz
np.savetxt(
    f"{FOLDER}gen_diprotic_acid_alphas.csv",
    list(zip(*generic_diprotic.alpha)),
    delimiter=",",
)
np.savetxt(
    f"{FOLDER}gen_diprotic_acid_logc.csv",
    list(zip(*generic_diprotic.log_concentrations)),
    delimiter=",",
)

generic_triprotic = Acid((2, 5, 12), 0.1)
np.savetxt(
    f"{FOLDER}gen_triprotic_acid_alphas.csv",
    list(zip(*generic_triprotic.alpha)),
    delimiter=",",
)
np.savetxt(
    f"{FOLDER}gen_triprotic_acid_logc.csv",
    list(zip(*generic_triprotic.log_concentrations)),
    delimiter=",",
)

# http://ion.chem.usu.edu/~sbialkow/Classes/3600/Overheads/H3A/H3A.html
tyrosine = Acid((2.17, 9.19, 10.47), 0.1)  # exercise 10.34 Harris
np.savetxt(f"{FOLDER}tyrosine_alphas.csv", list(zip(*tyrosine.alpha)), delimiter=",")
np.savetxt(
    f"{FOLDER}tyrosine_logc.csv", list(zip(*tyrosine.log_concentrations)), delimiter=","
)

CrIII_hydrolysis = (
    10 ** (-3.80),
    10 ** (-6.40),
    10 ** (-6.40),
    10 ** (-11.40),
)  # exercise 10.35 Harris
CrIII_pKa = np.log10(CrIII_hydrolysis) * -1
CrIII = Acid(CrIII_pKa, 0.1)
np.savetxt(
    f"{FOLDER}CrIII_hydrolysis_alphas.csv", list(zip(*CrIII.alpha)), delimiter=","
)
np.savetxt(
    f"{FOLDER}CrIII_hydrolysis_logc.csv",
    list(zip(*CrIII.log_concentrations)),
    delimiter=",",
)
