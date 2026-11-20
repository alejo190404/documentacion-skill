---
name: documentacion
description: Crea, revisa y mantiene documentacion de proyectos (documentos de desarrollo, README, guias, docstrings) en español neutro, y convierte documentos Word a Markdown y viceversa con un script de Python multiplataforma. Usar cuando el usuario pida crear un documento de desarrollo, revisar o mejorar documentacion existente, o importar/exportar documentos Word (.docx).
---

# Documentacion

## Metadatos
- version: 2.0.0-dev
- fecha: 2026-11-18
- cambios:
  - Skill portable (estandar Agent Skills): rutas relativas a la carpeta del skill.
  - Se reemplaza el script BAT por `scripts/convert.py` (Python 3.12+, Windows/macOS/Linux).

En este documento, `<skill>` es la carpeta que contiene este SKILL.md.

## Objetivo principal
- Crear, mejorar y mantener documentacion clara, consistente y actualizada.
- Trabajar sobre archivos de documentacion (Markdown, HTML de ayuda, etc.), comentarios en el codigo y docstrings.
- Ayudar a estructurar y reorganizar documentacion existente para que sea mas facil de entender y mantener.

## Estilo y tono
- Escribir en español neutro, claro y profesional, salvo que el usuario pida otro idioma; mantener consistencia en todo el documento.
- Usar Markdown (encabezados, listas, tablas, bloques de codigo).
- Ser conciso, pero suficientemente descriptivo para que otro desarrollador entienda el contexto.
- No usar emojis salvo peticion explicita.
- Mantener el tono y la estructura del resto de la documentacion del repositorio.

## Requisitos de entorno
- Python 3.12 o superior.
- Dependencias: `python -m pip install -r <skill>/requirements.txt`.
- pandoc: lo incluye `pypandoc_binary`. Si el script indica que pandoc no se puede ejecutar (por ejemplo, macOS Apple Silicon sin Rosetta), instalarlo en el sistema segun el mensaje del script.
- Opcional: Mermaid CLI (`mmdc`) en PATH para incrustar diagramas Mermaid como imagen en DOCX.
- Git instalado y disponible en la linea de comandos.
- Permisos de lectura/escritura sobre las carpetas del proyecto analizado.

Antes del primer flujo, verificar Python (`python --version` o `python3 --version`). Si falta Python o la version es menor que 3.12, detener el flujo e indicar como instalarlo.

## Comportamiento y flujo de trabajo
- Antes de escribir documentacion, leer el codigo y la documentacion relevantes e inferir el contexto.
- Protocolo de ejecucion en 2 niveles:
  - Nivel 1 (Router): detectar el flujo activo y validar entradas minimas antes de generar contenido.
  - Nivel 2 (Runbook): ejecutar unicamente los pasos del flujo activo y completar su checklist de salida.
- Las reglas del flujo activo prevalecen sobre las reglas generales en caso de conflicto.
- Si la peticion es ambigua, pedir una aclaracion breve antes de producir grandes cambios.
- Proponer, cuando tenga sentido, una estructura de secciones y luego rellenarla.
- No cambiar la logica del codigo: solo documentacion, comentarios o nombres puramente descriptivos, salvo peticion contraria.
- Mantener los ejemplos de codigo ejecutables y consistentes con la base de codigo actual.

### Seleccion de flujo
- Flujos soportados:
  - documento-desarrollo: genera un documento de diseño/desarrollo con la plantilla y los prompts estandar.
  - revision-doc: revisa y mejora documentacion existente.
  - importar-word-a-markdown: convierte Word <-> Markdown con `scripts/convert.py`.
- Si el usuario no indica el flujo, ofrecer: "Puedo ayudarte con: (1) Creacion de documento de desarrollo, (2) Revisar o mejorar documento existente, (3) Importar o exportar Word. Indica el numero u opcion que prefieres." y esperar la respuesta.

### Flujo: documento-desarrollo
- Archivos base:
  - Plantilla: `.github/skills/documentacion/plantillas/documento-desarrollo.plantilla.md` del workspace si existe; si no, `<skill>/plantillas/documento-desarrollo.plantilla.md`.
  - Prompts: `.github/skills/documentacion/prompts/documento-desarrollo.prompts.md` del workspace si existe; si no, `<skill>/prompts/documento-desarrollo.prompts.md`.
- Entrada esperada: ruta del Markdown final, contexto del desarrollo y, opcionalmente, personalizaciones de secciones.
- Fase 1 (carga y validacion):
  - Leer los prompts y construir un mapa id -> texto.
  - Leer la plantilla y localizar los marcadores `<!-- PROMPT: id -->`.
  - Validar correspondencia 1:1 entre IDs. Si faltan, listarlos y pedir confirmacion para continuar con `[PROMPT_FALTANTE:id]` o detener.
- Fase 2 (borrador por secciones):
  - Para cada marcador, generar la seccion con el prompt, el contexto del usuario y el codigo existente, y sustituir el marcador manteniendo el texto fijo de la plantilla.
  - La plantilla reproduce la estructura de `plantilla.docx` (Diseño detallado y desarrollo): conservar el orden, la numeracion y los titulos de las secciones, las tablas y el texto fijo. No agregar ni quitar secciones.
  - Si el marcador va seguido de una tabla, completar esa tabla (sustituir los `{campo}` y agregar filas) y eliminar el marcador. En diseño detallado, repetir el bloque de componente una vez por componente.
  - En el documento final no deben quedar marcadores `<!-- PROMPT -->` ni valores `{campo}` sin sustituir.
  - La plantilla ya incluye la tabla de contenido: no generar otra.
  - Diagramas Mermaid solo si el contenido describe arquitectura, flujos o secuencias.
  - Gantt en Mermaid solo si el usuario lo pide o el contexto incluye hitos.
- Fase 3 (persistencia):
  - Guardar en la ruta indicada. Si el archivo existe, pedir confirmacion (sobrescribir, actualizar, cancelar o copia con sufijo).

### Flujo: importar-word-a-markdown
- Entrada: ruta del proyecto (por defecto, el directorio actual), carpeta de entrada (por defecto `Entrada`), carpeta de salida (por defecto `fuentes-importadas`) y modo `docx2md` (por defecto) o `md2docx`.
- Ejecutar, igual en Windows, macOS y Linux (usar `python3` si `python` no apunta a 3.12+):

  ```
  python "<skill>/scripts/convert.py" "<ruta_proyecto>" "<carpeta_entrada>" "<carpeta_salida>" --modo <modo>
  ```

- El script crea las carpetas si no existen. Indicar al usuario que deposite los `.docx` (docx2md) o `.md` (md2docx) en la carpeta de entrada y volver a ejecutar.
- Codigos de salida: 0 correcto; 1 alguna conversion fallo (ver errores); 2 falta una dependencia: mostrar al usuario la instruccion de instalacion que imprime el script.
- Si el script informa archivos "Omitido (ya existe...)", preguntar al usuario si desea sobrescribirlos; si acepta, repetir con `--force`.
- En md2docx, con `mmdc` disponible los bloques Mermaid se incrustan como imagen; si no, quedan como codigo.
- Informar las rutas de los archivos generados. Leer los `.md` generados y acordar con el usuario el siguiente flujo (documento-desarrollo, revision-doc o documentacion puntual) y como se usara el contenido importado.

## Instrucciones especificas
- Funciones/clases/modulos: que hace, parametros, retorno y, cuando sea util, un ejemplo minimo.
- README o guias: sugerir solo las secciones que aplican al proyecto; evitar secciones genericas vacias.
- Comentarios en codigo: explicar el por que de las decisiones importantes y mantenerlos sincronizados con el codigo.

## Colaboracion
- Explicar brevemente los cambios antes de modificar documentacion de forma extensa.
- Si se modifican 3 o mas archivos o un archivo de raiz (README/CHANGELOG/CONTRIBUTING), incluir un resumen final de archivos tocados y su proposito.
- Respetar el estilo existente del proyecto.

## Limites
- No introducir opiniones personales ajenas al proyecto.
- No inventar detalles tecnicos: si algo no esta claro, pedir aclaracion o marcarlo como `[FALTA DETALLE SOBRE X]`.
