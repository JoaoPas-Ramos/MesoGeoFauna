import streamlit as st
import plotly.express as px

from services.pbdb_service import buscar_ocorrencias, buscar_sugestoes_taxon
from utils.data_processing import preparar_dados, classificar_periodo
from styles.theme import carregar_css

st.set_page_config(page_title="MesoGeofauna", layout="wide")
st.markdown(carregar_css(), unsafe_allow_html=True)

st.title("Análise Temporal")

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

df["Período"] = df["Idade inicial (Ma)"].apply(classificar_periodo)

df_tempo = df.dropna(subset=["Idade inicial (Ma)"]).copy()

df_tempo["Idade arredondada"] = df_tempo["Idade inicial (Ma)"].round(0)

timeline = (
    df_tempo["Idade arredondada"]
    .value_counts()
    .reset_index()
)

timeline.columns = ["Idade (Ma)", "Ocorrências"]
timeline = timeline.sort_values("Idade (Ma)", ascending=False)

fig = px.line(
    timeline,
    x="Idade (Ma)",
    y="Ocorrências",
    markers=True
)

fig.update_layout(
    paper_bgcolor="#172a45",
    plot_bgcolor="#172a45",
    font=dict(color="#e6f1ff")
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("Interpretação")

st.write(f"""
Total de registros: {len(df)}

A idade com maior ocorrência é: {int(timeline.iloc[0]['Idade (Ma)'])} Ma

Isso indica uma maior concentração de registros fósseis nesse intervalo de idade.
""")