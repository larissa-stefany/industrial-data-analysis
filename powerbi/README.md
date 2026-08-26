# Power BI Dashboard

Use `data/processed/manufacturing_production_clean.csv` como fonte principal no Power BI Desktop.

## Páginas sugeridas
### 1. Executive Overview
Cards: Total Production, Good Units, Defect Rate, Downtime Hours, OEE.
Visuals: produção mensal, OEE por turno, taxa de defeitos por máquina.

### 2. Quality Analysis
Visuals: ranking de máquinas por defeito, defeitos por produto, matriz máquina x turno, tendência mensal de qualidade.

### 3. Productivity & OEE
Visuals: OEE por máquina, Availability/Performance/Quality, downtime por máquina e turno, volume de produção.

## Filtros
- Data
- Linha
- Máquina
- Produto
- Turno
- Operador

## DAX
As medidas recomendadas estão em `powerbi/measures.dax`.
