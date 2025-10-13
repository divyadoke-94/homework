from PIL import Image, ImageDraw, ImageFont

# Load the original image
image_path = "ChatGPT Image Oct 12, 2025, 07_14_52 PM.png"
img = Image.open(image_path)

# Create a drawing object
draw = ImageDraw.Draw(img)

# Define the new title
new_title = "Heart Disease Detection"

# Cover the old title with a white rectangle
draw.rectangle([(150, 10), (750, 90)], fill="white")

# Set up font (using default font)
font = ImageFont.load_default()

# Draw the new title text
draw.text((260, 35), new_title, fill="black", font=font)

# Save the updated image
img.save("heart-disease-detection-diagram.png")
print("✅ Image saved as 'heart-disease-detection-diagram.png'")
