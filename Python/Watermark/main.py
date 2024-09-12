from PIL import Image, ImageDraw, ImageFont
import os

def add_watermark(input_image_path, output_image_path, watermark_text):
    # Check if input image exists
    if not os.path.isfile(input_image_path):
        print(f"Error: The file '{input_image_path}' does not exist.")
        return

    # Open the original image
    try:
        original_image = Image.open(input_image_path)
    except IOError:
        print(f"Error: Cannot open the image file '{input_image_path}'.")
        return
    
    width, height = original_image.size

    # Create an ImageDraw object
    draw = ImageDraw.Draw(original_image)

    # Choose a font and size
    font_size = 36
    try:
        # Load a TTF font (Ensure you have 'arial.ttf' or use a font available in your system)
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        # If the specified font is not available, use the default font
        print("Warning: 'arial.ttf' not found. Using default font.")
        font = ImageFont.load_default()

    # Calculate text size and position
    try:
        # For Pillow 8.0.0 and later
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        # For earlier versions of Pillow
        text_width, text_height = draw.textsize(watermark_text, font=font)

    text_x = width - text_width - 10  # 10 pixels from the right edge
    text_y = height - text_height - 10  # 10 pixels from the bottom edge

    # Draw the watermark text on the image
    draw.text((text_x, text_y), watermark_text, font=font, fill=(255, 255, 255, 128))

    # Save the image with watermark
    try:
        original_image.save(output_image_path)
        print(f"Watermark added successfully! Saved to '{output_image_path}'")
    except IOError:
        print(f"Error: Cannot save the image to '{output_image_path}'.")

if __name__ == "__main__":
    # Change the working directory to where the image is located
    os.chdir("C:/Users/Kitsune/Documents/Rep/Mini-Projects/Python/Watermark")

    # Print the current working directory
    print("Current Working Directory:", os.getcwd())

    # Use relative paths for files in the same directory as the script
    input_path = "input.jpg"  # Path to the input image
    output_path = "output_image_with_watermark.jpg"  # Path to save the output image
    watermark = "WATERMARK"  # Watermark text

    add_watermark(input_path, output_path, watermark)