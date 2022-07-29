import streamlit as st

from src.streamlit_functions import find_me_buttons, github_avatar_link, load_css

st.set_page_config(
    layout="centered", page_title="pH Diagrams - About", page_icon=":alembic:"
)

load_css()

sites = ("linkedin", "github", "portfolio", "github_sponsors")
links_francisco = (
    "flsbustamante",
    "chicolucio",
    "https://franciscobustamante.com.br",
    "chicolucio",
)
links_helena = ("helenabenevenuto", "helenabenevenuto")
links_natasha = ("natashaosouza", "natashaosouza")

columns_main = st.columns(3)

with columns_main[1]:
    st.image(github_avatar_link(23560423))

st.header("Francisco Bustamante")
st.success("A chemist working with Data Science and Python Programming")

columns_extra = st.columns(4)
for column, site, link in zip(columns_extra, sites, links_francisco):
    with column:
        find_me_buttons(site, link)

st.markdown("---")

columns_collaborator_1 = st.columns(3)
with columns_collaborator_1[0]:
    st.image(github_avatar_link(79546434))
    st.subheader("Helena Benevenuto")
    st.info("Chemistry student")
    for site, link in zip(sites, links_helena):
        find_me_buttons(site, link)

with columns_collaborator_1[2]:
    st.image(github_avatar_link(86806710))
    st.subheader("Natasha Souza")
    st.info("Chemistry student")
    for site, link in zip(sites, links_natasha):
        find_me_buttons(site, link)
