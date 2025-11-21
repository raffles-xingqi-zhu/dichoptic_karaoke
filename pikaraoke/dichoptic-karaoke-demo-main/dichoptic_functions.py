# import functions if needed


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