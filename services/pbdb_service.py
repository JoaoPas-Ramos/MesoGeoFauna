import requests

BASE_URL = "https://paleobiodb.org/data1.2/occs/list.json"
TAXA_URL = "https://paleobiodb.org/data1.2/taxa/auto.json"


def buscar_ocorrencias(busca_taxon, limite, intervalo):
    params = {
        "interval": intervalo,
        "show": "coords,ident,time,loc",
        "limit": limite
    }

    if busca_taxon:
        params["base_name"] = busca_taxon

    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def buscar_sugestoes_taxon(termo, limite=10):
    if not termo or len(termo.strip()) < 3:
        return []

    params = {
        "name": termo.strip(),
        "limit": limite
    }

    response = requests.get(TAXA_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()
    records = data.get("records", [])

    sugestoes = []
    for item in records:
        nome = item.get("nam")
        rank = item.get("rnk")
        ocorrencias = item.get("noc")

        if nome:
            if rank and ocorrencias is not None:
                rotulo = f"{nome} ({rank}, {ocorrencias} ocorrências)"
            elif rank:
                rotulo = f"{nome} ({rank})"
            else:
                rotulo = nome

            sugestoes.append({"nome": nome, "rotulo": rotulo})

    return sugestoes
