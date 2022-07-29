import streamlit as st

from src.ph_diagrams import Acid
from src.streamlit_functions import (
    CONFIG_PLOTLY,
    TITLE_PREFIX_DISTRIBUTION,
    TITLE_PREFIX_pC,
    load_css,
    text_from_markdown,
)

st.set_page_config(layout="centered", page_title="pH Diagrams", page_icon=":alembic:")

load_css()

PAGE_TEXT_FILE = "pages/02_Chemistry.md"

acetic_acid = Acid((4.76,), 0.1)
fumaric_acid = Acid((3.02, 4.48), 0.1)
citric_acid = Acid((3.13, 4.76, 6.39), 0.1)

content_parts = text_from_markdown(PAGE_TEXT_FILE)

st.markdown("".join(content_parts[0]))
st.plotly_chart(
    acetic_acid.plot(
        backend="plotly", title="".join((TITLE_PREFIX_DISTRIBUTION, "Acetic acid"))
    ),
    use_container_width=True,
    config=CONFIG_PLOTLY,
)

st.markdown("".join(content_parts[1]))
st.plotly_chart(
    fumaric_acid.plot(
        backend="plotly", title="".join((TITLE_PREFIX_DISTRIBUTION, "Fumaric acid"))
    ),
    use_container_width=True,
    config=CONFIG_PLOTLY,
)

st.markdown("".join(content_parts[2]))
st.plotly_chart(
    citric_acid.plot(
        backend="plotly", title="".join((TITLE_PREFIX_DISTRIBUTION, "Citric acid"))
    ),
    use_container_width=True,
    config=CONFIG_PLOTLY,
)

st.markdown("".join(content_parts[3]))
st.plotly_chart(
    acetic_acid.plot(
        backend="plotly",
        plot_type="pC",
        title="".join((TITLE_PREFIX_pC, "Acetic acid")),
    ),
    use_container_width=True,
    config=CONFIG_PLOTLY,
)

st.markdown("".join(content_parts[4]))
st.plotly_chart(
    fumaric_acid.plot(
        backend="plotly",
        plot_type="pC",
        title="".join((TITLE_PREFIX_pC, "Fumaric acid")),
    ),
    use_container_width=True,
    config=CONFIG_PLOTLY,
)

st.markdown("".join(content_parts[5]))
st.plotly_chart(
    citric_acid.plot(
        backend="plotly",
        plot_type="pC",
        title="".join((TITLE_PREFIX_pC, "Citric acid")),
    ),
    use_container_width=True,
    config=CONFIG_PLOTLY,
)
