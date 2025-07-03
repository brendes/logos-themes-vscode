base_colors = {
    "light": {
        "theme_type": "light",
        "red_1": "#bb5555",
        "red_2": "#e89090",
        "orange_1": "#d08868",
        "orange_2": "#f0bca0",
        "yellow_1": "#aa8866",
        "yellow_2": "#f0d0aa",
        "green_1": "#889944",
        "green_2": "#b0c088",
        "blue_1": "#667799",
        "blue_2": "#bbc8dd",
        "blue_bold": "#6680b8",
        "purple_1": "#8c6d9c",
        "purple_2": "#bbaadd",
        "magenta_1": "#bb6677",
        "magenta_2": "#d8b8c8",
        "cyan_1": "#669988",
        "cyan_2": "#b8dbd4",
        "invisible": "#00000000",
        "match_1": "#f8e0bb",
        "match_2": "#d0e0f8",
    },
    "dark": {
        "theme_type": "dark",
        "red_1": "#f87870",
        "orange_1": "#dd9966",
        "yellow_1": "#eebb88",
        "green_1": "#aab866",
        "blue_1": "#80a8b0",
        "purple_1": "#8c6d9c",
        "magenta_1": "#d3889b",
        "cyan_1": "#88b4a0",
        "invisible": "#00000000",
    },
}

themes = {
    "white": {
        **base_colors["light"],
        "theme_name": "Logos",
        "base_0": "#ffffff",
        "base_1": "#f8f8f8",
        "base_2": "#f2f2f2",
        "base_3": "#e8e8e8",
        "base_4": "#dddddd",
        "base_5": "#707070",
        "base_6": "#000000",
        "base_7": "#000000",
    },
    "sun": {
        **base_colors["light"],
        "theme_name": "Logos Sun",
        "base_0": "#fffffa",
        "base_1": "#f8f8f3",
        "base_2": "#f2f2ed",
        "base_3": "#e8e8e3",
        "base_4": "#ddddd8",
        "base_5": "#70706b",
        "base_6": "#000000",
        "base_7": "#000000",
        "match_1": "#f8e8bb",
        "match_2": "#d0d8f0",
    },
    "paper": {
        **base_colors["light"],
        "theme_name": "Logos Paper",
        "base_0": "#faf7f2",
        "base_1": "#f1ece4",
        "base_2": "#ece7e2",
        "base_3": "#e0d8d0",
        "base_4": "#d0c8bd",
        "base_5": "#887872",
        "base_6": "#403a32",
        "base_7": "#000000",
        "match_1": "#f8d8b8",
        "match_2": "#d0d8f8",
    },
    "acme": {
        **base_colors["light"],
        "theme_name": "Logos Acme",
        "base_0": "#ffffee",
        "base_1": "#f9f9e9",
        "base_2": "#f2f2e2",
        "base_3": "#e8e8d8",
        "base_4": "#ddddcc",
        "base_5": "#707068",
        "base_6": "#000000",
        "base_7": "#000000",
        "red_1": "#bb5d5d",
        "red_2": "#ee9999",
        "yellow_1": "#998866",
        "yellow_2": "#eeeeaa",
        "green_1": "#448844",
        "green_2": "#bbddbb",
        "blue_1": "#6677bb",
        "blue_2": "#ccccff",
        "magenta_1": "#aa77aa",
        "magenta_2": "#ddbbdd",
        "cyan_1": "#66aaaa",
        "cyan_2": "#addddd",
        "match_1": "#eeeea8",
        "match_2": "#ccccee",
    },
    "dark": {
        **base_colors["dark"],
        "theme_name": "Logos Dark",
        "base_0": "#282828",
        "base_1": "#333333",
        "base_2": "#383838",
        "base_3": "#484848",
        "base_4": "#585858",
        "base_5": "#a8a8a8",
        "base_6": "#d8d8d8",
        "base_7": "#ffffff",
    },
    "gruv": {
        **base_colors["dark"],
        "theme_name": "Logos Gruv",
        "base_0": "#302d2c",
        "base_1": "#3c3836",
        "base_2": "#403d3c",
        "base_3": "#504945",
        "base_4": "#665c54",
        "base_5": "#ceb8a2",
        "base_6": "#eed8c2",
        "base_7": "#ffefcc",
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
    theme["black_2"] = theme["bg_bold"]

    if theme.get("theme_type") == "light":
        theme["fg_ghost"] = theme["fg_main"] + "18"
        theme["fg_faint"] = theme["fg_main"] + "33"
        theme["fg_dim"] = theme["fg_main"] + "78"
        theme["fg_subtle"] = theme["fg_main"] + "98"
        theme["fg_ui"] = theme["fg_subtle"]
        theme["bg_hover"] = theme["bg_fade"]
        theme["bg_widget"] = theme["bg_main"]
        theme["bg_match_1"] = theme["match_1"] + "ee"
        theme["bg_match_2"] = theme["match_2"] + "ee"
        theme["border_hard"] = theme["fg_main"] + "88"
        theme["border_focus"] = theme["fg_main"] + "40"
        theme["border_soft"] = theme["fg_main"] + "28"
        theme["border_popup"] = theme["border_hard"]
        theme["black_1"] = theme["fg_main"]
        theme["white_2"] = theme["bg_main"]
        theme["link"] = theme["blue_bold"]
        theme["code"] = theme["magenta_1"]

    elif theme.get("theme_type") == "dark":
        theme["fg_ghost"] = theme["fg_main"] + "28"
        theme["fg_faint"] = theme["fg_main"] + "48"
        theme["fg_dim"] = theme["fg_main"] + "88"
        theme["fg_subtle"] = theme["fg_main"] + "b8"
        theme["fg_ui"] = theme["fg_subtle"]
        theme["bg_hover"] = theme["bg_hl"]
        theme["bg_widget"] = theme["bg_fade"]
        theme["bg_match_1"] = theme["magenta_1"] + "bb"
        theme["bg_match_2"] = theme["cyan_1"] + "bb"
        theme["border_hard"] = theme["fg_main"] + "68"
        theme["border_focus"] = theme["fg_main"] + "48"
        theme["border_soft"] = theme["bg_subtle"]
        theme["border_popup"] = theme["bg_fade"]
        theme["black_1"] = theme["bg_main"]
        theme["white_2"] = theme["fg_main"]
        theme["link"] = theme["cyan_1"]
        theme["code"] = theme["magenta_1"]
        for color in [
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "orange",
            "purple"
        ]:
            theme[f"{color}_2"] = theme[f"{color}_1"]
