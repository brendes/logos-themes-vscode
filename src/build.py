#!/usr/bin/env python3
import argparse
import json
import re
import tomllib
from pathlib import Path

from coloraide import Color

SRC = Path("src")
OUT_VSC = Path("themes") / "vscode"

MIX_RE = re.compile(r"mix\((#[0-9a-fA-F]{6}),(#[0-9a-fA-F]{6}),([\d.]+)\)")
ALPHA_RE = re.compile(r"alpha\(([\d.]+)\)")


def _strip_jsonc(s):
    """Strip // and /* */ comments outside of strings."""
    out = []
    i, n, in_str = 0, len(s), False
    while i < n:
        c = s[i]
        if in_str:
            out.append(c)
            if c == "\\":
                i += 2
                continue
            if c == '"':
                in_str = False
            i += 1
        elif c == '"':
            in_str = True
            out.append(c)
            i += 1
        elif c == "/" and i + 1 < n and s[i + 1] == "/":
            while i < n and s[i] != "\n":
                i += 1
        elif c == "/" and i + 1 < n and s[i + 1] == "*":
            i += 2
            while i + 1 < n and not (s[i] == "*" and s[i + 1] == "/"):
                i += 1
            i += 2
        else:
            out.append(c)
            i += 1
    return "".join(out)


def load_jsonc(path):
    """Parse JSONC as a dict."""
    s = _strip_jsonc(path.read_text())
    s = re.sub(r",(\s*[}\]])", r"\1", s)
    return json.loads(s)


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


def theme_vars(palette, theme, overrides=None):
    d = {}
    d.update(theme["base"])
    d.update(theme[palette["type"]])
    d.update(palette)
    if overrides:
        d.update(overrides)

    resolve_vars(d)
    eval_funcs(d)
    return d


def merge_hc_template(main_template, hc_template):
    """Merge a high-contrast vscode theme template onto the main template."""
    main = load_jsonc(main_template)
    hc = load_jsonc(hc_template)
    merged = dict(main)
    colors = dict(main.get("colors", {}))
    colors.update(hc.get("colors", {}))
    merged["colors"] = colors
    merged.pop("include", None)
    return json.dumps(merged, indent=2)


def build_theme(*, palette, theme, template, overrides=None):
    """Resolve vars for one palette and substitute into a template string."""
    d = theme_vars(palette, theme, overrides)
    out = template
    for k, v in d.items():
        out = out.replace("{" + k + "}", v)
    return out


def build_vsc_theme(*, name, palette, theme, template):
    """Build one vscode theme."""
    out = build_theme(palette=palette, theme=theme, template=template)
    OUT_VSC.mkdir(parents=True, exist_ok=True)
    (OUT_VSC / f"{name}-color-theme.json").write_text(out + "\n")


def build_hc_theme(*, key, hc, palette, theme, template):
    """Build one vscode high-contrast theme from a [hc.<key>] entry.

    `template` is the high-contrast template merged onto the main template at
    build time.
    """
    overrides = {**theme.get("hc_base", {}), **hc}
    out = build_theme(
        palette=palette, theme=theme, template=template, overrides=overrides
    )
    OUT_VSC.mkdir(parents=True, exist_ok=True)
    (OUT_VSC / f"{key}-hc-color-theme.json").write_text(out + "\n")


def main(theme_path=SRC / "colors.toml"):
    theme = tomllib.loads(theme_path.read_text())
    vsc_template = (SRC / "vscode" / "template.json").read_text()
    hc_template = merge_hc_template(
        SRC / "vscode" / "template.json", SRC / "vscode" / "hc-template.json"
    )
    for name, palette in theme["palettes"].items():
        build_vsc_theme(name=name, palette=palette, theme=theme, template=vsc_template)
    for key, hc in theme.get("hc", {}).items():
        palette = theme["palettes"][key]
        build_hc_theme(
            key=key, hc=hc, palette=palette, theme=theme, template=hc_template
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build Logos themes.")
    parser.add_argument(
        "theme",
        nargs="?",
        default="src/colors.toml",
        help="path to colors.toml (default: src/colors.toml)",
    )
    args = parser.parse_args()
    main(theme_path=Path(args.theme))
