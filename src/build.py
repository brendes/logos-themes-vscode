#!/usr/bin/env python3

import json
import os
import re
from generate import generate_all_themes
from colors import colors


def theme_filename(name):
    filename = re.sub(r"[^\w\s-]", "", name.lower())
    filename = re.sub(r"[-\s]+", "-", filename)
    return filename.strip("-")


def generate_theme(theme_dict, template_file, output_file):
    """Generate a color-theme JSON file based on a theme dictionary."""
    try:
        with open(template_file, "r") as f:
            theme_template = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in template file: {e}")

    def recursive_format(value):
        if isinstance(value, str):
            return value.format(**theme_dict)
        elif isinstance(value, list):
            return [recursive_format(item) for item in value]
        elif isinstance(value, dict):
            return {key: recursive_format(val) for key, val in value.items()}
        else:
            return value

    try:
        theme_output = recursive_format(theme_template)
    except KeyError as e:
        raise ValueError(f"Missing color key in theme: {e}")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w") as f:
        json.dump(theme_output, f, indent=2)


def update_package_json():
    with open("package.json", "r") as f:
        package_data = json.load(f)

    themes_section = []

    for theme in colors:
        name = theme["name"]
        base_type = theme["type"]
        type = "vs-dark" if base_type == "dark" else "vs"
        filename = f"{theme_filename(name)}-color-theme.json"
        theme_entry = {
            "label": name,
            "uiTheme": type,
            "path": f"./themes/{filename}",
        }
        themes_section.append(theme_entry)

    if "contributes" not in package_data:
        package_data["contributes"] = {}

    package_data["contributes"]["themes"] = themes_section

    with open("package.json", "w") as f:
        json.dump(package_data, f, indent=2)

    return len(themes_section)


def main():
    themes = generate_all_themes()
    template_file = "src/template.json"
    output_dir = "themes"

    for theme_dict in themes:
        name = theme_dict.get("name")
        filename = f"{theme_filename(name)}-color-theme.json"
        output_path = os.path.join(output_dir, filename)
        try:
            generate_theme(theme_dict, template_file, output_path)
            print(f"Generated {filename}")
        except (FileNotFoundError, ValueError) as e:
            print(f"Error generating {filename}: {e}")

    try:
        update_package_json()
        print("Updated package.json")
    except Exception as e:
        print(f"Error updating package.json: {e}")


if __name__ == "__main__":
    main()
