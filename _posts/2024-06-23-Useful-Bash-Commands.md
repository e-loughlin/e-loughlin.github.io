---
title: "Useful Command-Line Scripts"
tags:
  - Engineering
  - Programming
toc: true
toc_sticky: true
header:
  teaser: /assets/images/command-line.png
  og_image: /assets/images/command-line.png
---

![PIC](/assets/images/command-line.png)

# Useful Command Line Scripts

In the world of software engineering, efficiency is key. One way to enhance your productivity is by automating common tasks with command-line scripts. I've compiled a list of some of my favorite scripts that I frequently use in my `.zshrc` (on Mac) or `.bashrc` (on Ubuntu). These scripts help streamline my workflow and handle repetitive tasks effortlessly.

## Find And Replace Alias

**`far()`**: This script searches for files matching a specific pattern and replaces a given string within them. It’s perfect for making batch modifications across multiple files.

```bash
far() {
    pattern=$1
    find_str=$2
    replace_str=$3
    find . -type f -name "$pattern" -print0 | while IFS= read -r -d '' file; do
        if grep -q "$find_str" "$file"; then
            echo "Modifying file: $file"
            sed -i '' -e "s|$find_str|$replace_str|g" "$file"
        fi
    done
}
```

## Condense PDFs

**`condense_pdfs()`**: This script reduces the size of PDF files and appends `_REDUCED` to their filenames. Ideal for optimizing PDFs for easier sharing.

```bash
condense_pdfs() {
    find . -type f -name "*.pdf" ! -name "*REDUCED*" | while IFS= read -r file; do
        echo "Renaming and reducing file: $file"
        new_file="${file%.*}_REDUCED.pdf"
        
        cp "${file}" "${new_file}"
        ghostscript -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/ebook -dNOPAUSE -dQUIET -dBATCH -sOutputFile="${new_file}" "${file}"
    done
}
```

## Find and Rename Files

**`rename_files()`**: This script finds all files that match a search pattern and renames them by replacing a specified string. It includes a confirmation prompt before executing the rename.

```bash
rename_files() {
  if [ $# -ne 2 ]; then
    echo "Usage: rename_files <search_string> <replace_string>"
    return
  fi

  search_string="$1"
  replace_string="$2"

  files_to_rename=()

  # Collect the list of files matching the search string
  while IFS= read -r -d $'\0' file; do
    files_to_rename+=("$file")
  done < <(find . -type f -name "*${search_string}*" -print0)

  # Process the list of files in a for loop
  for file in "${files_to_rename[@]}"; do
    new_file="${file//$search_string/$replace_string}"

    if [ "$file" != "$new_file" ]; then
      target_dir=$(dirname "$new_file")

      # Create the target directory if it doesn't exist
      mkdir -p "$target_dir"

      echo "Renaming: $file -> $new_file"
      if confirm_action "Do you want to proceed?"; then
        mv -i "$file" "$new_file"
        echo "Renamed."
      else
        echo "Not renamed."
      fi
    fi
  done
}

confirm_action() {
    warning_message=$1
    echo -n "$warning_message (Y/n): "
    read choice
    case "$choice" in
        [yY]*) return 0 ;;
        [nN]*) return 1 ;;
        *) echo "Invalid choice. Please enter Y or n." ; confirm_action "$warning_message" ;;
    esac
}
```

## Grep Through Multiple Repositories

**`grep_all()`**: This script searches for a pattern across all Git repositories in a workspace directory, providing a convenient way to search through multiple projects.

```bash
grep_all() {
  if [ $# -ne 1 ]; then
    echo "Usage: grep_all <search_string>"
    return 1
  fi

  local search_string="$1"
  local ws_dir="$HOME/ws"
  local original_dir="$(pwd)"

  if [ ! -d "$ws_dir" ]; then
    echo "Error: Workspace directory '$ws_dir' not found."
    return 1
  fi

  cd "$ws_dir" || return 1

  # Loop through each folder in ~/ws
  for folder in */; do
    cd "$folder" || continue

    if git --no-pager grep "$search_string"; then
      echo "Found '$search_string' in $folder"
    else
      echo "'$search_string' not found in $folder"
    fi
    echo ""

    cd "$ws_dir" || return 1
  done

  cd "$original_dir" || return 1
  echo "Search completed. Returned to the original directory."
}
```

## Quick Git Commit and Push

**`gitq()`**: This script performs a `git pull`, stages changes, commits them with the current date and time, and pushes them to the repository.

```bash
gitq() {
	git pull
	git add .
	NOW=$( date '+%F_%H:%M:%S' );
	git commit -m "${NOW}"
	git push
}
```

## Get Git Repository URL

**`giturl()`**: This script fetches the HTTPS URL of the current Git repository branch.

```bash
function giturl() {
  local branch=$(git symbolic-ref --short HEAD)
  local upstream=$(git rev-parse --abbrev-ref --symbolic-full-name @{u})
  local remote=$(git config --get branch.$branch.remote)
  local url=$(git config --get remote.$remote.url | sed 's/git@github.com:/https:\/\/github.com\//' | sed 's/\.git//g')

  echo "$url/tree/$branch"
}
```

## Rewrite Git History

**`git_update_branch()`**: This advanced script is used for rewriting Git history, ideal for squashing commits. Use with caution!

```bash
git_update_branch() {
   # Determine the branch name to pull from (main or master)
    upstream_branch=""
    if git rev-parse --verify main &> /dev/null; then
      upstream_branch="main"
    elif git rev-parse --verify master &> /dev/null; then
      upstream_branch="master"
    fi

    echo "Upstream branch detected: ${upstream_branch}"

    my_branch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD) # Name of current branch you're on
    my_branch_old="${my_branch}_old" # Name of temporary branch
    git branch -m ${my_branch_old} # Re-name current branch to temp name
    git checkout ${upstream_branch}
    git pull
    git checkout -b ${my_branch} # Checkout new branch with existing name, up-to-date with master
    git merge --squash ${my_branch_old} # Merge changes from your temp branch into this updated branch
    git add .
    git commit # Fix up your commit message

    echo "Deleting branch ${my_branch_old}"
    git branch -D ${my_branch_old} # Delete the old temporary branch

    # If there are uncommitted changes, something went wrong. Do NOT push!
    echo "Check if everything is good. If so, run the following command:"
    echo "git push origin +${my_branch}" # Re-write history on your existing branch
}
```

## Line Difference Between Files

**`line_diff()`**: This script shows the lines present in one file but not in another.

```bash
line_diff() {
	comm -23 <(sort -u $1) <(sort -u $2)
}
```

