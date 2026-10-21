# Safari Gaucho (antes 4x4 Natural)

Un juego de **Insight Reality**.

Manejá una 4x4 por la sierra y el humedal del este de Uruguay y fotografiá los bichos donde viven. Algunos están a la vista; otros, en lugares que hay que encontrar: una quebrada con cascada, una cueva con pinturas, una laguna escondida.

Pensado para chicos de 7 a 12 años: naturaleza uruguaya, un cuaderno de campo con información real y un toque de lo indígena como puerta a lo espiritual humano.

## Jugar
- Abrí `index.html` en el navegador, o publicá la carpeta con GitHub Pages.
- Es una app web instalable (Chrome/Edge en PC y Android; Safari en iPhone/iPad con "Agregar a inicio") y funciona sin conexión.

## Estructura
- `index.html` — el juego completo (Three.js, todo generado con código: paisaje, animales, plantas y sonidos).
- `manifest.webmanifest`, `sw.js`, `icons/` — instalación como app y modo sin conexión.
- `versiones/` — cada versión guardada (v01…v12), y `CAMBIOS.md` con lo que trae cada una.

## Cómo se hizo
Idea, diseño y dirección: Insight Reality. Programado conversando con Claude (Anthropic).

## Licencia
© 2026 Insight Reality. Todos los derechos reservados. El repositorio es público para consulta y para publicar el juego, pero no es código abierto: ver `LICENSE`.


## Ramas
- `main`: el juego publicado.
- `playa`: versión con costa atlántica (dunas, playa, mar y laguna costera), en desarrollo. Incluye `prueba-mar.html`.
