from pathlib import Path

def organizar_pasta(diretorio):
    CATEGORIAS = {
        ".jpg": "Imagens", ".jpeg": "Imagens", ".png": "Imagens",
        ".pdf": "Documentos", ".docx": "Documentos", ".txt": "Documentos",
        ".zip": "Compactados", ".rar": "Compactados",
        ".exe": "Executaveis"
    }

    caminho_base = Path(diretorio)

    if not caminho_base.exists():
        return print(f"O diretório {diretorio} não existe.")

    for arquivo in caminho_base.iterdir():
        extensao = arquivo.suffix.lower()
        if arquivo.is_file() and extensao in CATEGORIAS:
            pasta_destino = caminho_base / CATEGORIAS[extensao]
            
            try:
                pasta_destino.mkdir(exist_ok=True)
                arquivo.rename(pasta_destino / arquivo.name)
            except (PermissionError, FileExistsError):
                continue

if __name__ == "__main__":
    organizar_pasta(Path.home() / "Downloads")
