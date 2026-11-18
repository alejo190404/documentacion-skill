# documentacion-skill

Skill `documentacion` para agentes de IA. Sirve para crear y revisar documentacion de proyectos y para convertir documentos entre Word y Markdown con Python, en Windows, macOS y Linux.

Sigue el estandar [Agent Skills](https://agentskills.io): toda la carpeta `skills/documentacion/` es el skill. Para instalarlo en cualquier herramienta, se copia esa carpeta.

```
skills/documentacion/
  SKILL.md                 instrucciones del agente
  requirements.txt         dependencias de Python
  scripts/convert.py       conversion Word <-> Markdown (reemplaza convertir_todos_docx.bat)
  plantillas/              plantilla del documento de desarrollo
  prompts/                 prompts por seccion de la plantilla
tests/                     pruebas del repositorio (no forman parte del skill)
```

## Requisitos

| Dependencia | Obligatoria | Instalacion |
|---|---|---|
| Python 3.12+ | Si | Windows: `winget install Python.Python.3.12` · macOS: `brew install python@3.12` · Linux: `sudo apt install python3.12 python3.12-venv` |
| pypandoc_binary (incluye pandoc) | Si | `python -m pip install -r skills/documentacion/requirements.txt` |
| pandoc en el sistema | Solo si el incluido no funciona | Windows: `winget install JohnMacFarlane.Pandoc` · macOS: `brew install pandoc` · Linux: `sudo apt install pandoc` |
| Git | Si | https://git-scm.com/downloads |
| Mermaid CLI (`mmdc`) | No | `npm install -g @mermaid-js/mermaid-cli` (requiere Node.js) |

> En macOS con Apple Silicon, `pypandoc_binary` 1.17 trae un pandoc x86_64 que solo arranca si Rosetta esta instalado. Hay dos soluciones: `brew install pandoc` o `softwareupdate --install-rosetta`. Cuando pandoc no se puede ejecutar, el script lo detecta e imprime la instruccion de instalacion.

Sin `mmdc`, la conversion funciona igual, pero los diagramas Mermaid quedan como bloques de codigo en el DOCX.

## Instalacion

### Un comando (cualquier herramienta compatible)

```
npx skills add alejo190404/documentacion-skill
```

El CLI [`skills`](https://github.com/vercel-labs/skills) detecta los agentes instalados (Claude Code, GitHub Copilot, Codex, Cursor, entre otros) y copia el skill en la carpeta que corresponde a cada uno.

### Manual

Clona el repositorio y copia `skills/documentacion` en la carpeta de skills de tu herramienta:

| Herramienta | Global (usuario) | Por proyecto |
|---|---|---|
| Claude Code | `~/.claude/skills/documentacion` | `.claude/skills/documentacion` |
| GitHub Copilot (VS Code) | `~/.copilot/skills/documentacion` | `.github/skills/documentacion` |
| Otras (Codex, etc.) | `~/.agents/skills/documentacion` | `.agents/skills/documentacion` |

macOS / Linux:

```
git clone https://github.com/alejo190404/documentacion-skill.git
mkdir -p ~/.claude/skills
cp -R documentacion-skill/skills/documentacion ~/.claude/skills/
python3.12 -m pip install -r ~/.claude/skills/documentacion/requirements.txt
```

Windows (PowerShell):

```
git clone https://github.com/alejo190404/documentacion-skill.git
New-Item -ItemType Directory -Force "$env:USERPROFILE\.claude\skills" | Out-Null
Copy-Item -Recurse documentacion-skill\skills\documentacion "$env:USERPROFILE\.claude\skills\"
py -3.12 -m pip install -r "$env:USERPROFILE\.claude\skills\documentacion\requirements.txt"
```

Cambia `.claude` por la carpeta de tu herramienta (consulta la tabla anterior).

## Uso del script

El agente ejecuta el script, pero tambien se puede usar directamente:

```
python skills/documentacion/scripts/convert.py <ruta_proyecto> [carpeta_entrada] [carpeta_salida] [--modo docx2md|md2docx] [--force]
```

- Valores por defecto: `.` como proyecto, `Entrada` como carpeta de entrada, `fuentes-importadas` como carpeta de salida y `docx2md` como modo.
- El script crea las carpetas si no existen. Los archivos de salida que ya existen no se sobrescriben, salvo con `--force`.
- Codigos de salida: `0` si todo salio bien, `1` si fallo alguna conversion y `2` si falta una dependencia.

Ejemplo:

```
python skills/documentacion/scripts/convert.py "C:\proyectos\mi app" Entrada fuentes-importadas --modo docx2md
```

## Desarrollo

```
python3.12 -m venv .venv
.venv/bin/pip install -r skills/documentacion/requirements.txt   # Windows: .venv\Scripts\pip
.venv/bin/python tests/test_convert.py
```
