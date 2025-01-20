# PNG to ICO Converter

This script converts all `.png` images in the `Input` folder to `.ico` format and saves them in the `Output` folder. If a file with the same name already exists in the `Output` folder, it will not be converted again.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Install Python from [python.org](https://www.python.org/).
2. Install the Pillow library using pip:

    ```sh
    pip install pillow
    ```

## Usage

1. Place your `.png` images in the [Input](http://_vscodecontentref_/0) folder.
2. Run the script:

    ```sh
    python png_to_ico.py
    ```

3. The converted `.ico` files will be saved in the [Output](http://_vscodecontentref_/1) folder.

## Notes

- The script will create the [Output](http://_vscodecontentref_/2) folder if it does not exist.
- Only `.png` files in the [Input](http://_vscodecontentref_/3) folder will be processed.
- Existing `.ico` files in the [Output](http://_vscodecontentref_/4) folder will not be overwritten.

## Example

```sh
Input/
    image1.png
    image2.png
Output/
    image1.ico
    image2.ico
```