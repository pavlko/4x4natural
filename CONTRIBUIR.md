# Cómo sumar bichos, lugares y más

Todo el juego está en un solo archivo: `index.html`. No hace falta instalar nada: lo abrís en el navegador y listo. Para publicar tu versión, hacé un *fork* de este repositorio y activá GitHub Pages.

## Trabajar con una IA
Este juego se hizo conversando con una inteligencia artificial (Claude). Podés hacer lo mismo:
1. Dale el archivo `index.html` y contale qué querés agregar, con detalles reales: cómo es el bicho, dónde vive, qué hace, cómo suena.
2. Pedile cambios chicos de a uno y probalos en el navegador.
3. Si algo no anda, mandale una captura de pantalla y contale qué esperabas ver.

## Dónde está cada cosa (buscá estas palabras en el archivo)
- **`const SPECIES=[`** — la lista de bichos. Cada uno tiene: `id`, `name` (nombre común), `sci` (nombre científico), `hab` (`land` camina, `perch` se posa, `hop` vuela entre perchas, `water`…), `shy` (cuánto se asusta), `hint` (la pista del cuaderno), `note` y `more` (lo que cuenta la tarjeta).
- **`BUILD.<id>=`** — cómo se dibuja cada bicho con formas simples.
- **`spawn(sp,x,z)`** — dónde aparece cada bicho en el mundo (buscá el `id` del bicho).
- **`const CALLS={`** y **`CALL_R`** — el sonido de cada bicho (sintetizado) y desde qué distancia se oye.
- **`const G={carpincho:`** — en qué pestaña del cuaderno va cada bicho (aves, mamíferos, reptiles, anfibios, invertebrados); los nombres de las pestañas están en **`GRPN`**.
- **`const PLACES=[`** — los lugares para descubrir.
- **`const SPECIALS=`**, **`SP_LABEL`** — las fotos especiales (por ejemplo, un bicho con su nido).
- **`function MEDALS()`** — los logros.
- **`DIVES`**, **`FISH`** — puntos de buceo y peces. **`MICRO`**, **`MSITES`** — el microscopio y sus muestras.
- **`function baseH(`** — la forma del terreno.

## Herramientas para revisar
- **Galería** (modo colaborador, o `?galeria` en la dirección): todos los bichos, peces, plantas, pinturas y objetos en 3D, con fotos reales de iNaturalist y Wikimedia al lado.
- **`herramientas/capturas.py`**: saca capturas de la interfaz en distintas pantallas y arma una hoja para detectar solapamientos.
- **Plantas por definir**: en la galería, las que dicen «?» esperan que alguien proponga la especie local correcta.

## Ideas para empezar
- Un bicho de tu zona, con su sonido y su lugar.
- Un hallazgo local: una historia, un objeto, una pintura.
- Un logro divertido o una foto especial (un bicho comiendo, con cría, en vuelo).
- Un ambiente nuevo: otra costa, un monte, una montaña, otro país.

## Cuidados
- El progreso de los jugadores se guarda en su navegador. Si cambiás el `id` de un bicho o de un lugar, quienes ya lo tenían lo pierden: mejor cambiar solo el `name`.
- Usá información real y revisada sobre los animales; en el cuaderno se aprende.
- Si mandás tus cambios a este repositorio (*pull request*), contá qué agregaste y por qué.
