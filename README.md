# Atividade Prática | Módulo II #

Neste desafio vamos testar seu conhecimento sobre os fundamentos de computação e versionamento de código em um projeto real de código.

**Descrição**

Neste projeto vamos construir uma aplicação simples em Python que testará a conectividade de um site (se este site está online ou não).
Recomendamos seguir o passo-a-passo dado em aula, mas você tem liberdade para personalizar a aplicação como quiser. O software é seu e o céu é o limite!

**Requisitos:**

- Você deve criar um repositório público no Github ou Bitbucket com o código da aplicação.
- Repositório deve conter um README e .gitignore bem estruturado.
- Todos os pacotes utilizados devem estar descritos em um arquivo requirements.txt
- A aplicação deverá permitir receber um ou mais URLs como argumento e retornar o status de cada website.

===================================================================================

Um código base foi desenvolvido em aula, e passado aos alunos para incluirmos nossa contribuição de acordo com os seguintes requisitos funcionais:

- Ampliar a função acima para permitir a inclusão de arquivos com listas de URLs no CLI passando um caminho --file path/to/file.csv.
- Criar um script em Bash que permite rodar esse verificador a partir de uma periodicidade pré-definida (por exemplo, a cada 24 horas). Ver CRON.

No módulo *_ _main_ _.py* precisamos implementar a lógica da `main` e do resto das funções necessárias para atender aos requisitos. 


```python

#...

def main():

#...

def _site_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result, url, error)
#...
```

A função main foi expandida, e outras duas funções foram incluídas para atender ao requisito funcional.


```python
#...
def main():
    user_args = read_user_cli_args()
    urls = _get_url_list(user_args)

    if not urls:
        print("No URL found")
        sys.exit(1)
    _site_check(urls)


def _get_url_list(user_args):
    """ Append all URLs passed as arguments to
        the url list fetched from file. 
    """
    urls = user_args.urls 
    
    if user_args.input_file:

        urls += _fetch_urls(user_args.input_file)
    return urls

def _fetch_urls(file):
    """ Check file for content, read through lines,
        and return a list off appended urls 
    """
    file_path = pathlib.Path(file)

    if file_path.is_file():
        
        with file_path.open() as fp:
            
            urls = [url.strip() for url in fp]
            
            if urls:
                return urls
            else:
                print(f"Error: file {file} is empty", file=sys.stderr)
    else:
        print("Error: File not found", file=sys.stderr)
        return []
#...
```

No módulo *cli.py* foi adicionado um trecho de código à função `read_user_cli_args` para agregar o argumento " -f " à aplicação.


```python
# ...
def read_user_cli_args():
# ...

# added argument for reading URLs from files
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="Read URLs from file",
    )
    
```

O módulo *checker.py* não teve alterações em relação ao código base.

A pasta **./input/** foi adicionada para armazenar os arquivos para teste da funcionalidade, e atualmente contém o arquivo urls.csv.

**E com isso fechamos o primeiro requisito funcional do projeto, e partimos para a segunda etapa do desafio!**


```python

```
