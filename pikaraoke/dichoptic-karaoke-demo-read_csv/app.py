from flask import Flask, render_template, jsonify
from karaoke_functions import read_lyrics_csv

app = Flask(__name__)

# Load lyrics once when app starts
lyrics_folder = "./song_lyrics/"
song_filename = "lyrics.csv"
lyrics_data = read_lyrics_csv(lyrics_folder + song_filename)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/api/lyrics")
def get_all_lyrics():
    """API endpoint that returns all lyrics data at once"""
    print(lyrics_data)
    return jsonify(lyrics_data)

if __name__ == "__main__":
    app.run(debug=True)