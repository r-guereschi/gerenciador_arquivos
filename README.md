# Gerenciador de Fotos
Este é um aplicativo simples em Python utilizando Tkinter para gerenciar fotos em um diretório específico. Ele oferece funcionalidades para renomear fotos, dividir fotos em subpastas e mover fotos de subpastas para o diretório principal.

## Tecnologias Utilizadas
- Python: Linguagem de programação principal.
- Tkinter: Biblioteca gráfica para criar interfaces de usuário.
- os: Módulo para interação com o sistema operacional (gerenciamento de arquivos e diretórios).
- re: Módulo para operações com expressões regulares.
- shutil: Módulo para operações de alto nível em arquivos e diretórios.
- tkinter.filedialog: Módulo para seleção de diretórios.
- tkinter.simpledialog: Módulo para caixas de diálogo simples de entrada de dados.
- tkinter.messagebox: Módulo para exibição de mensagens de aviso, erro e informação.
## Funcionalidades
- Renomear Fotos:
Esta funcionalidade permite renomear todas as fotos de um diretório selecionado adicionando um prefixo especificado pelo usuário.

- Dividir Fotos em Subpastas:
Esta funcionalidade divide as fotos de um diretório selecionado em subpastas, com um número definido de fotos por subpasta.

- Remover Subpastas e Mover Fotos:
Esta funcionalidade move todas as fotos das subpastas para o diretório principal e, em seguida, remove as subpastas vazias.

## Como Usar
Seleção de Diretório: Ao abrir o programa, clique nos botões para executar a função desejada. Será solicitada a seleção do diretório onde estão armazenadas as fotos.

- Renomear Fotos:

Clique no botão "Renomear Fotos".
Digite o novo prefixo na caixa de diálogo que aparece.
As fotos serão renomeadas com o prefixo digitado.
- Dividir Fotos em Subpastas:

Clique no botão "Dividir Fotos em Subpastas".
Digite o número desejado de fotos por subpasta na caixa de diálogo.
As fotos serão divididas em subpastas dentro do diretório selecionado.
- Remover Subpastas e Mover Fotos:

Clique no botão "Remover Subpastas e Mover Fotos".
As fotos serão movidas do interior das subpastas para o diretório principal selecionado, e as subpastas vazias serão removidas.
## Exemplo de Uso
- Inicialização:

Execute o arquivo Python gerenciador_de_fotos.py.
A interface gráfica será aberta.
- Renomear Fotos:

Selecione o diretório onde estão as fotos.
Digite um novo prefixo quando solicitado.
As fotos serão renomeadas com o prefixo especificado.
- Dividir Fotos em Subpastas:

Selecione o diretório onde estão as fotos.
Escolha o número de fotos por subpasta.
As fotos serão organizadas em subpastas dentro do diretório selecionado.
- Remover Subpastas e Mover Fotos:

Selecione o diretório onde estão as fotos com subpastas.
As fotos serão movidas para o diretório principal e as subpastas serão removidas.
