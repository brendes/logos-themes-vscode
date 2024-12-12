#!/usr/bin/env python3

base_colors = {
    "light": {
        "theme_type": "light",
        "red_1": "#bb5555",
        "red_2": "#e89090",
        "orange_1": "#d08868",
        "orange_2": "#f0ccb0",
        "yellow_1": "#aa8877",
        "yellow_2": "#eed8bb",
        "green_1": "#779955",
        "green_2": "#b0c088",
        "blue_1": "#6680cc",
        "blue_2": "#bbccdd",
        "magenta_1": "#aa7788",
        "magenta_2": "#d8b8c8",
        "cyan_1": "#77aaaa",
        "cyan_2": "#b8dbd4",
        "invisible": "#00000000",
    },
    "dark": {
        "theme_type": "dark",
        "red_1": "#f87870",
        "orange_1": "#dda288",
        "yellow_1": "#ddb848",
        "green_1": "#a9b665",
        "blue_1": "#80a8b0",
        "magenta_1": "#d3889b",
        "cyan_1": "#88b4a0",
        "invisible": "#00000000",
    },
}

themes = {
    "white": {
        **base_colors["light"],
        "theme_name": "Logos White",
        "base_0": "#ffffff",
        "base_1": "#f8f8f8",
        "base_2": "#f4f4f4",
        "base_3": "#eaeaea",
        "base_4": "#cccccc",
        "base_5": "#787878",
        "base_6": "#000000",
        "base_7": "#000000",
    },
    "sun": {
        **base_colors["light"],
        "theme_name": "Logos Sun",
        "base_0": "#fffffa",
        "base_1": "#f8f8f3",
        "base_2": "#f4f4ef",
        "base_3": "#e8e8e3",
        "base_4": "#ccccc9",
        "base_5": "#787873",
        "base_6": "#000000",
        "base_7": "#000000",
    },
    "acme": {
        **base_colors["light"],
        "theme_name": "Logos Acme",
        "base_0": "#ffffea",
        "base_1": "#f8f8e3",
        "base_2": "#f4f4df",
        "base_3": "#e8e8d3",
        "base_4": "#d8d8c3",
        "base_5": "#787870",
        "base_6": "#000000",
        "base_7": "#000000",
        "red_1": "#bb5d5d",
        "red_2": "#ee9999",
        "yellow_1": "#998866",
        "yellow_2": "#eeee9e",
        "green_1": "#448844",
        "green_2": "#bbddbb",
        "blue_1": "#5555cc",
        "blue_2": "#ccccff",
        "magenta_1": "#aa77aa",
        "magenta_2": "#ddbbdd",
        "cyan_1": "#66aaaa",
        "cyan_2": "#addddd",
    },
    "dark": {
        **base_colors["dark"],
        "theme_name": "Logos Dark",
        "base_0": "#282828",
        "base_1": "#303030",
        "base_2": "#343434",
        "base_3": "#444444",
        "base_4": "#666666",
        "base_5": "#cccccc",
        "base_6": "#d8d8d8",
        "base_7": "#ffffff",
    },
        "gruv": {
        **base_colors["dark"],
        "theme_name": "Logos Gruv",
        "base_0": "#32302f",
        "base_1": "#3a3837",
        "base_2": "#403d3c",
        "base_3": "#4c4948",
        "base_4": "#595654",
        "base_5": "#c8c0b8",
        "base_6": "#e0d0bb",
        "base_7": "#f8f5f1",
    },
    "nord": {
        **base_colors["dark"],
        "theme_name": "Logos Nord",
        "base_0": "#2e3440",
        "base_1": "#363d4c",
        "base_2": "#3c4352",
        "base_3": "#434c5e",
        "base_4": "#576279",
        "base_5": "#abb3c2",
        "base_6": "#d8dee9",
        "base_7": "#e8eef9",
        "red_1": "#bf616a",
        "orange_1": "#d08770",
        "green_1": "#a3be8c",
        "yellow_1": "#ebcb8b",
        "blue_1": "#81a1c1",
        "magenta_1": "#b48ead",
        "cyan_1": "#88c0d0",
    }
}

for theme_name, theme in themes.items():
    theme["bg_main"] = theme["base_0"]
    theme["bg_subtle"] = theme["base_1"]
    theme["bg_ui"] = theme["base_1"]
    theme["bg_fade"] = theme["base_2"]
    theme["bg_hl"] = theme["base_3"]
    theme["bg_sel"] = theme["base_3"] + "ee"
    theme["bg_strong"] = theme["base_4"]
    theme["bg_bold"] = theme["base_5"]
    theme["bg_drop"] = theme["bg_hl"] + "88"
    theme["fg_main"] = theme["base_6"]
    theme["fg_bold"] = theme["base_7"]

    if theme.get("theme_type") == "light":
        theme["fg_faint"] = theme["fg_main"] + "33"
        theme["fg_fade"] = theme["fg_main"] + "5c"
        theme["fg_dim"] = theme["fg_main"] + "88"
        theme["fg_subtle"] = theme["fg_main"] + "a8"
        theme["bg_match_1"] = theme["bg_strong"] + "ee"
        theme["bg_match_2"] = theme["yellow_2"] + "dd"
        theme["border_hard"] = theme["fg_main"] + "88"
        theme["border_soft"] = theme["fg_main"] + "28"
        theme["black_1"] = theme["fg_main"]
        theme["white_2"] = theme["bg_main"]
        theme["link"] = theme["blue_1"]

    elif theme.get("theme_type") == "dark":
        theme["fg_faint"] = theme["fg_main"] + "48"
        theme["fg_fade"] = theme["fg_main"] + "80"
        theme["fg_dim"] = theme["fg_main"] + "a8"
        theme["fg_subtle"] = theme["fg_main"] + "c8"
        theme["bg_match_1"] = theme["bg_strong"] + "ee"
        theme["bg_match_2"] = theme["orange_1"] + "78"
        theme["border_hard"] = theme["fg_main"] + "98"
        theme["border_soft"] = theme["fg_main"] + "28"
        theme["black_1"] = theme["bg_main"]
        theme["white_2"] = theme["fg_main"]
        theme["link"] = theme["cyan_1"]
        for color in [
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "orange",
        ]:
            theme[f"{color}_2"] = theme[f"{color}_1"]
