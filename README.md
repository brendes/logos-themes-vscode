# Λόγος

Monochrome themes with minimal syntax highlighting and calm UI.
An attempt is made to balance simplicity with usability.

## About

I find most multicolored syntax themes to be garish and overwhelming to look at for extended periods of time.
These themes use bold text and a few shades of a primary "base" color to highlight:
- comments
- strings
- constants

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

Examples can be viewed at [vscodethemes.com](https://vscodethemes.com/e/brendes.logos-themes/logos-white).

At the time of writing this, I update the theme frequently. I don't know how often the site syncs its themes but this will do for now.

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