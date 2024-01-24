#!/usr/bin/env python3

# fmt: off

light = {
    'fg_bold'   : '#000000',
    'accent_1'  : '#6688bb',
    'accent_2'  : '#c0d0e0',
    'accent_3'  : '#eed2bb',
    'red_0'     : '#bb5058',
    'red_1'     : '#d88088',
    'yellow_0'  : '#a88870',
    'yellow_1'  : '#eed2aa',
    'green_0'   : '#889f78',
    'green_1'   : '#afbf88',
    'blue_0'    : '#7080a0',
    'blue_1'    : '#b8c8d7',
    'magenta_0' : '#a07488',
    'magenta_1' : '#d8b8c8',
    'cyan_0'    : '#6f9b98',
    'cyan_1'    : '#b0d8d4',
    'orange_0'  : '#e09988',
    'purple_0'  : '#9090cc',
    'purple_1'  : '#ccccee',
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
    'fg_main'   : '#000000',
}

paper = {
    **light,
    'theme_name': 'Logos Paper',
    'bg_main'   : '#faf7f1',
    'bg_subtle' : '#f0ebe4',
    'bg_hl'     : '#e6ded4',
    'fg_fade'   : '#b2a29c',
    'fg_dim'    : '#92827c',
    'fg_subtle' : '#605a52',
    'fg_main'   : '#201b12',
    'fg_bold'   : '#000000',
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
    'accent_1'    : light['purple_0'],
    'accent_2'    : light['purple_1'],
    'accent_3'    : '#eeeeaa',
}

dark = {
    'theme_name': 'Logos Dark',
    'bg_main'   : '#2b2b2b',
    'bg_subtle' : '#333333',
    'bg_hl'     : '#444444',
    'fg_fade'   : '#888888',
    'fg_dim'    : '#aaaaaa',
    'fg_subtle' : '#cccccc',
    'fg_main'   : '#dddddd',
    'fg_bold'   : '#ffffff',
    'accent_1'  : '#90c4b4',
    'accent_2'  : '#90c4b4',
    'accent_3'  : '#d3889b',
    'red_0'     : '#e86862',
    'green_0'   : '#a9b665',
    'yellow_0'  : '#d89858',
    'blue_0'    : '#7daea3',
    'magenta_0' : '#d3889b',
    'cyan_0'    : '#88b490',
    'orange_0'  : '#eeaa77',
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
    'theme_name': 'Logos Nord',
    'bg_main'   : '#2e3440',
    'bg_subtle' : '#363d4c',
    'bg_hl'     : '#434c5e',
    'fg_fade'   : '#707b90',
    'fg_dim'    : '#8895ae',
    'fg_subtle' : '#a8b0c8',
    'fg_main'   : '#d8dee9',
    'fg_bold'   : '#eceff4',
    'accent_1'  : '#88c0d0',
    'accent_2'  : '#88c0d0',
    'accent_3'  : '#b48ead',
    'red_0'     : '#bf616a',
    'green_0'   : '#a3be8c',
    'yellow_0'  : '#ebcb8b',
    'blue_0'    : '#81a1c1',
    'magenta_0' : '#b48ead',
    'cyan_0'    : '#88c0d0',
    'orange_0'  : '#d08770',
}

red = {
    **dark,
    'theme_name': 'Logos Red',
    'bg_main'   : '#110000',
    'bg_subtle' : '#221111',
    'bg_hl'     : '#442222',
    'fg_fade'   : '#aa6666',
    'fg_dim'    : '#bb6666',
    'fg_subtle' : '#dd7777',
    'fg_main'   : '#ee8888',
    'fg_bold'   : '#ff9999',
    'accent_1'  : '#ee8888',
    'accent_2'  : '#ee8888',
    'accent_3'  : '#ee8888',
    'red_0'     : '#ee8888',
    'green_0'   : '#ee8888',
    'yellow_0'  : '#ee8888',
    'blue_0'    : '#ee8888',
    'magenta_0' : '#ee8888',
    'cyan_0'    : '#ee8888',
    'orange_0'  : '#ee8888',
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
    theme['theme_type'] = 'light'
    theme['black_0'] = theme['fg_main']
    theme['white_1'] = theme['bg_subtle']
    theme['border'] = theme['fg_main'] + '20'
    theme['match_alpha'] = 'd0'

for theme_name, theme in themes['dark'].items():
    theme['theme_type'] = 'dark'
    theme['black_0'] = theme['bg_main']
    theme['white_1'] = theme['fg_main']
    theme['border'] = theme['fg_main'] + '28'
    theme['match_alpha'] = '78'
    for color in ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan']:
        theme[f'{color}_1'] = theme[f'{color}_0']
