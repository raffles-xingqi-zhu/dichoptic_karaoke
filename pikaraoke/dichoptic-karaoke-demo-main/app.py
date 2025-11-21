from flask import Flask, render_template, jsonify
from karaoke_functions import read_lyrics_csv, get_song, get_lyrics_for_song
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

# Queue management
song_queue = []
current_song = None
lyrics_data = []
lyrics_folder = "./song_lyrics/"

# Example: Add some songs to the queue (replace with actual queue management)
queue_example = [
    "Backstreet Boys - I Want It That Way (Karaoke Version)---NxilU56kPu0.mp4",
    "Neil Diamond  - Sweet Caroline (Karaoke Version)---srLoAl1mhFw.mp4"
]

def load_next_song():
    """Load the next song from the queue"""
    global current_song, lyrics_data
    
    if song_queue:
        current_song = song_queue.pop(0)
        lyrics_data = get_lyrics_for_song(current_song, lyrics_folder)
        print(f"Loaded song: {current_song}")
    else:
        # Fallback to random song if queue is empty
        song_filename = get_song("songlist.csv")
        lyrics_data = read_lyrics_csv(lyrics_folder + song_filename)
        current_song = song_filename
        print(f"Queue empty, loaded random song: {song_filename}")

# Initialize with queue
song_queue = queue_example.copy()
load_next_song()

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

@app.route("/api/current-song")
def get_current_song():
    """API endpoint that returns the current song information"""
    return jsonify({
        "song": current_song,
        "has_lyrics": len(lyrics_data) > 0
    })

@app.route("/api/queue")
def get_queue():
    """API endpoint that returns the current song queue"""
    return jsonify({
        "queue": song_queue,
        "current_song": current_song
    })

@app.route("/api/queue/add/<song_name>", methods=["POST"])
def add_to_queue(song_name):
    """API endpoint to add a song to the queue"""
    song_queue.append(song_name)
    return jsonify({
        "message": f"Added {song_name} to queue",
        "queue_length": len(song_queue)
    })

@app.route("/api/next-song", methods=["POST"])
def next_song():
    """API endpoint to skip to the next song in queue"""
    load_next_song()
    return jsonify({
        "message": "Loaded next song",
        "current_song": current_song,
        "has_lyrics": len(lyrics_data) > 0
    })

if __name__ == "__main__":
    app.run(debug=True)