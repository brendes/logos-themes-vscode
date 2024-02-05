#!/usr/bin/env python3

# fmt: off

light = {
    'theme_type'    :  'light',
    'bg_accent'     : '#e8d0b8',
    'fg_bold'       : '#000000',
    'fg_accent'     : '#6677aa',
    'red_1'         : '#bb5058',
    'red_2'         : '#d88088',
    'orange_1'      : '#d08968',
    'orange_2'      : '#f0ccb0',
    'yellow_1'      : '#a88870',
    'yellow_2'      : '#eed2aa',
    'green_1'       : '#889f78',
    'green_2'       : '#afbf88',
    'blue_1'        : '#7080a0',
    'blue_2'        : '#b8c8d7',
    'magenta_1'     : '#a07488',
    'magenta_2'     : '#d8b8c8',
    'cyan_1'        : '#6f9b98',
    'cyan_2'        : '#b0d8d4',
    'invisible'     : '#00000000',
    'match_alpha'   : 'd0',
}

white = {
    **light,
    'theme_name'     : 'Logos White',
    'bg_main'        : '#ffffff',
    'bg_subtle'      : '#f8f8f8',
    'bg_fade'        : '#f2f2f2',
    'bg_hl'          : '#ebebeb',
    'bg_strong'      : '#cccccc',
    'fg_fade'        : '#aaaaaa',
    'fg_dim'         : '#888888',
    'fg_subtle'      : '#666666',
    'fg_main'        : '#111111',
}

tree = {
    **white,
    'theme_name': 'Logos Tree',
    'bg_main'   : '#fffffa',
    'bg_subtle' : '#f8f8f3',
    'bg_fade'   : '#f2f2ed',
    'bg_hl'     : '#ebebe6',
    'fg_main'   : '#000000',
}

paper = {
    **light,
    'theme_name': 'Logos Paper',
    'bg_main'   : '#faf7f1',
    'bg_subtle' : '#f0ebe4',
    'bg_fade'   : '#eae5de',
    'bg_hl'     : '#e6ded4',
    'bg_strong' : '#c2b2ac',
    'fg_fade'   : '#b2a29c',
    'fg_dim'    : '#92827c',
    'fg_subtle' : '#605a52',
    'fg_main'   : '#201b12',
    'fg_bold'   : '#000000',
}

acme = {
    **light,
    'theme_name'   : 'Logos Acme',
    'bg_main'      : '#ffffee',
    'bg_subtle'    : '#f8f8e8',
    'bg_fade'      : '#f2f2e2',
    'bg_hl'        : '#ebebdb',
    'bg_strong'    : '#ccccbc',
    'bg_accent'    : '#eeeeaa',
    'fg_fade'      : '#aaaaa0',
    'fg_dim'       : '#888880',
    'fg_subtle'    : '#666660',
    'fg_main'      : '#000000',
    'fg_bold'      : '#000000',
    'fg_accent'    : '#7777bb',
}

dark = {
    'theme_type'    : 'dark',
    'theme_name'    : 'Logos Dark',
    'bg_main'       : '#303030',
    'bg_subtle'     : '#383838',
    'bg_fade'       : '#404040',
    'bg_hl'         : '#484848',
    'bg_strong'     : '#686868',
    'bg_accent'     : '#eeaa77',
    'fg_fade'       : '#888888',
    'fg_dim'        : '#a2a2a2',
    'fg_subtle'     : '#bbbbbb',
    'fg_main'       : '#dddddd',
    'fg_bold'       : '#ffffff',
    'fg_accent'     : '#88bb99',
    'red_1'         : '#f87870',
    'orange_1'      : '#ddaa77',
    'yellow_1'      : '#d0a868',
    'green_1'       : '#a9b665',
    'blue_1'        : '#7daea3',
    'magenta_1'     : '#d3889b',
    'cyan_1'        : '#88b490',
    'invisible'     : '#00000000',
    'match_alpha'   : '88',
}

dark_warm = {
    **dark,
    'theme_name': 'Logos Dark Warm',
    'bg_main'   : '#32302f',
    'bg_subtle' : '#3a3837',
    'bg_fade'   : '#403d3c',
    'bg_hl'     : '#504e4c',
    'bg_strong' : '#706e6c',
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
    'bg_fade'   : '#3c4352',
    'bg_hl'     : '#434c5e',
    'bg_strong' : '#5c6372',
    'bg_accent' : '#88c0d0',
    'fg_fade'   : '#707b90',
    'fg_dim'    : '#8895ae',
    'fg_subtle' : '#a8b0c8',
    'fg_main'   : '#d8dee9',
    'fg_bold'   : '#eceff4',
    'fg_accent' : '#88c0d0',
    'red_1'     : '#bf616a',
    'orange_1'  : '#d08770',
    'green_1'   : '#a3be8c',
    'yellow_1'  : '#ebcb8b',
    'blue_1'    : '#81a1c1',
    'magenta_1' : '#b48ead',
    'cyan_1'    : '#88c0d0',
}

red = {
    **dark,
    'theme_name'    : 'Logos Red',
    'bg_main'       : '#110000',
    'bg_subtle'     : '#221111',
    'bg_fade'       : '#281818',
    'bg_hl'         : '#442222',
    'bg_strong'     : '#663333',
    'bg_accent'     : '#dd7777',
    'bg_match'      : '#bb6666',
    'fg_fade'       : '#aa6666',
    'fg_dim'        : '#bb6666',
    'fg_subtle'     : '#dd7777',
    'fg_main'       : '#ee8888',
    'fg_bold'       : '#ff9999',
    'fg_accent'     : '#ff9999',
    'red_1'         : '#ee8888',
    'green_1'       : '#ee8888',
    'yellow_1'      : '#ee8888',
    'blue_1'        : '#ee8888',
    'magenta_1'     : '#ee8888',
    'cyan_1'        : '#ee8888',
    'orange_1'      : '#ee8888',
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
    theme['border_light']  = theme['fg_main'] + '28'
    theme['border_strong'] = theme['fg_main'] + '40'
    theme['black_1']       = theme['fg_main']
    theme['white_2']       = theme['bg_subtle']

for theme_name, theme in themes['dark'].items():
    theme['border_light']  = theme['fg_main'] + '20'
    theme['border_strong'] = theme['fg_main'] + '30'
    theme['black_1']       = theme['bg_main']
    theme['white_2']       = theme['fg_main']
    for color in ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'orange']:
        theme[f'{color}_2'] = theme[f'{color}_1']
