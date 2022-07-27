import streamlit as st
import numpy as np
from src.ph_diagram import Acid
from src.helpers import valid_pka_values
from src.streamlit_functions import find_me_buttons, load_css

st.set_page_config(layout='wide',
                   page_title='pH diagrams',
                   page_icon=':alembic:')

load_css()

PAGE_TEXT_FILE = 'pages/01_Home.md'
TITLE_PREFIX_DISTRIBUTION = 'Distribution diagram - '
TITLE_PREFIX_pC = 'pC diagram - '

with open(PAGE_TEXT_FILE) as f:
    content = f.read()

st.markdown(content)

slider_grid = st.columns(4)

# TODO 0 is a valid pKa value. Change behaviour to accept this value (one zero)
pka1 = slider_grid[0].slider('pKa1', 0.0, 14.0, 0.0, 0.5)
pka2 = slider_grid[1].slider('pKa2', 0.0, 14.0, 0.0, 0.5)
pka3 = slider_grid[2].slider('pKa3', 0.0, 14.0, 0.0, 0.5)
conc_options = np.logspace(-5, -1, 5)
concentration = slider_grid[3].select_slider('concentration',
                                             options=conc_options,
                                             value=1E-1)

input_pkas = (pka1, pka2, pka3)

acid = Acid(tuple(valid_pka_values(input_pkas)), concentration)
acid_formula = acid.formulas(output='html')[0]
dist_plot = acid.plot('distribution', 'plotly',
                      title=''.join((TITLE_PREFIX_DISTRIBUTION, acid_formula)))
pC_plot = acid.plot('pC', 'plotly',
                    title=''.join((TITLE_PREFIX_pC, acid_formula)))

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(dist_plot, use_container_width=True)
with col2:
    st.plotly_chart(pC_plot, use_container_width=True)

sites = ('linkedin', 'portfolio', 'github', 'github_sponsors')
links = ('flsbustamante', 'https://franciscobustamante.com.br', 'chicolucio',
         'chicolucio')

columns = st.columns([1, 1, 1.2, 1, 1])

with columns[2]:
    st.info('Follow me for more interactive projects:')
    for site, link in zip(sites, links):
        find_me_buttons(site, link)
