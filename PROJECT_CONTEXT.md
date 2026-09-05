# Contexto durável do projeto MesoGeofauna

Atualizado em 27/08/2026 para preservar decisões acadêmicas e técnicas entre futuras sessões de trabalho.

## Identificação acadêmica

- Autor: João Gabriel Passos Ramos.
- Curso: Análise e Desenvolvimento de Sistemas, IFBA - Campus Santo Antônio de Jesus.
- Orientador: Prof. Me. Samuel Melo.
- Natureza: pré-projeto de TCC, não TCC concluído.
- Área: Engenharia de Software e Visualização de Dados.
- Tema: dashboard web para exploração espaço-temporal de ocorrências fósseis obtidas da Paleobiology Database (PBDB).
- Recorte acadêmico: Dinosauria durante o Mesozoico.
- Público: estudantes, pesquisadores, professores e interessados em paleontologia e paleobiogeografia.

## Regra de evidência

O texto acadêmico foi construído apenas com os arquivos, a fundamentação, a aula metodológica e o código fornecidos pelo autor. Não apresentar como fato científico, requisito confirmado ou funcionalidade implementada aquilo que não estiver sustentado por essas fontes ou pelo repositório.

## Estado atual do sistema

O protótipo é uma aplicação multipágina em Python e Streamlit.

- `app.py`: navegação entre Home, Dashboard, Análise Temporal e Análise Geográfica.
- `services/pbdb_service.py`: acesso aos endpoints de ocorrências e sugestões taxonômicas da PBDB.
- `utils/data_processing.py`: seleção e renomeação de campos, conversão numérica, classificação de períodos e resumo por intervalos.
- `components/map_component.py`: mapas Folium com marcadores, agrupamentos e mapa de calor.
- `components/chart_component.py`: gráfico Plotly de ocorrências por intervalo.
- `views/dashboard.py`: filtros, indicadores, mapa, gráfico e tabela.
- `views/analise_temporal.py`: linha baseada na idade inicial arredondada.
- `views/analise_geografica.py`: ranking de países.
- `styles/theme.py`: tema visual.

Tecnologias presentes: Streamlit, Folium, Requests, Pandas e Plotly.

## Funcionalidades existentes

- Consulta de ocorrências da PBDB em JSON.
- Filtros por táxon, período, quantidade, país e localidade.
- Limite selecionável entre 10 e 200 registros.
- Modos cartográficos por marcadores, agrupamentos e calor.
- Indicadores de registros, registros com coordenadas, táxons e países.
- Tabela com identificação, intervalo, idades, localização e coordenadas.
- Gráfico de ocorrências por intervalo.
- Páginas de análise temporal e geográfica.
- Conversão de coordenadas e idades para valores numéricos, preservando entradas incompatíveis como ausentes.
- Cache e tratamento básico de falha ou ausência de resultados.

## Limitações confirmadas

- O mapa usa coordenadas atuais sobre OpenStreetMap; representa a localidade atual da ocorrência ou coleta, não paleogeografia.
- A consulta visível é limitada a 200 registros; contagens não são o total completo da PBDB sem revisão da obtenção.
- A opção sem táxon pode recuperar ocorrências além de Dinosauria; o TCC deve manter o recorte de Dinosauria.
- A análise temporal usa idade inicial arredondada e é apenas descritiva.
- A análise geográfica apresenta ranking de países e usa linguagem de concentração significativa sem teste estatístico.
- Contagens não equivalem a abundância, diversidade real ou significância.
- Ausência de registro não prova ausência biológica.
- Sobreposição geográfica e temporal ampla não prova coexistência.
- O sistema não implementa paleocoordenadas.

## Escopo analítico acordado

Priorizar quatro análises coerentes e avaliáveis:

1. **Painel de qualidade e cobertura**: total recuperado; percentuais com coordenadas, idades, país, localidade e identificação; riqueza taxonômica observada. Usar sempre a expressão "riqueza observada", sem equivalência com diversidade real.
2. **Matriz entre região e intervalo geológico**: contagens de ocorrências ou táxons observados; regiões baseadas nas localidades atuais; destaque para recortes com poucos dados.
3. **Comparador temporal**: seleção de dois períodos ou intervalos; comparação de mapas, contagens, riqueza observada, regiões e composição do conjunto.
4. **Gráfico de intervalos cronológicos**: faixas entre idade inicial e final; pode mostrar sobreposição temporal, mas não afirmar coexistência.

Extensão opcional somente após as quatro prioridades: rede biogeográfica de compartilhamento taxonômico. Depende dos atributos taxonômicos, da definição das regiões e do cronograma.

## Pergunta de pesquisa atualizada

Como visualizações interativas coordenadas, organizadas por recortes temporais e acompanhadas por indicadores de cobertura, podem apoiar a exploração de ocorrências de dinossauros do Mesozoico provenientes da PBDB sem ocultar as limitações da amostra consultada?

## Ordem recomendada de implementação

1. Corrigir o recorte padrão para Dinosauria e revisar a estratégia de volume das consultas.
2. Centralizar métricas e agregações em `utils/data_processing.py` ou em serviços analíticos próprios.
3. Implementar o painel de qualidade e validar manualmente as porcentagens.
4. Implementar a matriz região por intervalo e validar células amostrais.
5. Implementar o comparador temporal.
6. Implementar o gráfico de faixas cronológicas.
7. Coordenar mapa, gráficos, indicadores e tabela pelo mesmo estado de filtros.
8. Substituir mensagens interpretativas não sustentadas por textos descritivos.
9. Criar testes funcionais e de agregação antes da rede opcional.

## Avaliação planejada

- Matriz requisito versus caso de teste.
- Correspondência entre resposta da API, dados tratados e valores exibidos.
- Recálculo manual de taxas de completude, riqueza observada e células da matriz.
- Testes de consultas, filtros, estados vazios e mensagens de erro.
- Observação de tempo de resposta e carregamento, sem limiares inventados.
- Se houver participantes: tarefas para localizar ocorrências, reconhecer campos ausentes, interpretar a matriz, comparar recortes e consultar faixas de idade.
- Quantidade e critérios dos participantes ainda precisam ser definidos.

## Direção arquitetural futura

O autor pretende estudar padrões de projeto no futuro; eles ainda não estão implementados.

Possibilidades a avaliar após a estabilização dos requisitos:

- **Adapter** para converter respostas da PBDB em um modelo interno estável.
- **Repository ou Service Layer** para isolar acesso, cache e estratégia de obtenção.
- **Strategy** para tornar intercambiáveis análises, agregações ou modos de visualização.
- **Factory** para padronizar a criação de gráficos e componentes cartográficos.
- **Facade** para oferecer às páginas uma interface única de consulta, processamento e análise.

Não aplicar padrões apenas para aumentar a quantidade de classes. Cada padrão deverá responder a um problema concreto de variação, acoplamento, teste ou manutenção.

## Documentação acadêmica

- `Pre-Projeto_TCC_MesoGeofauna_aprimorado.docx`: primeira versão aprimorada.
- `Pre-Projeto_TCC_MesoGeofauna_aprimorado_v2.docx`: acrescenta as quatro análises, atualiza problema, objetivos, metodologia, avaliação, resultados esperados e cronograma, e registra padrões de projeto como direção futura.
- Referências utilizadas: Upchurch, Hunn e Norman (2002), Dunhill et al. (2016), Andrienko et al. (2010), Roth (2013), Lieberman (2000) e a documentação da PBDB fornecida pelo autor.

## Próximo passo recomendado no código

Antes de adicionar uma página visual, refatorar a obtenção e a preparação para que todas as análises recebam o mesmo DataFrame validado e o mesmo objeto de filtros. Depois, implementar primeiro o painel de qualidade, pois ele possui menor complexidade e cria métricas reutilizáveis.

## Atualização de adequação ao roteiro da disciplina

Foi criada a versão `Pre-Projeto_TCC_MesoGeofauna_adequado_requisitos_v3.docx`, sem alteração do código funcional do sistema. A revisão:

- consolidou os objetivos específicos de nove para seis;
- numerou as seções textuais principais;
- tornou a proposta do trabalho explícita na metodologia;
- acrescentou uma comparação entre os trabalhos já fornecidos e a proposta;
- definiu critérios mais objetivos para classificar requisitos e verificar agregações;
- acrescentou a seção de recursos necessários e viabilidade;
- identificou o cronograma como quadro, com título e fonte;
- substituiu a data antiga da capa pelo ano de 2026, sem presumir uma data de apresentação.

## Atualização de 28 de agosto de 2026

Foi criada a versão `Pre-Projeto_TCC_MesoGeofauna_relatorio_tecnico_v4.docx`, novamente sem alteração do código funcional do sistema.

Decisões confirmadas pelo autor:

1. O pré-projeto será apresentado provisoriamente na modalidade **Relatório Técnico**, sujeito a validação posterior com o orientador/professor.
2. O cronograma corresponde ao período letivo **2026.2 do IFBA**, compreendido no planejamento entre **outubro de 2026 e março de 2027**.
3. Foi autorizada pesquisa externa apenas para ampliar a comparação com soluções relacionadas; nenhuma funcionalidade foi implementada no sistema nesta etapa.

Atualizações acadêmicas da versão v4:

- registro da modalidade Relatório Técnico na folha de rosto e na metodologia;
- cronograma datado de outubro/2026 a março/2027 e coluna temporal ampliada;
- ampliação de Trabalhos Relacionados com PBDB Navigator, EonMap, Neotoma Explorer e GPlates Portal;
- delimitação explícita de que o MesoGeofauna não é a primeira interface visual para a PBDB;
- diferenciação pretendida pelo recorte em Dinosauria no Mesozoico, interface e documentação em português, painel de qualidade e cobertura, matriz região por intervalo, comparação entre dois recortes temporais e avaliação da fidelidade entre API, tratamento e exibição;
- registro de que o gráfico de faixas cronológicas, isoladamente, não será alegado como inovação, pois há solução relacionada com recurso semelhante;
- inclusão e normalização das novas referências no padrão adotado pelo pré-projeto;
- recálculo integral do sumário e revisão visual das páginas.

Fontes externas incorporadas à comparação:

- PBDB Navigator: repositório oficial `https://github.com/paleobiodb/navigator`;
- Paleobiology Database User Guide Version 2.0: Uhen et al. (2026), DOI `10.5070/P9.62178`;
- EonMap: guia oficial `https://eonmap.com/guide`;
- Neotoma Explorer: ajuda oficial `https://apps.neotomadb.org/explorer/help/Getstarted.html`;
- GPlates Portal: Müller et al. (2016), DOI `10.1371/journal.pone.0150883`;
- API da PBDB: Peters e McClennen (2016), DOI `10.1017/pab.2015.39`.

Estado do código após a atualização documental: **nenhum arquivo funcional do repositório foi modificado**. As quatro análises prioritárias, os testes e o estudo futuro de padrões de projeto permanecem como trabalho a implementar.

## Memória de retomada

Ao continuar este trabalho, considerar como fonte principal este arquivo e a versão acadêmica mais recente `Pre-Projeto_TCC_MesoGeofauna_relatorio_tecnico_v4.docx`.

Decisões que não devem ser perdidas:

- o artefato acadêmico ainda é um **pré-projeto**, não o TCC final;
- a modalidade adotada provisoriamente é **Relatório Técnico**, pendente apenas de confirmação posterior com o professor;
- o orientador registrado é o **Prof. Me. Samuel Melo**;
- o cronograma acadêmico adotado é **outubro/2026 a março/2027**, correspondente a 2026.2 no calendário informado do IFBA;
- o MesoGeofauna não deve ser apresentado como primeira interface visual para a PBDB;
- os diferenciais devem ser descritos como a integração do recorte, da interface em português, das análises prioritárias e da avaliação documentada, sem alegações não demonstradas de inovação;
- PBDB Navigator, EonMap, Neotoma Explorer e GPlates são referências relacionadas já incorporadas ao pré-projeto;
- a prioridade de implementação permanece: preparação comum dos dados, painel de qualidade, matriz região por intervalo, comparador temporal e gráfico de faixas cronológicas;
- a rede biogeográfica é opcional e padrões de projeto serão estudados somente depois da estabilização dos requisitos;
- análises e textos devem distinguir contagem de registros, riqueza observada, completude, coordenadas atuais e inferências paleobiogeográficas;
- não afirmar abundância, diversidade real, significância, ausência biológica, coexistência ou paleogeografia sem método e evidência apropriados;
- nenhuma das funcionalidades propostas foi implementada durante a revisão documental.

Próxima retomada no código: inspecionar novamente o estado atual do repositório antes de editar, preservar alterações do autor e começar pela consolidação do fluxo de consulta e tratamento em um DataFrame validado e compartilhado pelas análises.
