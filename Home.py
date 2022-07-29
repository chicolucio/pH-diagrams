import numpy as np
import streamlit as st

from src.helpers import valid_pka_values
from src.ph_diagrams import Acid
from src.streamlit_functions import (
    CONFIG_PLOTLY,
    TITLE_PREFIX_DISTRIBUTION,
    TITLE_PREFIX_pC,
    find_me_buttons,
    load_css,
    vertical_spacer,
)

st.set_page_config(layout="wide", page_title="pH diagrams", page_icon=":alembic:")

load_css()

PAGE_TEXT_FILE = "pages/01_Home.md"

with open(PAGE_TEXT_FILE) as f:
    content = f.read()

st.markdown(content)

pkas = dict()

with st.sidebar:
    for i in range(1, 5):
        label = "".join(("pKa", str(i)))
        initial_value = 1.0 if i == 1 else 0.0
        pkas[label] = st.slider(label, 0.0, 14.0, initial_value, 0.5)
with st.sidebar:
    conc_options = np.logspace(-5, -1, 5)
    concentration = st.select_slider(
        "concentration", options=conc_options, value=1e-1, key="conc"
    )

input_pkas = pkas.values()

acid = Acid(tuple(valid_pka_values(input_pkas)), concentration)
acid_formula = acid.formulas(output="html")[0]
dist_plot = acid.plot(
    "distribution", "plotly", title="".join((TITLE_PREFIX_DISTRIBUTION, acid_formula))
)
pC_plot = acid.plot("pC", "plotly", title="".join((TITLE_PREFIX_pC, acid_formula)))

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(dist_plot, use_container_width=True, config=CONFIG_PLOTLY)
with col2:
    st.plotly_chart(pC_plot, use_container_width=True, config=CONFIG_PLOTLY)

sites = ("linkedin", "portfolio", "github", "github_sponsors")
links = (
    "flsbustamante",
    "https://franciscobustamante.com.br",
    "chicolucio",
    "chicolucio",
)

columns = st.columns([1, 1, 1.2, 1, 1])

with columns[2]:
    st.info("Follow me for more interactive projects:")
    for site, link in zip(sites, links):
        find_me_buttons(site, link)


# making room for the last slider on mobile...
vertical_spacer(10, sidebar=True)
