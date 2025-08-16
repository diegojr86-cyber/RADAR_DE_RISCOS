
# 📊 Radar de Risco – Engenharia de Dados

## 1. Objetivo

O Radar de Risco é uma solução robusta de Engenharia de Dados voltada para o monitoramento contínuo e projeção da inadimplência por Unidade Federativa (UF) e modalidade de crédito. A plataforma integra dados de fontes públicas (como Bacen e IBGE) e privadas, transformando informações dispersas em inteligência acionável para a gestão proativa do risco de crédito.

Desenvolvido com boas práticas de arquitetura, o projeto incorpora automação de pipelines, governança de dados e modelos preditivos baseados em séries temporais, sustentado por uma stack escalável e de fácil manutenção.

Essa base tecnológica permite às instituições financeiras:

- 📊 Antecipar movimentos de risco por região e produto  
- 🧠 Apoiar decisões estratégicas de concessão, precificação e provisionamento  
- 🛡️ Fortalecer modelos de risco e compliance com evidências históricas e projeções confiáveis  
- 📍 Segmentar políticas de crédito por geografia e perfil, aumentando a eficiência operacional  

---

## 2. Arquitetura de Dados

A arquitetura segue o conceito **Bronze → Silver → Gold**, com camadas bem definidas:

### 2.1 Camada de Monitoramento
- Atualização contínua de fontes públicas  
- Execução automática de pipelines  
- Validação de integridade dos dados  
- Geração de alertas e logs para observabilidade  

### 2.2 Camada de Ingestão e ETL (Bronze)

**Fontes Públicas**
- Extração de dados (Bacen) em formatos JSON/CSV  
- Armazenamento inicial em buckets  
- Ingestão no BigQuery (camada Bronze)  

**Fontes Privadas – SERASA (base simulada)**
- Importação de arquivos por granularidade estadual  
- Simulações via Python para enriquecer dados  
- DEPARA para padronização de códigos e modalidades  

### 2.3 Camada de Transformação e Modelagem (Silver)
- Transformações e consolidações no BigQuery  
- Aplicação de regras de negócio  
- Criação de base limpa e unificada  

### 2.4 Camada de Apresentação (Gold)
- Modelagem preditiva com ARIMA  
- Projeções para 12 meses  
- Painel Radar de Riscos no Power BI conectado à base Gold  
- Visualizações interativas para decisão estratégica  

### 2.5 Ciclo Automatizado
- Orquestração periódica dos pipelines  
- Detecção de novas cargas  
- Reprocessamento de projeções  
- Atualização da base Gold  
- Logs e notificações  

---

## 3. Requisitos Atendidos

- **Extração de Dados**: APIs, CSVs, fontes públicas e privadas  
- **Ingestão**: Lotes automatizados via ETL  
- **Armazenamento**: BigQuery (cloud) – escalável e de alto desempenho  
- **Observabilidade**: Logs, alertas e rastreabilidade (Implantar) 
- **Segurança**: Criptografia, controle de acesso e conformidade com LGPD  
- **Mascaramento de Dados**: Anonimização de campos sensíveis (Utilizado apenas para dados sensíveis de acordo com a governança e LGPD)
- **Escalabilidade**: Arquitetura pronta para expansão horizontal e vertical  

---

## 4. Stack Tecnológica

| Categoria             | Ferramenta              |
|----------------------|-------------------------|
| Cloud Data Warehouse | BigQuery                |
| Orquestração         | Cloud Scheduler / Python|
| Visualização         | Power BI                |
| Linguagem            | Python                  |
| Modelagem Preditiva  | ARIMA                   |
| Armazenamento Bruto  | Cloud Storage           |

---

## 5. 📁 Organização dos Notebooks

Este repositório está estruturado para facilitar a navegação e compreensão dos diferentes estágios do pipeline de dados. Os notebooks foram agrupados em pastas conforme sua função principal:

### 5.1 `extracao/`

Contém os notebooks responsáveis por coletar dados de fontes externas, como APIs, arquivos brutos ou bancos de dados.

| Arquivo                                    | Descrição breve                                |
|--------------------------------------------|------------------------------------------------|
| `01_dados_bacen_extracao_arquivo.ipynb`    | Extração inicial de dados da fonte bacen       |
| `05_dados_estado_serasa_SIMULACAO.ipynb`   | Coleta de dados complementares da fonte SERASA |
| `08_cria_depara_de_codigo_modalidade.ipynb`| Extração incremental e atualização de DEPARA   |

### 5.2 `ingestao/`

Reúne os notebooks que tratam da ingestão dos dados extraídos, incluindo limpeza, padronização e armazenamento em sistemas internos.

| Arquivo                                                           | Descrição breve                                  |  
|-------------------------------------------------------------------|--------------------------------------------------|
| `03_Importa_arquivo_para_bucket_BQ.ipynb`                         | Pré-processamento e normalização dos dados       |
| `04_importa_arquivo_do_bucket_para_bronze.ipynb`                  | Ingestão cloud camada bronze                     |
| `06_Importa_arquivo_inadim_estimada_para_bucket_BQ.ipynb`         | Pré-processamento e normalização dos dados       |
| `07_importa_arquivo_inadim_estimada_uf_bucket_para_bronze.ipynb`  | Carga em banco de dados                          |
| `09_Importa_arquivo_depara_modalidade_para_bucket_BQ.ipynb`       | Pré-processamento e normalização dos dados       |
| `10_importa_arquivo_depara_modalidade_bucket_para_bronze.ipynb`   | Ingestão cloud camada bronze                     |

Essa estrutura modular permite que cada etapa do fluxo de dados seja facilmente identificada, testada e reutilizada. Para contribuir com novos notebooks, recomenda-se seguir essa divisão temática.

---

## 6. Como Executar

### 6.1 Pré-requisitos
- Conta no Google Cloud Platform  (passo a passo:  002_criar_ambiente_BQ)
- Python 3.9+  
- Power BI Desktop  
- Anaconda Navigator (passo a passo:  001_instalacao_Anaconda)

### 6.2 Passos

```bash
git clone https://github.com/diegojr86-cyber/RADAR_DE_RISCOS.git
cd radar-de-risco
pip install -r requirements.txt
```
- Configure variáveis de ambiente (credenciais e configs)  
- Execute o pipeline ETL:  
```bash
  main.py
```
Executar via Jupyter/Notebook 
--- Este processo assegura plena observabilidade sobre as etapas de coleta e ingestão de dados, permitindo o acompanhamento contínuo e em tempo real do fluxo de informações. Com isso, é possível identificar rapidamente eventuais falhas, gargalos ou desvios, promovendo maior confiabilidade, rastreabilidade e eficiência operacional.

---

## 7. Exemplo de Fluxo de Dados

`[Monitoramento] → [Ingestão Bronze] → [Transformação Silver] → [Apresentação Gold] → [Power BI]`

---

## 8. Painel de Monitoramento


<img width="753" height="768" alt="image" src="https://github.com/user-attachments/assets/0f91673b-e35b-4c9a-8b88-22f6d412cdc4" />

---

## 9. Melhorias Futuras

- Implementação de arquitetura Kappa para streaming  
- Escalabilidade horizontal com particionamento e paralelismo  
- Painel de monitoramento dos scripts Python agendados no Windows  
- Automação de deploy com CI/CD  
- Inclusão de variáveis externas (Cadastro Positivo, CAGED, IPEA etc.)  
- Treinamento e validação dos modelos com RMSE, MAPE e validação cruzada  

---

## Autor

**Diego de Jesus Rodrigues** – Engenharia de Dados



