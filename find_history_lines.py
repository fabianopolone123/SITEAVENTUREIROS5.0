from pathlib import Path

text = Path("HISTORICO_DE_MUDANCAS.md").read_text(encoding="utf-8", errors="replace").splitlines()
for idx, line in enumerate(text, 1):
    if "Alteração Nº 0009" in line:
        print("0009", idx)
    if "Alteração Nº 0010" in line:
        print("0010", idx)
