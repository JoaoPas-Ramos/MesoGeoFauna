import streamlit as st
import plotly.express as px

from services.pbdb_service import buscar_ocorrencias, buscar_sugestoes_taxon
from utils.data_processing import preparar_dados
from styles.theme import carregar_css

st.set_page_config(page_title="MesoGeofauna", layout="wide")
st.markdown(carregar_css(), unsafe_allow_html=True)

st.title("Análise Geográfica")

PERIODOS = {
    "Todos": "Mesozoic",
    "Triássico": "Triassic",
    "Jurássico": "Jurassic",
    "Cretáceo": "Cretaceous"
}

@st.cache_data(show_spinner=False)
def obter_sugestoes_taxon(termo, limite=200):
    return buscar_sugestoes_taxon(termo, limite)

    
sugestoes = obter_sugestoes_taxon("")

opcoes_taxon = ["Todos os táxons"]
mapa_rotulos = {"Todos os táxons": ""}

for item in sugestoes:
    opcoes_taxon.append(item["rotulo"])
    mapa_rotulos[item["rotulo"]] = item["nome"]

taxon_escolhido_rotulo = st.selectbox(
    "Busca de táxon",
    opcoes_taxon,
    index=None,
    accept_new_options=True,
    placeholder=""
)

busca = mapa_rotulos.get(
    taxon_escolhido_rotulo,
    taxon_escolhido_rotulo
)

limite = st.slider("Quantidade", 10, 200, 50)
periodo = st.selectbox("Período", list(PERIODOS.keys()))

intervalo_api = PERIODOS[periodo]

with st.spinner("Consultando dados..."):
    data = buscar_ocorrencias(busca, limite, intervalo_api)

records = data.get("records", [])

if not records:
    st.warning("Nenhum dado encontrado.")
    st.stop()

df = preparar_dados(records)

df_geo = df.dropna(subset=["País"])

ranking = (
    df_geo["País"]
    .value_counts()
    .reset_index()
)

ranking.columns = ["País", "Ocorrências"]
ranking = ranking.head(10)

fig = px.bar(
    ranking,
    x="Ocorrências",
    y="País",
    orientation="h"
)

fig.update_layout(
    paper_bgcolor="#172a45",
    plot_bgcolor="#172a45",
    font=dict(color="#e6f1ff")
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretação")

st.write(f"""
Total de países com registros: {df_geo['País'].nunique()}

O país com maior número de ocorrências é: {ranking.iloc[0]['País']}

Isso indica concentração significativa de registros fósseis nessa região.
""")