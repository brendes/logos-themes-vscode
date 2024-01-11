#!/usr/bin/env python3

# fmt: off

light = {
    'theme_type'     : 'light',
    'fg_bold'        : '#000000',
    'color_red_0'    : '#bb5058',
    'color_red_1'    : '#d88088',
    'color_yellow_0' : '#a88870',
    'color_yellow_1' : '#eed2aa',
    'color_green_0'  : '#889f78',
    'color_green_1'  : '#afbf88',
    'color_blue_0'   : '#7080a0',
    'color_blue_1'   : '#b8c8d7',
    'color_magenta_0': '#a07488',
    'color_magenta_1': '#d8b8c8',
    'color_cyan_0'   : '#6f9b98',
    'color_cyan_1'   : '#b0d8d4',
    'color_orange_0' : '#e09988',
    'color_purple_0' : '#9090cc',
    'color_purple_1' : '#ccccee',
    'accent_1'       : '#609894',
    'accent_2'       : '#bbdddb',
    'accent_alt_2'   : '#ddbbdb',
}

white = {
    **light,
    'theme_name'     : 'Logos White',
    'bg_main'        : '#ffffff',
    'bg_subtle'      : '#f8f8f8',
    'bg_hl'          : '#ececec',
    'fg_fade'        : '#aaaaaa',
    'fg_dim'         : '#888888',
    'fg_subtle'      : '#666666',
    'fg_main'        : '#111111',
}

tree = {
    **white,
    'theme_name': 'Logos Tree',
    'bg_main'   : '#fffffa',
    'bg_subtle' : '#f6f6f1',
    'bg_hl'     : '#ebebe6',
}

paper = {
    **light,
    'theme_name'  : 'Logos Paper',
    'bg_main'     : '#faf7f1',
    'bg_subtle'   : '#f0ebe4',
    'bg_hl'       : '#e6ded4',
    'fg_fade'     : '#b2a29c',
    'fg_dim'      : '#92827c',
    'fg_subtle'   : '#605a52',
    'fg_main'     : '#201b12',
    'fg_bold'     : '#000000',
    'accent_1'    : '#70a490',
    'accent_2'    : '#bbddd4',
    'accent_alt_2': '#ddbbd4',
}

acme = {
    **light,
    'theme_name'  : 'Logos Acme',
    'bg_main'     : '#ffffeb',
    'bg_subtle'   : '#f8f8e5',
    'bg_hl'       : '#eeeeda',
    'fg_fade'     : '#aaaaa0',
    'fg_dim'      : '#888880',
    'fg_subtle'   : '#666660',
    'fg_main'     : '#000000',
    'fg_bold'     : '#000000',
    'accent_1'    : light['color_purple_0'],
    'accent_2'    : light['color_purple_1'],
    'accent_alt_2': '#eeeeaa',
}

dark = {
    'theme_name'     : 'Logos Dark',
    'theme_type'     : 'dark',
    'bg_main'        : '#303030',
    'bg_subtle'      : '#3b3b3b',
    'bg_hl'          : '#505050',
    'fg_fade'        : '#808080',
    'fg_dim'         : '#a0a0a0',
    'fg_subtle'      : '#c0c0c0',
    'fg_main'        : '#dddddd',
    'fg_bold'        : '#ffffff',
    'accent_1'       : '#90c4b4',
    'accent_2'       : '#90c4b4',
    'accent_alt_2'   : '#e8b878',
    'color_red_0'    : '#e86862',
    'color_green_0'  : '#a9b665',
    'color_yellow_0' : '#d89858',
    'color_blue_0'   : '#7daea3',
    'color_magenta_0': '#d3889b',
    'color_cyan_0'   : '#88b490',
    'color_orange_0' : '#eeaa77',
}

dark_warm = {
    **dark,
    'theme_name': 'Logos Dark Warm',
    'bg_main'   : '#32302f',
    'bg_subtle' : '#3a3837',
    'bg_hl'     : '#504e4c',
    'fg_fade'   : '#8c7f74',
    'fg_dim'    : '#a89984',
    'fg_subtle' : '#c8b8a4',
    'fg_main'   : '#ddc8a8',
    'fg_bold'   : '#ffeaca',
}

nord = {
    **dark,
    'theme_name'     : 'Logos Nord',
    'bg_main'        : '#2e3440',
    'bg_subtle'      : '#363d4c',
    'bg_hl'          : '#434c5e',
    'fg_fade'        : '#707b90',
    'fg_dim'         : '#8895ae',
    'fg_subtle'      : '#a8b0c8',
    'fg_main'        : '#d8dee9',
    'fg_bold'        : '#eceff4',
    'accent_1'       : '#88c0d0',
    'accent_2'       : '#88c0d0',
    'accent_alt_2'   : '#b48ead',
    'color_red_0'    : '#bf616a',
    'color_green_0'  : '#a3be8c',
    'color_yellow_0' : '#ebcb8b',
    'color_blue_0'   : '#81a1c1',
    'color_magenta_0': '#b48ead',
    'color_cyan_0'   : '#88c0d0',
    'color_orange_0' : '#d08770',
}

red = {
    **dark,
    'theme_name'     : 'Logos Red',
    'bg_main'        : '#110000',
    'bg_subtle'      : '#221111',
    'bg_hl'          : '#442222',
    'fg_fade'        : '#995555',
    'fg_dim'         : '#bb6666',
    'fg_subtle'      : '#dd7777',
    'fg_main'        : '#ee8888',
    'fg_bold'        : '#ff9999',
    'accent_1'       : '#ee7777',
    'accent_2'       : '#ee7777',
    'accent_alt_2'   : '#ee7777',
    'color_red_0'    : '#ee7777',
    'color_green_0'  : '#ee7777',
    'color_yellow_0' : '#ee7777',
    'color_blue_0'   : '#ee7777',
    'color_magenta_0': '#ee7777',
    'color_cyan_0'   : '#ee7777',
    'color_orange_0' : '#ee7777',
}

themes = {
    'light': {
        'white': white,
        'tree' : tree,
        'paper': paper,
        'acme' : acme,
    },
    'dark': {
        'dark'     : dark,
        'dark_warm': dark_warm,
        'nord'     : nord,
        'red'      : red,
    },
}

for theme_name, theme in themes['light'].items():
    theme['color_black_0'] = theme['fg_main']
    theme['color_white_1'] = theme['bg_subtle']
    theme['border'] = theme['fg_main'] + '20'
    theme['match_alpha'] = 'd0'

for theme_name, theme in themes['dark'].items():
    theme['color_black_0'] = theme['bg_main']
    theme['color_white_1'] = theme['fg_main']
    theme['border'] = theme['fg_main'] + '30'
    theme['match_alpha'] = '78'
    for color in ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']:
        theme[f'color_{color}_1'] = theme[f'color_{color}_0']
