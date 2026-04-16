import pandas as pd

COLUNAS = [
    "oid", "idn", "tna", "rnk", "oei",
    "eag", "lag", "lat", "lng", "cc2", "ggc"
]

INTERVALOS_MESOZOICOS = [
    "Induan", "Olenekian", "Anisian", "Ladinian", "Carnian", "Norian", "Rhaetian",
    "Hettangian", "Sinemurian", "Pliensbachian", "Toarcian", "Aalenian", "Bajocian",
    "Bathonian", "Callovian", "Oxfordian", "Kimmeridgian", "Tithonian",
    "Berriasian", "Valanginian", "Hauterivian", "Barremian", "Aptian", "Albian",
    "Cenomanian", "Turonian", "Coniacian", "Santonian", "Campanian", "Maastrichtian"
]

MAPA_PERIODO_PT = {
    "Triassic": "Triássico",
    "Jurassic": "Jurássico",
    "Cretaceous": "Cretáceo",
    "Desconhecido": "Desconhecido"
}

CORES_PERIODO = {
    "Triassic": "#ff9f1c",
    "Jurassic": "#2ec4b6",
    "Cretaceous": "#e71d36",
    "Desconhecido": "#6c757d"
}

CORES_PERIODO_PT = {
    MAPA_PERIODO_PT[periodo]: cor
    for periodo, cor in CORES_PERIODO.items()
}


def preparar_dados(records):
    df = pd.DataFrame(records)
    df = df.reindex(columns=COLUNAS).copy()

    df.rename(columns={
        "oid": "ID",
        "idn": "Nome identificado",
        "tna": "Táxon",
        "rnk": "Rank",
        "oei": "Intervalo",
        "eag": "Idade inicial (Ma)",
        "lag": "Idade final (Ma)",
        "lat": "Latitude",
        "lng": "Longitude",
        "cc2": "País",
        "ggc": "Localidade"
    }, inplace=True)

    df["Latitude"] = pd.to_numeric(df["Latitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
    df["Idade inicial (Ma)"] = pd.to_numeric(df["Idade inicial (Ma)"], errors="coerce")
    df["Idade final (Ma)"] = pd.to_numeric(df["Idade final (Ma)"], errors="coerce")

    return df


def classificar_periodo(idade):
    if pd.isna(idade):
        return "Desconhecido"
    if idade >= 201.3:
        return "Triassic"
    if idade >= 145.0:
        return "Jurassic"
    return "Cretaceous"


def gerar_resumo_intervalos(df):
    if "Intervalo" not in df.columns or df["Intervalo"].dropna().empty:
        return pd.DataFrame(columns=["Intervalo", "Ocorrências", "Período"])

    df_intervalos = df.dropna(subset=["Intervalo"]).copy()
    df_intervalos["Período"] = df_intervalos["Idade inicial (Ma)"].apply(classificar_periodo)

    resumo = (
        df_intervalos
        .groupby(["Intervalo", "Período"], dropna=False)
        .size()
        .reset_index(name="Ocorrências")
    )

    ordem_intervalos = {intervalo: i for i, intervalo in enumerate(INTERVALOS_MESOZOICOS)}
    resumo["Ordem"] = resumo["Intervalo"].map(ordem_intervalos).fillna(999)
    resumo = resumo.sort_values(["Ordem", "Ocorrências"], ascending=[True, False])

    intervalos_top = (
        resumo.groupby("Intervalo", as_index=False)["Ocorrências"]
        .sum()
        .sort_values(["Intervalo"], key=lambda s: s.map(ordem_intervalos).fillna(999))
        .head(12)["Intervalo"]
        .tolist()
    )

    resumo = resumo[resumo["Intervalo"].isin(intervalos_top)].copy()
    resumo = resumo.sort_values(["Ordem", "Ocorrências"], ascending=[False, True])

    return resumo
