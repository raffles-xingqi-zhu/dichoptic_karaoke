from flask import Flask, render_template, request
import os
import random  # <-- needed for random.choice

app = Flask(__name__)

# Configuration Variables
TEXT_FILE = 'text.txt'  # File to read text from
COLOR_1 = '#000000'  # Black
COLOR_2 = '#00FFFF'  # Cyan
COLOR_3 = '#FF0000'  # Red
BACKGROUND_COLOR = '#FFFEF7'  # Very light grey 
FONT_FAMILY = 'Courier New'  # Font
FONT_SIZE = '48px'  # Font size
DEFAULT_CONTRAST = 1


def adjust_color_contrast(hex_color, contrast):
    """
    Adjust color contrast relative to white background.
    contrast < 1.0: lighter (less contrast)
    contrast = 1.0: original color
    contrast > 1.0: darker (more contrast)
    """
    # Remove '#' and convert to RGB
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    
    # Adjust each channel (move toward 0 for more contrast, toward 255 for less)
    if contrast > 1.0:
        # Increase contrast by making darker
        r = int(r / contrast)
        g = int(g / contrast)
        b = int(b / contrast)
    else:
        # Decrease contrast by making lighter
        r = int(r + (255 - r) * (1 - contrast))
        g = int(g + (255 - g) * (1 - contrast))
        b = int(b + (255 - b) * (1 - contrast))
    
    # Clamp values between 0-255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    return f'#{r:02x}{g:02x}{b:02x}'


@app.route("/")
def hello_world():
    # Get contrast level from URL parameter or use default
    contrast = float(request.args.get('contrast', DEFAULT_CONTRAST))
    
    # Read text from file
    try:
        with open(TEXT_FILE, 'r', encoding='utf-8') as f:
            text_content = f.read()
    except FileNotFoundError:
        text_content = 'Error: text.txt not found. Please create a text.txt file in the same directory.'
     # Split text into words
    words = text_content.split()

    # Create a list of (word, color) pairs with random colors
    colors = [adjusted_color1, adjusted_color2, adjusted_color3]
    colored_words = [
        (word, random.choice(colors))
        for word in words
    ]
    # Apply contrast adjustment to base colors
    adjusted_color1 = adjust_color_contrast(COLOR_1, contrast)
    adjusted_color2 = adjust_color_contrast(COLOR_2, contrast)
    adjusted_color3 = adjust_color_contrast(COLOR_3, contrast)

    from flask import Flask, render_template, request
import os
import random  # needed for random.choice

app = Flask(__name__)

# Configuration Variables
TEXT_FILE = 'text.txt'  # File to read text from
COLOR_1 = '#000000'  # Black
COLOR_2 = '#00FFFF'  # Cyan
COLOR_3 = '#FF0000'  # Red
BACKGROUND_COLOR = '#FFFEF7'  # Very light grey 
FONT_FAMILY = 'Courier New'  # Font
FONT_SIZE = '36px'  # Font size
DEFAULT_CONTRAST = 1


def adjust_color_contrast(hex_color, contrast):
    """
    Adjust color contrast relative to white background.
    contrast < 1.0: lighter (less contrast)
    contrast = 1.0: original color
    contrast > 1.0: darker (more contrast)
    """
    # Remove '#' and convert to RGB
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
    
    # Adjust each channel (move toward 0 for more contrast, toward 255 for less)
    if contrast > 1.0:
        # Increase contrast by making darker
        r = int(r / contrast)
        g = int(g / contrast)
        b = int(b / contrast)
    else:
        # Decrease contrast by making lighter
        r = int(r + (255 - r) * (1 - contrast))
        g = int(g + (255 - g) * (1 - contrast))
        b = int(b + (255 - b) * (1 - contrast))
    
    # Clamp values between 0-255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    return f'#{r:02x}{g:02x}{b:02x}'


@app.route("/")
def hello_world():
    # Get contrast level from URL parameter or use default
    contrast = float(request.args.get('contrast', DEFAULT_CONTRAST))
    
    # Read text from file
    try:
        with open(TEXT_FILE, 'r', encoding='utf-8') as f:
            text_content = f.read()
    except FileNotFoundError:
        text_content = 'Error: text.txt not found. Please create a text.txt file in the same directory.'
    
    # Apply contrast adjustment to base colors
    adjusted_color1 = adjust_color_contrast(COLOR_1, contrast)
    adjusted_color2 = adjust_color_contrast(COLOR_2, contrast)
    adjusted_color3 = adjust_color_contrast(COLOR_3, contrast)

    # Split text into words
    words = text_content.split()

    # Create a list of (word, color) pairs with random colors
    colors = [adjusted_color1, adjusted_color2, adjusted_color3]
    colored_words = [
        (word, random.choice(colors))
        for word in words
    ]

    # Render template with colored_words
    return render_template(
        "index.html",
        colored_words=colored_words,
        bg_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        font_size=FONT_SIZE,
        contrast=contrast
    )
if __name__ == "__main__":
    app.run(debug=True)
