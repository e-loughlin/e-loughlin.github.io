import argparse
import os
import re
import shutil


def extract_png_filenames(input_file):
    # Regex pattern to match file paths ending in .png
    pattern = re.compile(r"[^\/\\]+\.png")

    png_filenames = set()

    # Read the input file
    with open(input_file, "r") as file:
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                png_filenames.add(match)

    return png_filenames


def copy_files(filenames, source_dir, target_dir):
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Walk through the source directory recursively
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file in filenames:
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)
                shutil.copy2(source_path, target_path)
                print(f"Copied {source_path} to {target_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract .png filenames from a file and copy those files from source directory to target directory."
    )
    parser.add_argument(
        "input_file", type=str, help="Path to the input file containing file paths"
    )
    parser.add_argument("source_dir", type=str, help="Path to the source directory")
    parser.add_argument("target_dir", type=str, help="Path to the target directory")
    args = parser.parse_args()

    # Extract .png filenames
    png_filenames = extract_png_filenames(args.input_file)

    # Copy the extracted files
    copy_files(png_filenames, args.source_dir, args.target_dir)
