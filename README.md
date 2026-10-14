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
- Máquina **M-12** com maior taxa de defeitos (indicador de qualidade); a máquina de menor OEE deve ser identificada separadamente pelo ranking de eficiência
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
├── .github/workflows/tests.yml  # Testes automáticos no GitHub Actions
├── docs/                        # Plano, dicionário e questões de negócio
├── powerbi/                     # Especificação e medidas DAX (não é um .pbix)
├── sql/                         # Esquema e consultas SQL
├── src/                         # Gerador, ETL, KPIs, qualidade e gráficos
├── tests/                       # Testes automatizados com pytest
├── README.md
└── requirements.txt
```

As pastas `data/raw/`, `data/processed/` e `images/` são geradas localmente na execução; não são capturas de tela já publicadas no repositório.

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

### 5. Gere gráficos reais dos resultados

```bash
python -m src.generate_charts
```

As imagens serão salvas em `images/` (OEE por máquina e Pareto de defeitos), com base nos dados sintéticos processados pelo próprio projeto.

### 6. Rode os testes

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
  KPIs + gráficos + insights
            ↓
  Power BI (modelo proposto)
```

## Análises desenvolvidas

### Qualidade
Avaliação de taxa de defeitos por máquina e turno para identificar equipamentos com maior concentração de perdas de qualidade.

### Produtividade
Comparação de volume produzido, tempo de parada e eficiência entre máquinas, turnos e períodos.

### OEE
Cálculo e análise dos componentes de disponibilidade, performance e qualidade para encontrar oportunidades de melhoria operacional.

## Power BI

A pasta `powerbi/` contém medidas DAX e uma **especificação de dashboard**, não um relatório `.pbix` concluído. A proposta inclui:

- Cards de Produção, OEE, Defeitos e Downtime
- Ranking de máquinas críticas
- Comparação por turno
- Tendência mensal
- Filtros por máquina, turno e período

## Reprodutibilidade dos dados

Os arquivos brutos e o banco SQLite completos não são versionados no GitHub porque são gerados automaticamente e ocupam dezenas de MB. Para reproduzir exatamente a estrutura do projeto, execute `generate_data.py` e depois `etl.py`.

Os indicadores podem ser reproduzidos executando `python -m src.kpis` e `python -m src.insights` após a geração e o ETL. Os gráficos são gerados com `python -m src.generate_charts`.

## Próximos passos

- Criar modelo preditivo de falhas/manutenção
- Implementar análise de causa raiz automatizada
- Ampliar cobertura do pipeline CI existente com testes de integração e SQL
- Evoluir dashboard para acompanhamento operacional quase em tempo real

## Autora

**Larissa Stefany**  
Portfólio focado em Dados, Analytics, Python, SQL e Power BI.

---

Este projeto utiliza dados sintéticos e não contém informações de nenhuma empresa real.
