import folium
from folium.plugins import MarkerCluster, HeatMap
from utils.data_processing import MAPA_PERIODO_PT

CORES = {
    "Triassic": "#ff9f1c",
    "Jurassic": "#2ec4b6",
    "Cretaceous": "#e71d36",
    "Desconhecido": "#6c757d"
}

CORES_PERIODO = {
    "Triássico": "#ff9f1c",
    "Jurássico": "#2ec4b6",
    "Cretáceo": "#e71d36",
    "Desconhecido": "#6c757d"
}


def criar_mapa(df_mapa, modo_visualizacao):
    lat_media = df_mapa["Latitude"].mean()
    lng_media = df_mapa["Longitude"].mean()

    mapa = folium.Map(
        location=[lat_media, lng_media],
        zoom_start=3,
        tiles="OpenStreetMap"
    )

    if modo_visualizacao == "Marcadores":
        for _, row in df_mapa.iterrows():
            periodo = row.get("Período", "Desconhecido")
            periodo_pt = MAPA_PERIODO_PT.get(periodo, "Desconhecido")
            periodo_ponto = periodo_pt
            cor = CORES_PERIODO.get(periodo_ponto, "#6c757d")

            tooltip_texto = row.get("Táxon", "N/A")

            popup = f"""
<div style="
    font-family: Arial, sans-serif;
    font-size: 13px;
    color: #e6f1ff;
    background-color: #172a45;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid rgba(0,242,255,0.2);
    min-width: 180px;
    line-height: 1.4;
">
    <div style="
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 6px;
        color: #00f2ff;
    ">
        {row.get("Táxon", "N/A")}
    </div>

    <div style="
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        background-color: {cor};
        color: white;
        font-size: 11px;
        margin-bottom: 8px;
    ">
        {periodo_ponto}
    </div>

    <div><strong>Intervalo:</strong> {row.get("Intervalo", "N/A")}</div>
    <div><strong>País:</strong> {row.get("País", "N/A")}</div>
    <div><strong>Localidade:</strong> {row.get("Localidade", "N/A")}</div>
</div>
"""

            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=6,
                tooltip=folium.Tooltip(
                    tooltip_texto,
                    sticky=False,
                    style="""
                        background-color: #172a45;
                        color: #e6f1ff;
                        border: 1px solid rgba(0,242,255,0.2);
                        border-radius: 8px;
                        padding: 6px 10px;
                        font-family: Arial, sans-serif;
                        font-size: 12px;
                    """
                ),
                popup=folium.Popup(popup, max_width=250),
                color="#0a192f",
                weight=1,
                fill=True,
                fill_color=cor,
                fill_opacity=0.85
            ).add_to(mapa)

    elif modo_visualizacao == "Clusters":
        cluster = MarkerCluster().add_to(mapa)
        for _, row in df_mapa.iterrows():
            periodo = row.get("Período", "Desconhecido")
            periodo_pt = MAPA_PERIODO_PT.get(periodo, "Desconhecido")
            periodo_ponto = periodo_pt
            cor = CORES_PERIODO.get(periodo_ponto, "#6c757d")

            tooltip_texto = row.get("Táxon", "N/A")

            popup = f"""
<div style="
    font-family: Arial, sans-serif;
    font-size: 13px;
    color: #e6f1ff;
    background-color: #172a45;
    padding: 10px;
    border-radius: 10px;
    border: 1px solid rgba(0,242,255,0.2);
    min-width: 180px;
    line-height: 1.4;
">
    <div style="
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 6px;
        color: #00f2ff;
    ">
        {row.get("Táxon", "N/A")}
    </div>

    <div style="
        display: inline-block;
        padding: 3px 8px;
        border-radius: 12px;
        background-color: {cor};
        color: white;
        font-size: 11px;
        margin-bottom: 8px;
    ">
        {periodo_ponto}
    </div>

    <div><strong>Intervalo:</strong> {row.get("Intervalo", "N/A")}</div>
    <div><strong>País:</strong> {row.get("País", "N/A")}</div>
    <div><strong>Localidade:</strong> {row.get("Localidade", "N/A")}</div>
</div>
"""

            folium.CircleMarker(
                location=[row["Latitude"], row["Longitude"]],
                radius=6,
                tooltip=folium.Tooltip(
                    tooltip_texto,
                    sticky=False,
                    style="""
                        background-color: #172a45;
                        color: #e6f1ff;
                        border: 1px solid rgba(0,242,255,0.2);
                        border-radius: 8px;
                        padding: 6px 10px;
                        font-family: Arial, sans-serif;
                        font-size: 12px;
                    """
                ),
                popup=folium.Popup(popup, max_width=250),
                color="#0a192f",
                weight=1,
                fill=True,
                fill_color=cor,
                fill_opacity=0.85
            ).add_to(cluster)

    elif modo_visualizacao == "Mapa de Calor":
        heat_data = df_mapa[["Latitude", "Longitude"]].dropna().values.tolist()
        HeatMap(heat_data, radius=18, blur=12, min_opacity=0.3).add_to(mapa)

    if modo_visualizacao != "Mapa de Calor":
        legenda = """
        <div style="
            position: fixed;
            bottom: 40px;
            left: 40px;
            z-index: 9999;
            background-color: white;
            padding: 10px 12px;
            border-radius: 8px;
            border: 1px solid #d9d9d9;
            font-size: 13px;
            color: #222;
        ">
            <div style="font-weight: bold; margin-bottom: 6px;">Períodos</div>
            <div><span style="color:#ff9f1c;">●</span> Triássico</div>
            <div><span style="color:#2ec4b6;">●</span> Jurássico</div>
            <div><span style="color:#e71d36;">●</span> Cretáceo</div>
            <div><span style="color:#6c757d;">●</span> Desconhecido</div>
        </div>
        """

        mapa.get_root().html.add_child(folium.Element(legenda))
    return mapa
