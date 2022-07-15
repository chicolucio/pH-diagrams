import streamlit as st
import numpy as np
from ph_diagram import Acid, valid_pka_values

st.set_page_config(layout='wide')
st.title('pH diagrams')

slider_grid = st.columns(4)

pka1 = slider_grid[0].slider('pKa1', 0.0, 14.0, 0.0, 0.5)
pka2 = slider_grid[1].slider('pKa2', 0.0, 14.0, 0.0, 0.5)
pka3 = slider_grid[2].slider('pKa3', 0.0, 14.0, 0.0, 0.5)
conc_options = np.logspace(-5, -1, 5)
concentration = slider_grid[3].select_slider('concentration',
                                             options=conc_options,
                                             value=1E-1)

input_pkas = (pka1, pka2, pka3)

acid = Acid(tuple(valid_pka_values(input_pkas)), concentration)
dist_plot = acid.plot('distribution', 'plotly')
pC_plot = acid.plot('pC', 'plotly')

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(dist_plot, use_container_width=True)
with col2:
    st.plotly_chart(pC_plot, use_container_width=True)
