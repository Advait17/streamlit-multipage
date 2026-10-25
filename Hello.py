import streamlit as st

st.set_page_config(
    page_title="Data Demo Hub",
    page_icon="📊",
    layout="wide",
)

# ---- Header ---------------------------------------------------------------
st.title("📊 Data Demo Hub")
st.caption("A multipage Streamlit app · 36104 Data Visualisation and Narratives")

st.markdown(
    "This app brings together three small interactive demos, each on its own page. "
    "Use the **sidebar on the left** to switch between them."
)

st.divider()

# ---- Demo cards -------------------------------------------------------------
st.subheader("What's inside")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("### 📈 Plotting")
        st.write(
            "An animated line chart that grows in real time, "
            "with a progress bar in the sidebar."
        )
        st.caption("Shows: `st.line_chart`, live updates")

with col2:
    with st.container(border=True):
        st.markdown("### 🌍 Mapping")
        st.write(
            "A 3D map of San Francisco bike rentals and BART "
            "stations. Toggle the map layers in the sidebar."
        )
        st.caption("Shows: `st.pydeck_chart`, layered maps")

with col3:
    with st.container(border=True):
        st.markdown("### 📋 DataFrame")
        st.write(
            "UN agricultural production by country. Pick countries "
            "to compare them in a table and an area chart."
        )
        st.caption("Shows: `st.multiselect`, Altair charts")

st.divider()

# ---- How it works -----------------------------------------------------------
st.subheader("How this app is built")

left, right = st.columns([1, 1])

with left:
    st.markdown(
        """
        Streamlit builds the sidebar navigation automatically from the
        project's folder structure:

        - `Hello.py` is the **entrypoint** and this home page
        - every script in `pages/` becomes its own page
        - numbers at the start of file names set the page order
        """
    )

with right:
    st.code(
        """streamlit-multipage/
├── Hello.py
├── requirements.txt
└── pages/
    ├── 1_Plotting_Demo.py
    ├── 2_Mapping_Demo.py
    └── 3_DataFrame_Demo.py""",
        language="text",
    )

# ---- Sidebar ----------------------------------------------------------------
st.sidebar.success("Pick a demo above")