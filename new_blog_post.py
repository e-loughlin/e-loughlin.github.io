import argparse
import os
import shutil
from datetime import datetime

from slugify import slugify


def create_markdown_file(directory, title, date=None):
    # Handle date
    if date is None:
        date = datetime.today().strftime("%Y-%m-%d")
    else:
        # Validate date format
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return

    # Slugify the title
    slugified_title = slugify(title)

    # Create paths
    posts_dir = "./_posts/"
    assets_dir = f"./assets/images/{date}-{slugified_title}/"
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)

    # Create markdown file name
    md_file_name = f"{date}-{slugified_title}.md"
    md_file_path = os.path.join(posts_dir, md_file_name)

    # Start writing the markdown file
    with open(md_file_path, "w") as md_file:
        md_file.write(f"---\n")
        md_file.write(f'title: "{title}"\n')
        md_file.write(f"tags:\n")
        md_file.write(f"  - Test\n\n")
        md_file.write(f"header:\n")
        md_file.write(
            f"  teaser: https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/{date}-{slugified_title}/img1.png\n"
        )
        md_file.write(
            f"  og_image: https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/{date}-{slugified_title}/img1.png\n"
        )
        md_file.write(f"gallery:\n")

        # Move and rename images
        images = sorted(os.listdir(directory))
        for i, img_name in enumerate(images):
            if img_name.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                img_new_name = f"img{i+1}.png"
                src_img_path = os.path.join(directory, img_name)
                dest_img_path = os.path.join(assets_dir, img_new_name)
                shutil.move(src_img_path, dest_img_path)

                img_url = f"/assets/images/{date}-{slugified_title}/{img_new_name}"
                md_file.write(f"  - url: {img_url}\n")
                md_file.write(f"    image_path: {img_url}\n")
                md_file.write(f'    alt: "{title} Image {i+1}"\n')
                md_file.write(f'    title: "Image {i+1} title caption"\n')

        # Add the gallery inclusion
        md_file.write(f"---\n\n")
        md_file.write(f'{{% include gallery caption="{title}" layout="half" %}}\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a markdown file with a gallery format for images."
    )
    parser.add_argument("directory", help="Directory containing the images to process.")
    parser.add_argument("title", help="Title of the post.")
    parser.add_argument(
        "--date", help="Date in the format YYYY-MM-DD (optional).", default=None
    )

    args = parser.parse_args()

    create_markdown_file(args.directory, args.title, args.date)
