import argparse
import os
import re
import shutil
from datetime import datetime


def slugify(title):
    return re.sub(r"\W+", "_", title.lower()).strip("_")


def create_markdown_file(title, date, directory):
    slugified_title = slugify(title)
    post_dir = "./_posts"
    images_dir = f"./assets/images/{date}-{slugified_title}"

    if not os.path.exists(post_dir):
        os.makedirs(post_dir)
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    # Creating the .md file
    filename = f"{date}-{slugified_title}.md"
    filepath = os.path.join(post_dir, filename)

    with open(filepath, "w") as md_file:
        md_file.write(f"---\n")
        md_file.write(f'title: "{title}"\n')
        md_file.write(f"tags:\n")
        md_file.write(f"    - Test\n\n")
        md_file.write(f"header:\n")
        md_file.write(
            f"  teaser: https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/{date}-{slugified_title}/img1.png\n"
        )
        md_file.write(
            f"  og_image: https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/{date}-{slugified_title}/img1.png\n"
        )
        md_file.write(f"---\n\n")

        # Move and rename images, add markdown image links
        images = sorted(
            [
                img
                for img in os.listdir(directory)
                if img.lower().endswith((".png", ".jpg", ".jpeg"))
            ]
        )

        for i, image in enumerate(images, start=1):
            new_image_name = f"img{i}.png"
            src_path = os.path.join(directory, image)
            dest_path = os.path.join(images_dir, new_image_name)
            shutil.move(src_path, dest_path)

            md_file.write(
                f"![{title} Image {i}](https://raw.githubusercontent.com/e-loughlin/e-loughlin.github.io/main/assets/images/{date}-{slugified_title}/{new_image_name})\n"
            )
            md_file.write(f"*Description for image {i}*\n\n")


def main():
    parser = argparse.ArgumentParser(
        description="Create a markdown post and process images."
    )
    parser.add_argument("directory", help="Directory containing images to process.")
    parser.add_argument("title", help="Title of the post.")
    parser.add_argument(
        "--date",
        help="Date in YYYY-MM-DD format. Defaults to today.",
        default=datetime.today().strftime("%Y-%m-%d"),
    )

    args = parser.parse_args()
    create_markdown_file(args.title, args.date, args.directory)


if __name__ == "__main__":
    main()
