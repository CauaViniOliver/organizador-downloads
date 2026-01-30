Organizador de downloads
Script pra organizar os arquivos da sua pasta de downloads automaticamente.

como funciona:
O script olha a extensão do arquivo e joga na pasta certa (Imagens, Documentos, etc). Se a pasta não existir, ele cria.

como rodar:
1. Coloque o script (Organizer.py) na pasta de downloads
2. Abra o terminal/cmd nessa pasta
3. Execute: python Organizer.py (Python 3 obrigatório)
Nota: Os caminhos se ajustam automaticamente (Windows/Linux)

o que eu usei:
pathlib pra lidar com os caminhos das pastas.
um dicionário pra mapear o que vai pra onde.
try/except pra ignorar erro de arquivo sendo usando.
