import streamlit as st
from styles.theme import carregar_css

st.set_page_config(page_title="MesoGeofauna", layout="wide")
st.markdown(carregar_css(), unsafe_allow_html=True)

st.markdown('<div class="app-title">MesoGeofauna</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Dashboard interativo para análise paleobiogeográfica baseado na Paleobiology Database</div>',
    unsafe_allow_html=True
)

st.markdown("---")

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("### Sobre o sistema")
    st.write("""
O **MesoGeofauna** é uma ferramenta interativa para exploração e análise de ocorrências fósseis do Mesozoico.

A aplicação permite visualizar dados paleontológicos em mapas, gráficos e tabelas, facilitando a compreensão da distribuição espacial e temporal de diferentes táxons.
""")

    st.markdown("### Como usar")
    st.write("""
1. Acesse o **Dashboard** na sidebar para explorar os dados gerais.
2. Utilize os filtros para refinar a busca.
3. Acesse as páginas de **Análise** para obter interpretações específicas.
""")

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color: rgba(230, 241, 255, 0.6); font-size: 0.9rem;">
        Desenvolvido como Trabalho de Conclusão de Curso — Análise e Desenvolvimento de Sistemas
    </div>
    """,
    unsafe_allow_html=True
)
