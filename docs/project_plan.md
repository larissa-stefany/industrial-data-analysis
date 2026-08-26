# Project Plan — Industrial Production Analytics

## Business context
Uma indústria de manufatura precisa entender gargalos de produtividade e qualidade em suas linhas de produção. O projeto simula um ambiente fabril com máquinas, turnos, operadores, produtos, disponibilidade, performance, qualidade, defeitos e paradas.

## Objective
Construir uma solução end-to-end de análise de dados que permita localizar perdas, comparar desempenho entre máquinas e turnos e orientar ações de melhoria contínua.

## Business questions
1. Quais máquinas apresentam maior taxa de defeitos?
2. Qual turno possui o melhor OEE?
3. Onde se concentram as maiores horas de parada?
4. Como a qualidade varia por produto e turno?
5. Quais máquinas combinam alto volume com baixa qualidade?
6. Existe relação entre downtime, disponibilidade e OEE?
7. Quais oportunidades devem ser priorizadas pela gestão?

## Core KPIs
- Total produzido
- Peças boas
- Peças defeituosas
- Taxa de defeitos
- Downtime total
- Availability
- Performance
- Quality
- OEE

## Architecture
Raw CSV → Python ETL → Clean CSV + SQLite → SQL/Python Analysis → Power BI Dashboard → Business Insights
