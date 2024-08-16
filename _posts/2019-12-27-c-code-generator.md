---
title: "C++ Code Generator"
tags:
  - Engineering
  - Golang
  - C++
  - Programming
header:
  teaser: /assets/images/2019-12-27-c-code-generator/img02.png
  og_image: /assets/images/2019-12-27-c-code-generator/img02.png
toc: true
toc_sticky: true
---

<p align="center">
  <img src="/assets/images/2019-12-27-c-code-generator/img02.png" alt="Sudoku Solved with Brute Force">
</p>

# CppCodeGenerator: Streamline Your C++ Development

Are you tired of manually writing boilerplate C++ code for interfaces, classes, mocks, and tests? Look no further than CppCodeGenerator, a powerful tool designed to automate and streamline your C++ code generation tasks. 

## What is CppCodeGenerator?

CppCodeGenerator is a tool for generating boilerplate C++ code from user-provided template files and configurations. Whether you need to create interfaces, class headers and implementations, mock classes, or test classes, this tool can handle it all with ease.

### Key Features:
- **Generate Interfaces**: Create new interfaces quickly.
- **Class Headers and Implementations**: Generate class headers and implementations with minimal effort.
- **Mock Classes**: Easily generate mock classes for GoogleMock.
- **Test Classes**: Create test classes for GoogleTest.

![Generating a new interface](https://raw.githubusercontent.com/e-loughlin/CppCodeGenerator/master/documentation/readme_resources/01_new_interface.gif)

## How It Works

1. **Installation**:
   Clone the repository and build the project with Go. Here’s how:
   ```bash
   git clone https://github.com/e-loughlin/CppCodeGenerator.git
   cd CppCodeGenerator
   mkdir build && cd build
   go build ..
   ```

2. **Usage**:
   Use command-line arguments to specify the type of code to generate:
   - `--type` for class type (interface, class, mock, or test)
   - `--interface` for specifying an existing C++ interface
   - `--name` for naming the class

   Example to generate a new interface:
   ```bash
   CppCodeGenerator --type interface --name MyFirstClass
   ```

   ![Generating a new class from an existing interface](https://raw.githubusercontent.com/e-loughlin/CppCodeGenerator/master/documentation/readme_resources/04_new_class.gif)

3. **Configuration**:
   Modify `config.json` to customize prefixes, suffixes, and formatting. You can also adjust policies and template file names to fit your needs.

   ![Configuring prefixes, suffixes, syntax, and file extensions](https://raw.githubusercontent.com/e-loughlin/CppCodeGenerator/master/documentation/readme_resources/11_configurations_1.gif)

4. **Templates**:
   Use user-defined template `.txt` files to control the format of the generated code. Customize these templates as needed to match your project requirements.

   ![Template filenames](https://raw.githubusercontent.com/e-loughlin/CppCodeGenerator/master/documentation/readme_resources/12_template_filenames.GIF)

## Additional Resources

For more details and to get started with CppCodeGenerator, visit the [GitHub repository](https://github.com/e-loughlin/CppCodeGenerator).

