# Λόγος

Themes with minimal monochrome syntax colors and calm UI.
An attempt is made to balance prettiness with simplicity and usability.

## About

I find most multicolored syntax themes to be garish and overwhelming to look at for extended periods of time.
These themes use bold text and a few shades of a primary "base" color to highlight:
- keywords
- comments
- strings
- constants
- global definitions

## Variants

| variant   | type  | description                                                                         |
| --------- | ----- | ----------------------------------------------------------------------------------- |
| white     | light | core light theme with white background                                              |
| tree      | light | off-white variant of the white theme                                                |
| paper     | light | inspired by the [Flatwhite](https://github.com/biletskyy/flatwhite-syntax) theme    |
| acme      | light | inspired by the [Acme editor](https://en.wikipedia.org/wiki/Acme_%28text_editor%29) |
| dark      | dark  | inspired by the [Gruvbox](https://github.com/morhetz/gruvbox) themes, desaturated   |
| dark-warm | dark  | inspired by the [Gruvbox](https://github.com/morhetz/gruvbox) themes                |
| nord      | dark  | inspired by the [Nord](https://www.nordtheme.com) theme                             |
| red       | dark  | dark with red text for very low light                                               |

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