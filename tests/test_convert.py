"""Prueba de ida y vuelta md2docx -> docx2md. Ejecutar: python tests/test_convert.py"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "skills/documentacion/scripts"))
from convert import main

MD = """# Módulo de pruebas ñ

| Campo | Tipo |
|-------|------|
| id    | int  |

```mermaid
graph TD; A-->B
```
"""

with tempfile.TemporaryDirectory() as tmp:
    proj = Path(tmp) / "proyecto con espacios ñ"
    (proj / "md").mkdir(parents=True)
    (proj / "md/doc.md").write_text(MD, encoding="utf-8")

    assert main([str(proj), "md", "word", "--modo", "md2docx"]) == 0
    assert (proj / "word/doc.docx").exists()

    assert main([str(proj), "word", "vuelta"]) == 0
    out = (proj / "vuelta/doc.md").read_text(encoding="utf-8")
    assert "Módulo de pruebas ñ" in out and "Campo" in out, out

    # Sin --force no se sobrescribe.
    (proj / "vuelta/doc.md").write_text("intacto", encoding="utf-8")
    assert main([str(proj), "word", "vuelta"]) == 0
    assert (proj / "vuelta/doc.md").read_text(encoding="utf-8") == "intacto"

print("OK")
