import argparse
import os

import nbformat
import yaml
from nbconvert import HTMLExporter
from slugify import slugify


def convert_notebook_to_html(notebook_path):
    # Load the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Convert the notebook to HTML
    html_exporter = HTMLExporter()
    html_exporter.template_name = "basic"
    body, resources = html_exporter.from_notebook_node(notebook_content)

    # Extract the notebook name and create the output file path
    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    slugified_name = slugify(notebook_name)
    output_path = f"../_pages/nb/{notebook_name}.html"

    # Prepare the content to be saved
    html_content = f"""---
permalink: /nb/{slugified_name}
layout: nb
author_profile: false
toc: true
toc_label: Contents
toc_sticky: true
---


{{% raw %}}

<br>
<strong>Interactive version with <a href="https://e-loughlin.github.io/notebooks/lab/">Jupyterlite</a>.</strong>

The <a href="https://github.com/e-loughlin/notebooks/tree/main/content">GitHub repository</a> contains the .ipynb files.

{body}

{{% endraw %}}
"""

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the HTML content to the output file
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Notebook converted and saved to {output_path}")


def update_navigation_yml(notebook_path):
    # Load the notebook
    notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
    slugified_name = slugify(notebook_name)
    notebook_title = notebook_name.replace(
        "-", " "
    ).title()  # Adjust the title format if needed

    # Path to the navigation YAML file
    nav_yml_path = "../_data/navigation.yml"

    # Load the existing navigation YAML
    with open(nav_yml_path, "r", encoding="utf-8") as f:
        nav_data = yaml.safe_load(f)

    # Check if 'sidebar-nb' is in nav_data and is a dictionary
    if "sidebar-nb" in nav_data and isinstance(nav_data["sidebar-nb"][0], dict):
        if "children" not in nav_data["sidebar-nb"][0]:
            nav_data["sidebar-nb"]["children"] = []

        # Add new entry to sidebar-nb
        new_entry = {"title": notebook_title, "url": f"/nb/{slugified_name}/"}
        nav_data["sidebar-nb"][0]["children"].append(new_entry)
    else:
        print(
            f"Error: 'sidebar-nb' is missing or not in the expected format in {nav_yml_path}"
        )
        return

    # Save the updated navigation YAML
    with open(nav_yml_path, "w", encoding="utf-8") as f:
        yaml.dump(nav_data, f, default_flow_style=False)

    print(f"Navigation file updated with {notebook_title}")


def main():
    parser = argparse.ArgumentParser(
        description="Convert Jupyter notebook to HTML with Jekyll front matter and update navigation.yml."
    )
    parser.add_argument("notebook", help="Path to the Jupyter notebook file")
    args = parser.parse_args()

    convert_notebook_to_html(args.notebook)
    update_navigation_yml(args.notebook)


if __name__ == "__main__":
    main()
