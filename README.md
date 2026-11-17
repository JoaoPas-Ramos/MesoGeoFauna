# MesoGeofauna

Dashboard em Python e Streamlit para explorar dados de ocorrências fósseis da [Paleobiology Database](https://paleobiodb.org/). O projeto faz parte do TCC de Análise e Desenvolvimento de Sistemas no IFBA.

## O que você pode explorar

- Consulte ocorrências na API da PBDB, escolha um táxon e ajuste o limite de registros.
- Filtre por país e alterne entre marcadores, agrupamentos e mapa de calor no Dashboard.
- Use as páginas de análise temporal e geográfica para navegar pelos registros disponíveis.

## Como o dashboard funciona

O serviço em `services/pbdb_service.py` consulta a PBDB e recebe os registros em JSON. O módulo `utils/data_processing.py` organiza os dados com Pandas. As páginas em `views/` usam os componentes de mapas Folium e gráficos Plotly de `components/` para apresentar o recorte escolhido. `app.py` configura a navegação do Streamlit.

## Rodar localmente

Na raiz do repositório, com Python 3.14 no Windows (PowerShell):

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m streamlit run app.py
```

No macOS ou Linux, crie o ambiente com `python3 -m venv .venv` e use `.venv/bin/python` nos comandos de instalação e execução. Abra a URL mostrada pelo Streamlit. No Dashboard, busque `Dinosauria`, selecione um táxon e experimente a visualização por agrupamentos.

## Limitações e desenvolvimento

Novas consultas dependem da disponibilidade da PBDB. Os mapas usam coordenadas atuais, e o recorte representa apenas as ocorrências registradas e retornadas pela fonte. O TCC segue em desenvolvimento, com trabalho em análises comparativas, rastreabilidade de filtros e testes automatizados.
