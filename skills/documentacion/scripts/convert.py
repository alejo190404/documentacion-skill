#!/usr/bin/env python3
"""Conversion Word <-> Markdown para el skill documentacion (reemplaza convertir_todos_docx.bat).

Uso:
    python convert.py <ruta_proyecto> [carpeta_entrada] [carpeta_salida] [--modo docx2md|md2docx] [--force]

Codigos de salida: 0 ok, 1 alguna conversion fallo, 2 falta una dependencia o Python < 3.12.
"""
import argparse
import logging
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

if sys.version_info < (3, 12):
    sys.exit(f"Se requiere Python 3.12 o superior (actual: {sys.version.split()[0]}).")

REQUIREMENTS = Path(__file__).resolve().parent.parent / "requirements.txt"
MERMAID = re.compile(r"^```mermaid[^\n]*\n(.*?)^```[ \t]*$", re.S | re.M)
EXT = {"docx2md": (".docx", ".md"), "md2docx": (".md", ".docx")}


def render_mermaid(text: str, tmp: Path) -> str:
    """Reemplaza bloques mermaid por imagenes PNG si mmdc esta disponible; si no, los deja como codigo."""
    mmdc = shutil.which("mmdc")
    if not mmdc:
        if MERMAID.search(text):
            print("Aviso: mmdc no esta en PATH; los diagramas Mermaid quedan como codigo.")
        return text

    def repl(m: re.Match) -> str:
        n = len(list(tmp.glob("mermaid-*.png")))
        src, png = tmp / f"mermaid-{n}.mmd", tmp / f"mermaid-{n}.png"
        src.write_text(m.group(1), encoding="utf-8")
        r = subprocess.run([mmdc, "-i", str(src), "-o", str(png)], capture_output=True, text=True, shell=sys.platform == "win32")
        if r.returncode != 0 or not png.exists():
            print(f"Aviso: mmdc fallo en un diagrama, se deja como codigo: {r.stderr.strip()}")
            return m.group(0)
        return f"![diagrama]({png.as_posix()})"

    return MERMAID.sub(repl, text)


def convert(pypandoc, src: Path, dst: Path, modo: str) -> None:
    if modo == "docx2md":
        pypandoc.convert_file(str(src), "gfm", format="docx", outputfile=str(dst),
                              extra_args=[f"--extract-media={dst.parent / 'media' / src.stem}"])
        return
    with tempfile.TemporaryDirectory() as tmp:
        text = render_mermaid(src.read_text(encoding="utf-8"), Path(tmp))
        # resource-path: las imagenes relativas del .md se resuelven desde su carpeta.
        pypandoc.convert_text(text, "docx", format="gfm", outputfile=str(dst),
                              extra_args=[f"--resource-path={src.parent}"])


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("proyecto", nargs="?", default=".", type=Path)
    p.add_argument("entrada", nargs="?", default="Entrada")
    p.add_argument("salida", nargs="?", default="fuentes-importadas")
    p.add_argument("--modo", choices=EXT, default="docx2md")
    p.add_argument("--force", action="store_true", help="sobrescribir archivos de salida existentes")
    a = p.parse_args(argv)

    try:
        import pypandoc
    except ImportError:
        print(f"Falta la libreria pypandoc. Instala las dependencias con:\n  {sys.executable} -m pip install -r \"{REQUIREMENTS}\"", file=sys.stderr)
        return 2
    logging.getLogger("pypandoc").setLevel(logging.CRITICAL)  # su traceback al probar el pandoc incluido es ruido
    try:
        pypandoc.get_pandoc_version()
    except OSError:
        # pypandoc_binary 1.17 trae pandoc x86_64 incluso en la rueda arm64 de macOS: sin Rosetta no arranca.
        print("pandoc no esta disponible o no se puede ejecutar. Instalalo en el sistema:\n"
              "  macOS: brew install pandoc  (o: softwareupdate --install-rosetta)\n"
              "  Windows: winget install JohnMacFarlane.Pandoc\n"
              "  Linux: sudo apt install pandoc  (o el gestor de tu distribucion)", file=sys.stderr)
        return 2

    entrada, salida = a.proyecto / a.entrada, a.proyecto / a.salida
    try:
        entrada.mkdir(parents=True, exist_ok=True)
        salida.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        print(f"No se pudieron crear las carpetas de trabajo: {e}", file=sys.stderr)
        return 1

    ext_in, ext_out = EXT[a.modo]
    # Word deja archivos ~$x.docx de bloqueo mientras el documento esta abierto.
    fuentes = sorted(f for f in entrada.glob(f"*{ext_in}") if not f.name.startswith("~$"))
    if not fuentes:
        print(f"No hay archivos {ext_in} en {entrada}. Deposita los archivos ahi y vuelve a ejecutar.")
        return 0

    generados, omitidos, fallidos = [], [], []
    for src in fuentes:
        dst = salida / (src.stem + ext_out)
        if dst.exists() and not a.force:
            omitidos.append(dst)
            continue
        try:
            convert(pypandoc, src, dst, a.modo)
            generados.append(dst)
        except Exception as e:  # pandoc lanza RuntimeError/OSError; se reporta y se sigue con el resto
            fallidos.append((src, e))

    for f in generados:
        print(f"Generado: {f}")
    for f in omitidos:
        print(f"Omitido (ya existe, usa --force para sobrescribir): {f}")
    for f, e in fallidos:
        print(f"Error en {f}: {e}", file=sys.stderr)
    return 1 if fallidos else 0


if __name__ == "__main__":
    sys.exit(main())
