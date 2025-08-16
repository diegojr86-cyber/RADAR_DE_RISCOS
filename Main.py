!pip install papermill --quiet

import papermill as pm
import os

BASE_PATH = r"C:\Users\diego\OneDrive\DATAMASTER\dados_bacen_new\codigos_python"

notebooks = [
    "01_dados_bacen_extracao_arquivo.ipynb",
    "03_Importa_arquivo_para_bucket_BQ.ipynb",
    "04_importa_arquivo_do_bucket_para_bronze.ipynb",
    "05_dados_estado_serasa_SIMULACAO.ipynb",
    "06_Importa_arquivo_inadim_estimada_para_bucket_BQ.ipynb",
    "07_importa_arquivo_inadim_estimada_uf_bucket_para_bronze.ipynb",
    "08_cria_depara_de_codigo_modalidade.ipynb",
    "09_Importa_arquivo_depara_modalidade_para_bucket_BQ.ipynb",
    "10_importa_arquivo_depara_modalidade_bucket_para_bronze.ipynb"
]

OUTPUT_PATH = os.path.join(BASE_PATH, "executados")
os.makedirs(OUTPUT_PATH, exist_ok=True)

print("🚀 Iniciando execução dos notebooks...\n")

for nb in notebooks:
    input_path = os.path.join(BASE_PATH, nb)
    output_path = os.path.join(OUTPUT_PATH, f"executado_{nb}")
    
    print(f"▶️ Executando: {nb}")
    if not os.path.exists(input_path):
        print(f"❌ Arquivo não encontrado: {input_path}\n")
        continue

    try:
        pm.execute_notebook(
            input_path,
            output_path,
            parameters={},
            kernel_name="python3"  # ajuste conforme seu kernel
        )
        print(f"✅ Finalizado: {nb}\n")
    except Exception as e:
        print(f"❌ Erro ao executar {nb}: {e}\n")

print("🏁 Pipeline completo.")