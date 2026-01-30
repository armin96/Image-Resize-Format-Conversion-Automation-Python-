import os
from PIL import Image

SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

def process_images(
    input_folder,
    output_folder,
    max_width,
    max_height,
    output_format,
    preview=True
):
    os.makedirs(output_folder, exist_ok=True)

    files = [
        f for f in os.listdir(input_folder)
        if f.lower().endswith(SUPPORTED_FORMATS)
    ]

    if not files:
        print(" No images found")
        return

    print("\nProcessing images:\n")

    for filename in files:
        input_path = os.path.join(input_folder, filename)

        with Image.open(input_path) as img:
            img.thumbnail((max_width, max_height))

            name, _ = os.path.splitext(filename)
            new_name = f"{name}.{output_format.lower()}"
            output_path = os.path.join(output_folder, new_name)

            print(f"{filename} → {new_name} ({img.size[0]}x{img.size[1]})")

            if not preview:
                img.save(output_path, output_format.upper())

    if preview:
        print("\n Preview mode ON — no files saved")
    else:
        print("\n Images processed successfully")

if __name__ == "__main__":
    print("Image Resize & Format Conversion Tool")
    print("-----------------------------------")

    input_folder = input("Input folder: ").strip()
    output_folder = input("Output folder: ").strip()

    max_width = int(input("Max width (px): "))
    max_height = int(input("Max height (px): "))

    output_format = input("Output format (jpg/png/webp): ").strip()
    preview = input("Preview only? (y/n): ").lower() == "y"

    process_images(
        input_folder=input_folder,
        output_folder=output_folder,
        max_width=max_width,
        max_height=max_height,
        output_format=output_format,
        preview=preview
    )
