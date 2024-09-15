---
title: "Automated Scroll and Screenshot Tool"
tags:
  - Engineering
  - Automation
  - Python
header:
  teaser: /assets/images/2023-07-12-automated-scroll-and-screenshot-tool/img02.png
  og_image: /assets/images/2023-07-12-automated-scroll-and-screenshot-tool/img02.png
toc: true
toc_sticky: true
---


![Automated Scroll and Screenshot Tool](/assets/images/2023-07-12-automated-scroll-and-screenshot-tool/img02.png)


<center>
<iframe width="560" height="315" src="https://www.youtube.com/embed/WOgt3EsVAUU" title="YouTube: Screenshot Tool" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</center>

# Scroll and Screenshot Tool

Source code can be found on [GitHub](https://github.com/e-loughlin/scroll-screenshotter)

## Overview

This blog post details a Python tool that automates scrolling and capturing screenshots in a loop. It's ideal for capturing information hidden beyond a single screen in applications without built-in export functionalities.

**Originally designed for capturing Microsoft Teams chats**, this tool can be adapted for any application where scrolling is required to view all the content.

For detailed information and additional options, run the following command in your terminal:

```bash
python scroll-screenshotter.py -h
```

## Requirements

* **Python 3:** Ensure you have Python 3 installed on your system.
* **Required Libraries:** Install the necessary libraries using pip:

```bash
pip install -r requirements.txt
```

This command installs the Python libraries listed in the `requirements.txt` file, which are essential for the tool's functionality.


## Using the Tool

Here's an example of how to use the tool:

```bash
python scroll-screenshotter.py -s 20 -o /Users/eloughlin/Desktop -t <my_run_name>
```

This command will:

* Scroll down 20 times (`-s 20`) after each screenshot.
* Save the screenshots to the specified directory (`-o /Users/eloughlin/Desktop`).
* Name each screenshot with a prefix based on the provided title (`-t <my_run_name>`) followed by a sequence number (e.g., "chat_with_evan_01.jpg", "chat_with_evan_02.jpg", etc.).

## Additional Options

The tool offers various options to customize its behavior:

* **Scrolls per Screenshot (`-s`):** (Required) This option specifies the number of scroll downs (or ups) to perform before capturing a screenshot.

* **Output Directory (`-o`):** (Required) This option defines the directory where the captured screenshots will be saved. 

* **Title (`-t`):** (Required) This option allows you to set a prefix for the screenshot filenames. 

* **Image Quality Percent (`-q`):** (Optional, Default: 60) This option controls the image quality of the saved screenshots. A lower percentage creates smaller file sizes but with a corresponding reduction in image quality.

* **Image Size Percent (`-r`):** (Optional, Default: 60) This option allows you to reduce the size of the saved screenshots by a specified percentage. 

* **Scroll Key (`-k`):** (Optional, Default: "down") This option defines the keyboard key used for scrolling. By default, it's set to "down", but you can change it to "up" if your application requires scrolling up (e.g., chat windows). Refer to PyAutoGUI's documentation ([link to PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/keyboard.html)) for a list of supported keyboard keys and more advanced key settings. **Note that for Microsoft Teams, you may need to scroll "up", instead of the default of "down". MAKE SURE YOU SET THE RIGHT KEY**

