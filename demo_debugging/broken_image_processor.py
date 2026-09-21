#!/usr/bin/env python3
"""
Intentionally broken image processor for debugging exercise.
This script will crash with an UnidentifiedImageError when run.
"""

from PIL import Image
import sys


def process_image(file_path):
    """Open and process an image file."""
    print(f"Attempting to open: {file_path}")

    try:
        img = Image.open(file_path)
    except Image.UnidentifiedImageError:
        print("Error: The file is not a valid image")
        sys.exit(1)

    print(f"Image format: {img.format}")
    print(f"Image size: {img.size}")

    return img


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python broken_image_processor.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    process_image(file_path)
