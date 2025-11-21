import pandas as pd
from typing import List, Tuple

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