#!/usr/bin/env python3

import json
import os
from themes import themes


def generate_theme(theme_dict, template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    with open(template_file, "r") as f:
        theme_template = json.load(f)

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

    with open(output_file, "w") as f:
        json.dump(theme_output, f, indent=2)


def main():
    for theme_name, theme_dict in themes.items():
        output_file_name = f"logos-{theme_name.replace('_', '-')}-color-theme.json"
        output_file_path = os.path.join("themes", output_file_name)
        generate_theme(theme_dict, "src/template.json", output_file_path)


if __name__ == "__main__":
    main()
