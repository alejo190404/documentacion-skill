<!-- Estructura y texto fijo tomados de plantilla.docx (Diseño detallado y desarrollo). Cada marcador PROMPT tiene un id en prompts/documento-desarrollo.prompts.md. Los valores {campo} se sustituyen por datos reales al generar el documento. -->
<!-- PROMPT: encabezado -->
|  | Documento Diseño detallado y desarrollo | Versión: 1 |
|---|---|---|
| **MANUAL DE PROCEDIMIENTOS** | {codigoRequerimiento} – {tituloRequerimiento} | Fecha: {fechaElaboracion} |
|  | División de Tecnología |  |

# CONTROL DE VERSIONES

<!-- PROMPT: control-versiones -->
| **VERSION** | **FECHA** | **MODIFICACIÓN** | **RESPONSABLE** | **DIVULGACIÓN/ REGLAMENTACIÓN** |
|:---:|:---:|:---:|:---:|:---:|
| 1.0 | {fechaElaboracion} | Creación documento | {nombreResponsable} |  |

# APROBACIONES DEL COMITÉ DE DISEÑO DETALLADO

A continuación se deben listar las personas que aprueban el diseño detallado del requerimiento para poder dar paso al desarrollo del mismo.

Comités de diseño:

- Diseño detallado: Aprobaciones por COE (para el caso de servicios), director o coordinador, Infraestructura, Arquitectura, Seguridad de la Información en caso que hayan participado en el requerimiento

<!-- PROMPT: aprobaciones -->
| **SECCIÓN** | **NOMBRE Y APELLIDO** | **CARGO Y ÁREA** | **FECHA DE APROBACIÓN** |
|:---:|:---:|:---:|:---:|
| Diseño detallado | {nombreCoordinador} | Coordinador Chapter Backend Satélites |  |

# TABLA DE CONTENIDO

- [CONTROL DE VERSIONES](#control-de-versiones)
- [APROBACIONES DEL COMITÉ DE DISEÑO DETALLADO](#aprobaciones-del-comité-de-diseño-detallado)
- [TABLA DE CONTENIDO](#tabla-de-contenido)
- [INTRODUCCIÓN](#introducción)
- [1. DESCRIPCIÓN](#1-descripción)
- [2. DISEÑO DETALLADO](#2-diseño-detallado)
  - [2.1. PROCESOS DE DEPURACIÓN](#21-procesos-de-depuración)
  - [2.2. COPIAS DE SEGURIDAD O BACKUP](#22-copias-de-seguridad-o-backup)
- [3. DESARROLLO DEL REQUERIMIENTO (Si aplica)](#3-desarrollo-del-requerimiento-si-aplica)
  - [3.1. DETALLAR COMPONENTES ADICIONALES](#31-detallar-componentes-adicionales)
  - [3.2. DETALLAR FUNCIONALIDADES](#32-detallar-funcionalidades)
- [4. ANEXOS](#4-anexos)
- [5. VERIFICACIONES ADICIONALES](#5-verificaciones-adicionales)
- [6. CASOS DE PRUEBAS UNITARIAS](#6-casos-de-pruebas-unitarias)

# INTRODUCCIÓN

Este documento tiene como objetivo representar la solución al requerimiento de manera detallada en una aplicación específica con sus dependencias, entradas y salidas. Así como los casos de pruebas unitarias realizadas en la solución.

NOTA: El desarrollo de cualquier solución de requerimiento debe seguir los estándares de desarrollo que define Arquitectura.

Link: [TI - Plantilla Arquitectura e Infraestructura](http://wiki/svn/TI-%20Procesos%20y%20Metodologia/Manual%20Procesos%20de%20TI/Documentos/DS%20-%20Desarrollar%20e%20Implementar%20Productos/Plantillas/DS02%20-%20Dise%c3%b1ar%20requerimiento/TI%20-%20Plantilla%20Arquitectura%20e%20Infraestructura.dot)

**Objetivo**

- Presentar los componentes que serán consultados, modificados, creados y/o eliminados en la solución del requerimiento
- Especificar como se resuelven las necesidades relacionadas con backups, recuperación de datos y procesos de depuración de información.

**Incluir:**

- Aplicaciones relacionadas.
- Componentes afectados (nuevos, modificados, eliminados).
- Almacenamiento de información.
- Disponibilidad de información.
- Interacción entre aplicaciones.

# 1. DESCRIPCIÓN

**Descripción del requerimiento:**

<!-- PROMPT: descripcion -->

# 2. DISEÑO DETALLADO

<!-- PROMPT: diseno-detallado -->
**{repositorio}**\
**Componente:** {nombre}\
**Tipo:** {tipo}

| **Archivo** | **Tipo Cambio** | **Descripción** |
|---|---|---|
| {archivo} | {tipoCambio} | {descripcionCambio} |

## 2.1. PROCESOS DE DEPURACIÓN

Durante la etapa de diseño del requerimiento se debe contemplar aquellas tablas, archivos, objetos o cualquier otro componente que debiera ser depurado periódicamente con el fin de evitar complicaciones afectando la disponibilidad del aplicativo involucrado.

<!-- PROMPT: procesos-depuracion -->
|  |  |
|---|---|
| **Tabla / Objeto / Archivo:** | ***NA*** |
| **Descripción:** | ***NA*** |
| **Tipo de Depuración:** | ***NA*** |
| **Periodicidad:** | ***NA*** |
| **Descripción breve del proceso de depuración:** | ***NA*** |

## 2.2. COPIAS DE SEGURIDAD O BACKUP

<!-- PROMPT: copias-seguridad -->
|  |  |
|---|---|
| **Objeto de respaldo:** | ***NA*** |
| **Descripción de la información:** | ***NA*** |
| **Tipo de backup:** | ***NA*** |
| **Frecuencia:** | ***NA*** |
| **Días de ejecución:** | ***NA*** |
| **Hora de ejecución:** | ***NA*** |
| **Retención:** | ***NA*** |

# 3. DESARROLLO DEL REQUERIMIENTO (Si aplica)

## 3.1. DETALLAR COMPONENTES ADICIONALES

<!-- PROMPT: componentes-adicionales -->
| **Nombre del componente** | **Tipo** |
|:---:|:---:|
|  |  |

## 3.2. DETALLAR FUNCIONALIDADES

<!-- PROMPT: detallar-funcionalidades -->
- **Lista de Programas, archivos, paquetes**
- **Lista de modificaciones hacia la bases de datos *(Si incluyen script´s dilgenciar)***
- **Lista de Script´s y la descripción de lo que contiene cada uno.**
- **Parametrizaciones de la aplicación**
- **Documentación de Arquitectura**

# 4. ANEXOS

<!-- PROMPT: anexos -->
| **ANEXOS Y REFERENCIAS** |  |
|:---:|:---:|
| **CÓDIGO** | **DESCRIPCION** |
|  |  |

# 5. VERIFICACIONES ADICIONALES

<!-- PROMPT: verificaciones-adicionales -->

# 6. CASOS DE PRUEBAS UNITARIAS

<!-- PROMPT: casos-pruebas-unitarias -->
| **ID** | **CASO DE PRUEBA** | **RESULTADO ESPERADO** | **APROBADO** |
|:---:|:---:|:---:|:---:|
| *{id}* | *{descripcion}* | *{resultado}* | *{aprobado}* |

---

Banco de Occidente – USO INTERNO
