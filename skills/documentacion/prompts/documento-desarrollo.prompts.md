# Prompts del documento de desarrollo (Diseño detallado y desarrollo)

Reglas comunes:
- Cuando el marcador va seguido de una tabla, completar esa tabla: sustituir los valores `{campo}` y agregar filas si hace falta. No cambiar encabezados, columnas ni texto fijo de la plantilla.
- Un dato que no se pueda obtener del contexto, del codigo ni del diff se marca `[FALTA DETALLE SOBRE X]`. No inventar nombres, fechas ni cargos.
- Una seccion que no aplica al requerimiento conserva `NA`.

## encabezado
Completa la tabla de encabezado: `{codigoRequerimiento}` (codigo del requerimiento o historia, por ejemplo el id del ticket), `{tituloRequerimiento}` (titulo corto) y `{fechaElaboracion}` (fecha de elaboracion, formato DD/MM/AAAA; por defecto, la fecha actual).

## control-versiones
Completa la fila de la version 1.0 con `{fechaElaboracion}` y `{nombreResponsable}` (quien elabora el documento; si no se conoce, usar el autor de los commits del diff). Si el documento se actualiza, agrega una fila con la nueva version, fecha, modificacion y responsable. La columna DIVULGACIÓN/ REGLAMENTACIÓN queda vacia salvo que el usuario la indique.

## aprobaciones
Sustituye `{nombreCoordinador}` por el nombre del coordinador del Chapter Backend Satelites que aprueba el diseño. Agrega una fila por cada aprobador adicional que indique el usuario (COE, director, Infraestructura, Arquitectura, Seguridad de la Informacion) con su cargo y area. La fecha de aprobacion queda vacia.

## descripcion
Describe el requerimiento en uno a tres parrafos: necesidad de negocio, que se construye o modifica, aplicaciones relacionadas, interaccion entre aplicaciones y alcance. Basarse en el contexto del usuario (historia, epic, ticket) y en el codigo.

## diseno-detallado
Repite el bloque (repositorio, componente, tipo y tabla de archivos) una vez por cada componente afectado. `{repositorio}`: nombre del repositorio; `{nombre}`: componente (servicio, modulo, job, libreria); `{tipo}`: tipo de componente (por ejemplo: Microservicio, API, Batch, Libreria, Base de datos, Frontend). En la tabla, una fila por archivo afectado: ruta relativa del archivo, tipo de cambio (Nuevo, Modificado o Eliminado) y una descripcion breve de que cambia y por que. Si hay repositorio Git, tomar los archivos del diff entre la rama base y la rama de trabajo. Agregar un diagrama Mermaid despues de los componentes solo si el requerimiento describe una arquitectura, un flujo o una secuencia entre componentes.

## procesos-depuracion
Si el requerimiento crea tablas, archivos, logs u objetos que crecen y deben depurarse periodicamente, reemplaza cada `NA` con: el objeto, su descripcion, el tipo de depuracion (manual, automatica, por script, por job), la periodicidad y una descripcion breve del proceso. Repetir la tabla por cada objeto. Si no aplica, dejar `NA`.

## copias-seguridad
Si el requerimiento almacena informacion que necesita respaldo, reemplaza cada `NA` con: objeto de respaldo, descripcion de la informacion, tipo de backup (completo, incremental, diferencial), frecuencia, dias y hora de ejecucion y retencion. Repetir la tabla por cada objeto. Si no aplica, dejar `NA`.

## componentes-adicionales
Lista los componentes adicionales que no se detallaron en la seccion 2 (dependencias nuevas, configuraciones de infraestructura, colas, topicos, jobs, certificados) con su nombre y tipo, una fila por componente. Si no hay, dejar la fila vacia.

## detallar-funcionalidades
Desarrolla cada viñeta de la plantilla con sub-viñetas: programas, archivos y paquetes entregados; modificaciones a bases de datos (tablas, columnas, indices) y los scripts que las aplican; lista de scripts con la descripcion de su contenido; parametrizaciones de la aplicacion (variables, propiedades, feature flags y sus valores por ambiente); documentacion de Arquitectura (enlaces o referencias). Escribir `NA` bajo la viñeta que no aplique.

## anexos
Lista anexos y referencias, una fila por elemento: codigo (identificador del anexo, ticket, documento o enlace) y descripcion. Incluir el ticket del requerimiento y documentos o enlaces relevantes. Si no hay, dejar la fila vacia.

## verificaciones-adicionales
Describe verificaciones adicionales a las pruebas unitarias (pruebas de integracion, revisiones de seguridad, analisis estatico, validaciones funcionales, revision de rendimiento) y su resultado. Si no hay, escribir `NA`.

## casos-pruebas-unitarias
Una fila por caso de prueba unitaria: `{id}` (por ejemplo CP-01), `{descripcion}` (que se prueba), `{resultado}` (resultado esperado) y `{aprobado}` (Si/No). Obtener los casos de las pruebas existentes en el repositorio o del diff; si no hay pruebas, proponer casos para los cambios documentados y dejar Aprobado como `[FALTA DETALLE SOBRE resultado de ejecucion]`.
