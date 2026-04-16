import plotly.express as px
from utils.data_processing import CORES_PERIODO_PT


def criar_grafico(df):
    if df.empty:
        return None

    fig = px.bar(
        df,
        x="Ocorrências",
        y="Intervalo",
        color="Período_PT",
        orientation="h",
        text="Ocorrências",
        color_discrete_map=CORES_PERIODO_PT,
        category_orders={
            "Período_PT": ["Triássico", "Jurássico", "Cretáceo", "Desconhecido"]
        }
    )

    fig.update_traces(textposition="outside", cliponaxis=False)
    return fig
