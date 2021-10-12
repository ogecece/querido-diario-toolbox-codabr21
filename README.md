# Querido Diário Toolbox - PYBR 2021

Este repositório é o código que foi utilizado na apresentação
"Experimentando a caixa de ferramentas do Querido Diário: trabalhando com dados não estruturados"
na Python Brasil 2021.

## Como usar

Para iniciar, configure seu ambiente virtual Python 3 e execute:

```sh
$ pip install -r requirements.txt
```

Depois, converta os arquivos fonte para texto puro com o comando (arquivos fonte não estão disponíveis
no repositório remoto ainda, passe para o próximo passo):

```sh
$ python scripts/extrator.py
```

Vários arquivos serão criados na pasta `data-processed`. Agora você pode identificar os CNPJs nestes arquivos com:

```sh
$ python scripts/cnpjs.py
```

Com o arquivo `data/cnpjs.json` criado, você pode interagir com o notebook `cnpj_analysis.ipynb` à vontade :)
