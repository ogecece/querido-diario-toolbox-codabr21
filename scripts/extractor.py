from pathlib import Path

from querido_diario_toolbox import Gazette
from querido_diario_toolbox.etl.text_extractor import create_text_extractor
from tqdm import tqdm


ROOT = Path(__file__).parent.parent
SOURCE_DATA = ROOT / "data" / "source"
TARGET_DATA = ROOT / "data-processed"
TARGET_DATA.mkdir(exist_ok=True)

config = {"apache_tika_jar": f"{ROOT}/tests/bin/tika-app-1.24.1.jar"}
extrator_textual = create_text_extractor(config)


def extrai_texto(arquivo, apagar_ao_completar=True):
    data_publicacao = arquivo.parent.name
    municipio = arquivo.parent.parent.name
    nome_arquivo = arquivo.stem

    try:
        diario = Gazette(filepath=str(arquivo))
    except Exception as e:
        # Unsupported file type
        return

    target_folder = TARGET_DATA / municipio / data_publicacao / nome_arquivo
    target_folder.mkdir(exist_ok=True, parents=True)

    conteudo = target_folder / "content.txt"
    extrator_textual.extract_text(diario, path_dest=str(conteudo))

    metadados = target_folder / "metadata.json"
    extrator_textual.extract_metadata(diario, path_dest=str(metadados))

    extrator_textual.load_content(diario)

    if apagar_ao_completar:
        arquivo.unlink()


arquivos = [arquivo for arquivo in SOURCE_DATA.rglob("*") if arquivo.is_file()]
for arquivo in tqdm(arquivos):
    extrai_texto(arquivo)

