from flask import Flask, render_template, jsonify
from karaoke_functions import read_lyrics_csv, get_song

app = Flask(__name__)

# Load lyrics once when app starts
lyrics_folder = "./song_lyrics/"
song_filename = get_song("songlist.csv")
lyrics_data = read_lyrics_csv(lyrics_folder + song_filename)


@app.route("/")
def index():
    return render_template('_index.html')

@app.route("/api/lyrics")
def get_all_lyrics():
    """API endpoint that returns all lyrics data at once"""
    return jsonify(lyrics_data)

if __name__ == "__main__":
    app.run(debug=True)