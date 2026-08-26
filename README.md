# Industrial Data Analysis — Manufacturing Performance & Quality

Projeto de portfólio de **Análise de Dados Industrial** voltado à identificação de gargalos de produtividade, qualidade e eficiência em um ambiente de manufatura.

A solução simula um cenário realista de chão de fábrica com **100.000 registros de produção**, aplica ETL em Python, estrutura consultas SQL, calcula KPIs industriais e organiza análises para consumo em Power BI.

## Objetivo de negócio

Responder perguntas como:

- Quais máquinas apresentam maior taxa de defeitos?
- Qual turno possui melhor e pior eficiência?
- Como o tempo de parada impacta produtividade e OEE?
- Quais equipamentos concentram as maiores perdas?
- Como produção, qualidade e eficiência evoluem ao longo do ano?

## Principais KPIs

- Produção total
- Taxa de defeitos
- Disponibilidade
- Performance
- Qualidade
- OEE (Overall Equipment Effectiveness)
- Tempo de parada
- Eficiência por máquina e turno

## Resultados da base simulada

- **100.000 registros** de produção
- Aproximadamente **27 milhões de unidades produzidas**
- **OEE médio: ~78,6%**
- **Taxa média de defeitos: ~4,8%**
- Máquina **M-12** identificada como um dos principais pontos críticos de qualidade
- **3º turno** com desempenho médio inferior aos demais turnos

> Os dados são totalmente sintéticos e foram gerados apenas para fins educacionais e de portfólio.

## Tecnologias

- Python
- Pandas
- NumPy
- Matplotlib
- SQLite
- SQL
- Jupyter Notebook
- Power BI / DAX
- Pytest
- Git / GitHub

## Estrutura do projeto

```text
industrial-data-analysis/
├── data/
│   ├── raw/                  # Dados brutos gerados localmente
│   └── processed/            # Dados tratados e tabelas-resumo
├── docs/
│   └── project_plan.md
├── images/
│   ├── defect_rate_by_machine.png
│   ├── monthly_production.png
│   └── oee_by_shift.png
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_quality_analysis.ipynb
│   └── 03_productivity_analysis.ipynb
├── powerbi/
│   ├── README.md
│   └── measures.dax
├── sql/
│   ├── analysis_queries.sql
│   └── schema.sql
├── src/
│   ├── generate_data.py
│   ├── etl.py
│   └── kpis.py
├── tests/
│   └── test_pipeline.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/larissa-stefany/industrial-data-analysis.git
cd industrial-data-analysis
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente e instale as dependências:

```bash
pip install -r requirements.txt
```

### 3. Gere os dados sintéticos

```bash
python src/generate_data.py
```

### 4. Execute o ETL

```bash
python src/etl.py
```

### 5. Rode os testes

```bash
pytest
```

## Pipeline

```text
Synthetic Manufacturing Data
            ↓
      Python ETL
            ↓
Cleaning + Feature Engineering
            ↓
     SQLite / CSV
       ↙         ↘
   SQL Analysis   Python EDA
       ↘         ↙
        Power BI
            ↓
   Business Insights
```

## Análises desenvolvidas

### Qualidade
Avaliação de taxa de defeitos por máquina e turno para identificar equipamentos com maior concentração de perdas de qualidade.

### Produtividade
Comparação de volume produzido, tempo de parada e eficiência entre máquinas, turnos e períodos.

### OEE
Cálculo e análise dos componentes de disponibilidade, performance e qualidade para encontrar oportunidades de melhoria operacional.

## Power BI

A pasta `powerbi/` contém as medidas DAX e a especificação do dashboard. A proposta inclui:

- Cards de Produção, OEE, Defeitos e Downtime
- Ranking de máquinas críticas
- Comparação por turno
- Tendência mensal
- Filtros por máquina, turno e período

## Reprodutibilidade dos dados

Os arquivos brutos e o banco SQLite completos não são versionados no GitHub porque são gerados automaticamente e ocupam dezenas de MB. Para reproduzir exatamente a estrutura do projeto, execute `generate_data.py` e depois `etl.py`.

As tabelas-resumo leves permanecem no repositório para facilitar a inspeção rápida dos resultados.

## Próximos passos

- Criar modelo preditivo de falhas/manutenção
- Implementar análise de causa raiz automatizada
- Adicionar pipeline CI com testes
- Evoluir dashboard para acompanhamento operacional quase em tempo real

## Autora

**Larissa Stefany**  
Portfólio focado em Dados, Analytics, Python, SQL e Power BI.

---

Este projeto utiliza dados sintéticos e não contém informações de nenhuma empresa real.
