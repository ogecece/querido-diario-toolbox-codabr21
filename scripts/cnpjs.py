import json
from collections import Counter
from pathlib import Path

from tqdm import tqdm
from querido_diario_toolbox.process.edition_process import extract_and_validate_cnpj

ROOT = Path(__file__).parent.parent
PROCESSED_DATA = ROOT / "data-processed"
CNPJ_MATCHES = ROOT / "data" / "cnpjs.json"


def extrai_cnpjs(arquivo):
    data_publicacao = arquivo.parent.parent.name
    municipio = arquivo.parent.parent.parent.name
    nome_arquivo = arquivo.parent.stem

    texto = arquivo.read_text()
    cnpjs = extract_and_validate_cnpj(texto)

    contador_cnpjs = Counter(cnpjs)

    metadados_cnpjs = []
    for cnpj, qtd_encontrados in contador_cnpjs.items():
        metadados_cnpjs.append(
            {
                "cnpj": cnpj,
                "qtd_encontrados": qtd_encontrados,
                "municipio": municipio,
                "data_publicacao": data_publicacao,
                "nome_arquivo": nome_arquivo,
                "caminho_arquivo": str(arquivo),
            }
        )

    return metadados_cnpjs


cnpjs_encontrados = []
arquivos = list(PROCESSED_DATA.rglob("content.txt"))
for arquivo in tqdm(arquivos):
    result = extrai_cnpjs(arquivo)
    cnpjs_encontrados.extend(result)

    if result:
        print(result)

with CNPJ_MATCHES.open("w") as cnpjs_json:
    json.dump(cnpjs_encontrados, cnpjs_json, indent=2)
