from flask import Flask, render_template, jsonify
from karaoke_functions import read_lyrics_csv, get_song
from dichoptic_functions import adjust_color_contrast

app = Flask(__name__)

# Configuration variables ====================================
COLOR_1 = '#000000'  # Black
COLOR_2 = '#00FFFF'  # Cyan
COLOR_3 = '#FF0000'  # Red

hex_colours = [COLOR_1, COLOR_2, COLOR_3]
contrasts = [1.0, 0.9, 0.6]

adjusted_colours = []

for i in range(len(hex_colours)):
    adjusted_colour = adjust_color_contrast(hex_colours[i], contrasts[i])
    adjusted_colours.append(adjusted_colour)
    
BACKGROUND_COLOR = '#FFFEF7'  # Very light grey 
FONT_FAMILY = "Roboto Flex"  # Font
FONT_SIZE = '36px'  # Font size

# Load lyrics once when app starts
lyrics_folder = "./song_lyrics/"
song_filename = get_song("songlist.csv")
lyrics_data = read_lyrics_csv(lyrics_folder + song_filename)

@app.route("/")
def index():
    return render_template(
        "index.html",
        adjusted_colours = adjusted_colours,
        bg_color=BACKGROUND_COLOR,
        font_family=FONT_FAMILY,
        font_size=FONT_SIZE
    )

@app.route("/api/lyrics")
def get_all_lyrics():
    """API endpoint that returns all lyrics data at once"""
    return jsonify(lyrics_data)

if __name__ == "__main__":
    app.run(debug=True)