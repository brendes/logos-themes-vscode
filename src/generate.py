from colors import base_colors, colors


def generate_theme(theme_config):
    type = theme_config["type"]
    base = None
    for bc in base_colors:
        if bc["type"] == type:
            base = bc
            break
    theme = {**base, **theme_config}
    theme.update(
        {
            "bg_main": theme["base_0"],
            "bg_subtle": theme["base_1"],
            "bg_ui": theme["base_1"],
            "bg_fade": theme["base_2"],
            "bg_hl": theme["base_3"],
            "bg_sel": theme["base_3"] + "ee",
            "bg_strong": theme["base_4"],
            "bg_drop": theme["base_3"] + "88",
            "fg_main": theme["base_6"],
            "fg_bold": theme["base_7"],
            "black_2": theme["base_5"],
        }
    )
    if theme["type"] == "light":
        theme.update(_set_light_theme_colors(theme))
    else:
        theme.update(_set_dark_theme_colors(theme))

    return theme


def _set_light_theme_colors(theme):
    return {
        "fg_ghost": theme["fg_main"] + "18",
        "fg_faint": theme["fg_main"] + "33",
        "fg_dim": theme["fg_main"] + "78",
        "fg_subtle": theme["fg_main"] + "98",
        "fg_ui": theme["fg_main"] + "98",
        "bg_bold": theme["base_5"],
        "bg_hover": theme["bg_fade"],
        "bg_widget": theme["bg_main"],
        "bg_match_1": theme.get("match_1", "#f8e0bb") + "ee",
        "bg_match_2": theme.get("match_2", "#d0e0f8") + "ee",
        "border_hard": theme["fg_main"] + "88",
        "border_medium": theme["fg_main"] + "40",
        "border_soft": theme["fg_main"] + "28",
        "border_popup": theme["fg_main"] + "88",
        "border_ui": theme["fg_main"] + "28",
        "black_1": theme["fg_main"],
        "white_2": theme["bg_main"],
        "link": theme.get("blue_bold", theme["blue_1"]),
        "code": theme["magenta_1"],
    }


def _set_dark_theme_colors(theme):
    colors = {
        "fg_ghost": theme["fg_main"] + "28",
        "fg_faint": theme["fg_main"] + "48",
        "fg_dim": theme["fg_main"] + "88",
        "fg_subtle": theme["fg_main"] + "b8",
        "fg_ui": theme["fg_main"] + "b8",
        "bg_bold": theme["base_6"],
        "bg_hover": theme["bg_hl"],
        "bg_widget": theme["bg_fade"],
        "bg_match_1": theme["magenta_1"] + "bb",
        "bg_match_2": theme["cyan_1"] + "bb",
        "border_hard": theme["fg_main"] + "68",
        "border_medium": theme["fg_main"] + "48",
        "border_soft": theme["fg_main"] + "28",
        "border_popup": theme["bg_fade"],
        "border_ui": theme["bg_subtle"],
        "black_1": theme["bg_main"],
        "white_2": theme["fg_main"],
        "link": theme["cyan_1"],
        "code": theme["magenta_1"],
    }
    for color in [
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "orange",
        "purple",
    ]:
        key_2 = f"{color}_2"
        key_1 = f"{color}_1"
        if key_1 in theme and key_2 not in theme:
            colors[key_2] = theme[key_1]

    return colors


def generate_all_themes():
    return [generate_theme(config) for config in colors]
