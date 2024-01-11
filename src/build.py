#!/usr/bin/env python3

import json
import importlib
import os
import yaml
from themes import themes


def generate_theme(theme_dict, template_file, output_file):
    '''Generate a color-theme JSON file based on a theme dictionary.'''
    with open(template_file, 'r') as f:
        theme_template = yaml.safe_load(f)

    # Format the strings in the YAML dictionary
    def recursive_format(value):
        if isinstance(value, str):
            return value.format(**theme_dict)
        elif isinstance(value, list):
            return [recursive_format(item) for item in value]
        elif isinstance(value, dict):
            return {key: recursive_format(val) for key, val in value.items()}
        else:
            return value

    theme_output = recursive_format(theme_template)

    with open(output_file, 'w') as f:
        json.dump(theme_output, f, indent=2)


def main():
    for category, theme_group in themes.items():
        for theme_name, theme_dict in theme_group.items():
            output_file_name = f"logos-{theme_name.replace('_', '-')}-color-theme.json"
            output_file_path = os.path.join('themes', output_file_name)
            generate_theme(theme_dict, 'src/template.yml', output_file_path)


if __name__ == '__main__':
    main()
