#!/usr/bin/env python3

white = {
    "theme_type": "light",
    "theme_name": "Logos White",
    "base_0": "#ffffff",
    "base_1": "#f8f8f8",
    "base_2": "#f2f2f2",
    "base_3": "#e8e8e8",
    "base_4": "#000000",
    "base_5": "#000000",
    "fg_accent": "#6078aa",
    "bg_accent": "#bbd0e8",
    "red_1": "#bb5555",
    "red_2": "#e89090",
    "orange_1": "#d08868",
    "orange_2": "#f0ccb0",
    "yellow_1": "#aa8877",
    "yellow_2": "#eed8bb",
    "green_1": "#779955",
    "green_2": "#b0c088",
    "blue_1": "#6677aa",
    "blue_2": "#bbd0e8",
    "magenta_1": "#aa7788",
    "magenta_2": "#d8b8c8",
    "cyan_1": "#77aaaa",
    "cyan_2": "#b8dbd4",
    "invisible": "#00000000",
}

sun = {
    **white,
    "theme_name": "Logos Sun",
    "base_0": "#fffffa",
    "base_1": "#f8f8f3",
    "base_2": "#f2f2ed",
    "base_3": "#e8e8e3",
}

paper = {
    **white,
    "theme_name": "Logos Paper",
    "base_0": "#faf8f0",
    "base_1": "#f2ede6",
    "base_2": "#eae5de",
    "base_3": "#e6ded4",
    "base_4": "#201b12",
}

acme = {
    **white,
    "theme_name": "Logos Acme",
    "base_0": "#ffffea",
    "base_1": "#f8f8e3",
    "base_2": "#f2f2dd",
    "base_3": "#e8e8d3",
    "red_1": "#bb5d5d",
    "red_2": "#ee9999",
    "yellow_1": "#998866",
    "yellow_2": "#eeeeaa",
    "green_1": "#448844",
    "green_2": "#bbddbb",
    "blue_1": "#5577aa",
    "blue_2": "#ccddee",
    "magenta_1": "#aa77aa",
    "magenta_2": "#ddbbdd",
    "cyan_1": "#66aaaa",
    "cyan_2": "#addddd",
    "fg_accent": "#7777b0",
    "bg_accent": "#ccccee",
}

dark = {
    "theme_name": "Logos Dark",
    "theme_type": "dark",
    "base_0": "#2b2b2b",
    "base_1": "#333333",
    "base_2": "#3b3b3b",
    "base_3": "#484848",
    "base_4": "#dddddd",
    "base_5": "#ffffff",
    "red_1": "#f87870",
    "orange_1": "#ddaa77",
    "yellow_1": "#d0a868",
    "green_1": "#a9b665",
    "blue_1": "#80a8dd",
    "magenta_1": "#d3889b",
    "cyan_1": "#88b4a0",
    "fg_accent": "#88d4c0",
    "bg_accent": "#88d4c0",
    "invisible": "#00000000",
}

gruv = {
    **dark,
    "theme_name": "Logos Gruv",
    "base_0": "#32302f",
    "base_1": "#3a3837",
    "base_3": "#403d3c",
    "base_3": "#5c544b",
    "base_4": "#e0d0bb",
}

nord = {
    **dark,
    "theme_name": "Logos Nord",
    "base_0": "#2e3440",
    "base_1": "#363d4c",
    "base_2": "#3c4352",
    "base_3": "#434c5e",
    "base_4": "#d8dee9",
    "base_5": "#e8eef9",
    "red_1": "#bf616a",
    "orange_1": "#d08770",
    "green_1": "#a3be8c",
    "yellow_1": "#ebcb8b",
    "blue_1": "#81a1c1",
    "magenta_1": "#b48ead",
    "cyan_1": "#88c0d0",
    "fg_accent": "#88c0d0",
    "bg_accent": "#88c0d0",
}

red = {
    **dark,
    "theme_name": "Logos Red",
    "base_0": "#000000",
    "base_1": "#221111",
    "base_2": "#281818",
    "base_3": "#442222",
    "base_4": "#ee8888",
    "base_5": "#ff9999",
    "red_1": "#cc6666",
    "green_1": "#cc6666",
    "yellow_1": "#cc6666",
    "blue_1": "#cc6666",
    "magenta_1": "#cc6666",
    "cyan_1": "#cc6666",
    "orange_1": "#cc6666",
    "fg_accent": "#ff9999",
    "bg_accent": "#995555",
}

themes = {
    "light": {
        "white": white,
        "sun": sun,
        "paper": paper,
        "acme": acme,
    },
    "dark": {
        "dark": dark,
        "gruv": gruv,
        "nord": nord,
        "red": red,
    },
}

for category in themes.values():
    for theme_name, theme in category.items():
        theme["bg_main"] = theme["base_0"]
        theme["bg_subtle"] = theme["base_1"]
        theme["bg_fade"] = theme["base_2"]
        theme["bg_hl"] = theme["base_3"]
        theme["bg_drop"] = theme["bg_hl"] + "88"
        theme["fg_main"] = theme["base_4"]
        theme["fg_bold"] = theme["base_5"]
        theme["link"] = theme["fg_accent"]

        if theme in themes["light"].values():
            theme["fg_faint"] = theme["fg_main"] + "33"
            theme["fg_fade"] = theme["fg_main"] + "70"
            theme["fg_dim"] = theme["fg_main"] + "90"
            theme["fg_subtle"] = theme["fg_main"] + "aa"
            theme["bg_match_1"] = theme["bg_accent"] + "bb"
            theme["bg_match_2"] = theme["yellow_2"] + "bb"
            theme["black_1"] = theme["fg_main"]
            theme["white_2"] = theme["bg_main"]
            theme["border_1"] = theme["fg_fade"]
            theme["border_2"] = theme["fg_faint"]

        elif theme in themes["dark"].values():
            theme["fg_faint"] = theme["fg_main"] + "68"
            theme["fg_fade"] = theme["fg_main"] + "80"
            theme["fg_dim"] = theme["fg_main"] + "a0"
            theme["fg_subtle"] = theme["fg_main"] + "c0"
            theme["bg_match_1"] = theme["fg_accent"] + "77"
            theme["bg_match_2"] = theme["orange_1"] + "77"
            theme["black_1"] = theme["bg_main"]
            theme["white_2"] = theme["fg_main"]
            theme["border_1"] = theme["fg_main"] + "50"
            theme["border_2"] = theme["fg_main"] + "38"
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
