#!/usr/bin/env python3
import re
import tomllib
from pathlib import Path

from coloraide import Color

SRC = Path("src")
OUT = Path("themes")

MIX_RE = re.compile(r"mix\((#[0-9a-fA-F]{6}),(#[0-9a-fA-F]{6}),([\d.]+)\)")
ALPHA_RE = re.compile(r"alpha\(([\d.]+)\)")


def resolve_vars(d):
    """Fixed-point {var} expansion — a value can reference a var whose own
    value is itself unresolved, so one pass over all keys isn't enough."""
    for _ in range(10):
        changed = False
        for k in d:
            for j in d:
                token = "{" + j + "}"
                if token in d[k]:
                    d[k] = d[k].replace(token, d[j])
                    changed = True
        if not changed:
            break


def eval_mix(m):
    c1, c2, pct = m.group(1), m.group(2), float(m.group(3))
    mixed = Color(c1).mix(c2, pct / 100, space="oklab")
    return mixed.convert("srgb").to_string(hex=True)


def eval_alpha(m):
    pct = float(m.group(1))
    return f"{round(pct / 100 * 255):02x}"


def eval_funcs(d):
    for k in d:
        d[k] = MIX_RE.sub(eval_mix, d[k])
        d[k] = ALPHA_RE.sub(eval_alpha, d[k])


def build_theme(name, palette, theme, template):
    d = {}
    d.update(theme["base"])
    d.update(theme[palette["type"]])
    d.update(palette)

    resolve_vars(d)
    eval_funcs(d)

    out = template
    for k, v in d.items():
        out = out.replace("{" + k + "}", v)

    OUT.mkdir(exist_ok=True)
    (OUT / f"{name}-color-theme.json").write_text(out + "\n")


def main():
    theme = tomllib.loads((SRC / "theme.toml").read_text())
    template = (SRC / "lib" / "template.json").read_text()
    for name, palette in theme["palettes"].items():
        build_theme(name, palette, theme, template)


if __name__ == "__main__":
    main()
