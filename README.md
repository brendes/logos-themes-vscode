# Λόγος

Themes using monochrome shades for syntax and calm UI colors.
An attempt is made to balance prettiness with simplicity and usability.

## About

I find syntax highlighting that uses few colors to be less confusing than one
that uses many colors.
After playing with different schemes, I realized that I get least tired of
looking at the same colors all the time when I use monochrome syntax
highlighting.
I care less about the exact meaning of each color (and often can't be bothered
to memorize them) than I do about being able to scan the shape and structure of
the code.

## Variants

| variant        | type  | base color | description                                                                         |
| -------------- | ----- | ---------- | ----------------------------------------------------------------------------------- |
| logos-white     | light | `#ffffff`  |                                                                                     |
| logos-tree      | light | `#fffffa`  | based on logos-white                                                                 |
| logos-paper     | light | `#faf8f1`  | inspired by the [Flatwhite](https://github.com/biletskyy/flatwhite-syntax) theme    |
| logos-acme      | light | `#ffffee`  | inspired by the [Acme editor](https://en.wikipedia.org/wiki/Acme_%28text_editor%29) |
| logos-dark      | dark  | `#2f2f2f`  | inspired by the [Gruvbox](https://github.com/morhetz/gruvbox) themes, desaturated   |
| logos-dark-warm | dark  | `#32302f`  | inspired by the [Gruvbox](https://github.com/morhetz/gruvbox) themes                |
| logos-nord      | dark  | `#2e3440`  | inspired by the [Nord](https://www.nordtheme.com) theme                             |

## Build
```
make build
make package
```
Requires Python ≥ 3.11.

## TODO

- screenshots