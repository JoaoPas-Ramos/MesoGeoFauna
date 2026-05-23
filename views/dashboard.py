import streamlit as st
import pandas as pd
import requests
from streamlit.components.v1 import html

from services.pbdb_service import buscar_ocorrencias, buscar_sugestoes_taxon
from utils.data_processing import (
    preparar_dados,
    classificar_periodo,
    gerar_resumo_intervalos,
    MAPA_PERIODO_PT
)
from components.map_component import criar_mapa
from components.chart_component import criar_grafico
from styles.theme import carregar_css, CARD_BG, SECONDARY_TURQUOISE, TEXT_WHITE

st.set_page_config(page_title="MesoGeofauna", layout="wide")
st.markdown(carregar_css(), unsafe_allow_html=True)

PERIODOS = {
    "Todos": "Mesozoic",
    "Triássico": "Triassic",
    "Jurássico": "Jurassic",
    "Cretáceo": "Cretaceous"
}

@st.cache_data(show_spinner=False)
def obter_ocorrencias(busca_taxon, limite_registros, intervalo):
    return buscar_ocorrencias(busca_taxon, limite_registros, intervalo)

@st.cache_data(show_spinner=False)
def obter_sugestoes_taxon(termo, limite=200):
    return buscar_sugestoes_taxon(termo, limite)

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-brand">
            <h1>Meso<span>Geofauna</span></h1>
        </div>
        <div class="sidebar-text">Explorador paleobiogeográfico do Mesozoico</div>
        <div class="sidebar-section-title">Filtros</div>
        """,
        unsafe_allow_html=True
    )

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
    limite = st.slider("Quantidade de registros", min_value=10, max_value=200, value=50)
    periodo = st.radio("Período do Mesozoico", list(PERIODOS.keys()), index=0)

intervalo_api = PERIODOS[periodo]

try:
    with st.spinner("Consultando Paleobiology Database..."):
        data = obter_ocorrencias(busca, limite, intervalo_api)
except requests.exceptions.RequestException as e:
    st.error(f"Erro na requisição à PBDB: {e}")
    st.stop()

records = data.get("records", [])
if not records:
    st.warning("Nenhum registro foi encontrado para os filtros informados.")
    st.stop()

df_limpo = preparar_dados(records)

with st.sidebar:
    paises_disponiveis = ["Todos"]
    if "País" in df_limpo.columns:
        paises_validos = sorted(df_limpo["País"].dropna().astype(str).unique().tolist())
        paises_disponiveis += paises_validos

    filtro_pais = st.selectbox("Filtrar por país", paises_disponiveis)
    filtro_localidade = st.text_input("Filtrar por localidade", placeholder="Ex: Bahariya")

    modo_visualizacao = st.selectbox(
        "Tipo de Visualização",
        [
            "Marcadores",
            "Clusters",
            "Mapa de Calor"
        ]
    )

df_filtrado = df_limpo.copy()

if filtro_pais != "Todos" and "País" in df_filtrado.columns:
    df_filtrado = df_filtrado[df_filtrado["País"].astype(str) == filtro_pais]

if filtro_localidade and "Localidade" in df_filtrado.columns:
    df_filtrado = df_filtrado[
        df_filtrado["Localidade"].astype(str).str.contains(filtro_localidade, case=False, na=False)
    ]

df_mapa = df_filtrado.dropna(subset=["Latitude", "Longitude"]).copy()
df_mapa["Período"] = df_mapa["Idade inicial (Ma)"].apply(classificar_periodo)
df_mapa = df_mapa.head(1000)

grafico_df = gerar_resumo_intervalos(df_filtrado)
grafico_df["Período_PT"] = grafico_df["Período"].map(MAPA_PERIODO_PT).fillna("Desconhecido")

taxa_unicos = df_filtrado["Táxon"].nunique(dropna=True)
paises_unicos = df_filtrado["País"].nunique(dropna=True)
idade_mais_antiga = df_filtrado["Idade inicial (Ma)"].max() if not df_filtrado["Idade inicial (Ma)"].dropna().empty else None

with st.sidebar:
    if not df_filtrado.empty and busca:
        primeiro = df_filtrado.iloc[0]
        latitude_resumo = primeiro.get("Latitude", None)
        longitude_resumo = primeiro.get("Longitude", None)

        if pd.notna(latitude_resumo) and pd.notna(longitude_resumo):
            coordenadas = f"{latitude_resumo:.2f}, {longitude_resumo:.2f}"
        else:
            coordenadas = "N/A"

        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-card-header">
                    <h3>Resumo do resultado</h3>
                </div>
                <div class="info-card-body">
                    <p><strong>Táxon:</strong> {primeiro.get("Táxon", "N/A")}</p>
                    <p><strong>Intervalo:</strong> {primeiro.get("Intervalo", "N/A")}</p>
                    <p><strong>Localidade:</strong> {primeiro.get("Localidade", "N/A")}</p>
                    <p><strong>País:</strong> {primeiro.get("País", "N/A")}</p>
                    <p><strong>Coordenadas:</strong> {coordenadas}</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('<div class="app-title">Dashboard Paleobiogeográfico do Mesozoico</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Exploração interativa de ocorrências fósseis com dados da Paleobiology Database</div>',
    unsafe_allow_html=True
)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Registros encontrados", len(df_filtrado))
m2.metric("Registros com coordenadas", len(df_mapa))
m3.metric("Táxons únicos", taxa_unicos)
m4.metric("Países únicos", paises_unicos)

st.markdown(
    """
    <div class="map-panel">
        <div class="map-title">Distribuição espacial de ocorrências fósseis</div>
        <div class="map-subtitle">Visualização central do dashboard para análise paleobiogeográfica das ocorrências recuperadas.</div>
    """,
    unsafe_allow_html=True
)

if not df_mapa.empty:
    mapa = criar_mapa(df_mapa, modo_visualizacao)
    html(mapa._repr_html_(), height=560)
else:
    st.info("Não há coordenadas disponíveis para exibir no mapa.")

st.markdown("</div>", unsafe_allow_html=True)

idade_texto = f"{idade_mais_antiga:.1f} Ma" if idade_mais_antiga is not None else "N/A"

st.markdown(
    f"""
    <div class="bottom-strip">
        <div class="bottom-strip-title">Faixa temporal</div>
        <div class="bottom-strip-text">Período selecionado: <strong>{periodo}</strong> | Registro mais antigo no conjunto atual: <strong>{idade_texto}</strong></div>
        <div>
            <span class="timeline-badge">Triássico</span>
            <span class="timeline-badge">Jurássico</span>
            <span class="timeline-badge">Cretáceo</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col_grafico, col_tabela = st.columns([1, 1.25])

with col_grafico:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Ocorrências por intervalo</div>', unsafe_allow_html=True)

    fig = criar_grafico(grafico_df)
    if fig is not None:
        fig.update_layout(
            height=420,
            margin=dict(l=20, r=20, t=10, b=20),
            paper_bgcolor=CARD_BG,
            plot_bgcolor=CARD_BG,
            font=dict(color=TEXT_WHITE),
            legend=dict(
                title="Período",
                bgcolor=CARD_BG,
                font=dict(color=TEXT_WHITE)
            ),
            xaxis=dict(
                title="Quantidade de ocorrências",
                showgrid=True,
                gridcolor="rgba(230, 241, 255, 0.08)",
                zeroline=False
            ),
            yaxis=dict(
                title="Intervalo geológico",
                showgrid=False
            )
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Não há dados suficientes para gerar o gráfico por intervalo.")

    st.markdown("</div>", unsafe_allow_html=True)

with col_tabela:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown('<div class="panel-title">Tabela de registros</div>', unsafe_allow_html=True)

    colunas_tabela = [
        col for col in [
            "Táxon",
            "Nome identificado",
            "Intervalo",
            "Idade inicial (Ma)",
            "Idade final (Ma)",
            "País",
            "Localidade",
            "Latitude",
            "Longitude"
        ] if col in df_limpo.columns
    ]

    df_exibicao = df_filtrado[colunas_tabela].copy()
    if "Idade inicial (Ma)" in df_exibicao.columns:
        df_exibicao = df_exibicao.sort_values(by="Idade inicial (Ma)", ascending=False, na_position="last")

    st.dataframe(df_exibicao, use_container_width=True, hide_index=True, height=420)
    st.markdown("</div>", unsafe_allow_html=True)