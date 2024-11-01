# Λόγος

Themes with minimal monochrome syntax highlighting and calm UI.

## About

I find most multicolored syntax themes to be garish and not nice to look at for extended periods of time.
Additionally, most UI themes use so many different colors and shades that it becomes distracting.

These themes use a few shades of a primary "base" color to highlight:
1. comments,
2. strings,
3. and constants. 

Each theme has a set of accent colors that are used sparingly to distinguish salient UI elements.
Overall, an attempt is made to balance simplicity with usability.

## Theme variants

| variant | type  | description                   |
| ------- | ----- | ----------------------------- |
| white   | light | neutral theme                 |
| sun     | light | off-white theme               |
| paper   | light | even more off-white           |
| acme    | light | yellow theme                  |
| dark    | dark  | neutral theme                 |
| gruv    | dark  | warm dark theme               |
| nord    | dark  | cool dark theme               |
| red     | dark  | very dark theme with red text |

## Screenshots

Here is a screenshot of some Go code using the `Logos White` theme.

<img src="./assets/screenshot-go.png" alt="go code screenshot" width="800"/>

Auto-generated examples can be viewed at [vscodethemes.com](https://vscodethemes.com/e/brendes.logos-themes/logos-white).
The website renders the themes a little inaccurately, but it will do for now.

## Install
- In VS Code: `⌘-P` then `ext install logos-themes`
- On the web: https://marketplace.visualstudio.com/items?itemName=brendes.logos-themes

## Build

Requires Python ≥ 3.11.
- Build themes: `make build`
- Build extension: `make package`

## Credits/inspiration
- [Acme editor](https://en.wikipedia.org/wiki/Acme_%28text_editor%29)
- [Flatwhite](https://github.com/biletskyy/flatwhite-syntax)
- [Gruvbox](https://github.com/morhetz/gruvbox)
- [Nord](https://www.nordtheme.com)