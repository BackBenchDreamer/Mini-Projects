from PIL import Image, ImageDraw
import os

def create_diamond_image(size, color=(255, 255, 255, 128)):
    """Create an image with a diamond shape."""
    diamond_image = Image.new('RGBA', size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(diamond_image)
    
    # Diamond coordinates (centered in the image)
    width, height = size
    coords = [
        (width // 2, 0),
        (width, height // 2),
        (width // 2, height),
        (0, height // 2)
    ]
    
    # Draw the diamond
    draw.polygon(coords, fill=color)
    
    return diamond_image

def add_diamond_watermark(input_image_path, output_image_path, diamond_size=(100, 100), spacing=10):
    """Add repeated diamond watermark to an image."""
    # Check if input image exists
    if not os.path.isfile(input_image_path):
        print(f"Error: The file '{input_image_path}' does not exist.")
        return

    # Open the original image
    try:
        original_image = Image.open(input_image_path).convert("RGBA")
    except IOError:
        print(f"Error: Cannot open the image file '{input_image_path}'.")
        return
    
    width, height = original_image.size

    # Create diamond watermark image
    diamond_image = create_diamond_image(diamond_size)
    diamond_width, diamond_height = diamond_image.size
    
    # Create a new image for the result
    result_image = Image.new('RGBA', original_image.size)
    result_image.paste(original_image, (0, 0))
    
    # Draw diamonds in a grid pattern
    for x in range(0, width, diamond_width + spacing):
        for y in range(0, height, diamond_height + spacing):
            result_image.paste(diamond_image, (x, y), diamond_image)
    
    # Convert result image to RGB before saving as JPEG
    result_image_rgb = result_image.convert("RGB")
    
    # Save the image with watermark
    try:
        result_image_rgb.save(output_image_path, format='JPEG')
        print(f"Watermark added successfully! Saved to '{output_image_path}'")
    except IOError as e:
        print(f"Error: Cannot save the image to '{output_image_path}'. Details: {e}")

if __name__ == "__main__":
    # Use relative paths for files in the same directory as the script
    input_path = "input.jpg"  # Path to the input image (relative)
    output_path = "output_image_with_diamond_watermark.jpg"  # Path to save the output image (relative)

    # Change the working directory to where the script is located
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Print the current working directory
    print("Current Working Directory:", os.getcwd())

    add_diamond_watermark(input_path, output_path)
