import pandas as pd
from typing import List, Tuple, Optional
from lyricDict import SongNameToLyricsFilePath

def get_song(song_list_filepath: str):
    # load csv
    df = pd.read_csv(song_list_filepath)
    value = df.sample(1).iloc[0] 
    song_filepath =  value["filename"]

    # Assert it's a string
    assert isinstance(song_filepath, str), "Value is not a string"
     
    return song_filepath

def read_lyrics_csv(filename: str) -> List[Tuple[float, float, str]]:
    """
    Read lyrics and timestamps from a CSV file using pandas.
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        List of tuples: [(start_time_in_seconds, end_time_in_seconds, text), ...]
    """
    try:
        df = pd.read_csv(filename)

        # Make sure required columns exist
        required_columns = {"Start time (s)", "End time (s)", "Text"}
        if not required_columns.issubset(df.columns):
            raise ValueError(f"CSV must contain columns: {required_columns}")
        
        # Convert to list of tuples
        return list(df[["Start time (s)", "End time (s)", "Text"]].itertuples(index=False, name=None))
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []


def get_current_lyric(lyrics_data: List[Tuple[str, float]], current_time: float) -> str:
    """
    Get the lyric that should be displayed at the current time.
    
    Args:
        lyrics_data: List of (lyrics, timestamp) tuples
        current_time: Current time in seconds
        
    Returns:
        The lyric to display, or empty string if no match
    """
    current_lyric = ""
    
    for lyric, timestamp in lyrics_data:
        if timestamp <= current_time:
            current_lyric = lyric
        else:
            break
    
    return current_lyric


def get_lyrics_filename(song_name: str) -> Optional[str]:
    """
    Map a song name to its corresponding lyrics filename using the lyrics dictionary.
    
    Args:
        song_name: The name of the queued song
        
    Returns:
        The filename of the lyrics CSV file, or None if not found
    """
    return SongNameToLyricsFilePath.get(song_name)


def get_lyrics_for_song(song_name: str, lyrics_folder: str = "./song_lyrics/") -> List[Tuple[float, float, str]]:
    """
    Get lyrics data for a specific song by name.
    
    Args:
        song_name: The name of the queued song
        lyrics_folder: Path to the folder containing lyrics files
        
    Returns:
        List of tuples containing lyrics data, or empty list if not found
    """
    lyrics_filename = get_lyrics_filename(song_name)
    if lyrics_filename:
        return read_lyrics_csv(lyrics_folder + lyrics_filename)
    else:
        print(f"Warning: No lyrics file found for song: {song_name}")
        return []
