import csv
from typing import List, Tuple

# def read_lyrics_csv(filename: str) -> List[Tuple[str, float]]:
#     """
#     Read lyrics and timestamps (in seconds) from a CSV file.
    
#     Args:
#         filename: Path to the CSV file
        
#     Returns:
#         List of tuples: [(lyrics, timestamp_in_seconds), ...]
#     """
#     lyrics_data = []
    
#     try:
#         with open(filename, 'r', encoding='utf-8') as csvfile:
#             reader = csv.reader(csvfile)
#             next(reader)  # Skip header row
            
#             for row in reader:
#                 if len(row) >= 2:
#                     lyrics = row[0].strip()
#                     timestamp_str = row[1].strip()
                    
#                     # Expect timestamp directly in seconds
#                     timestamp = float(timestamp_str)
                    
#                     lyrics_data.append((lyrics, timestamp))
    
#     except FileNotFoundError:
#         print(f"Error: {filename} not found")
#         return []
#     except ValueError:
#         print("Error: Could not parse timestamp (ensure it's a number in seconds)")
#         return []
    
#     return lyrics_data


def read_lyrics_csv(filename: str) -> List[Tuple[str, float]]:
    """
    Read lyrics and timestamps from a CSV file.
    
    Args:
        filename: Path to the CSV file
        
    Returns:
        List of tuples: [(lyrics, timestamp_in_seconds), ...]
    """
    lyrics_data = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header row
            
            for row in reader:
                if len(row) >= 2:
                    lyrics = row[0].strip()
                    timestamp_str = row[1].strip()
                    
                    # Convert M:SS or MM:SS format to seconds
                    if ':' in timestamp_str:
                        parts = timestamp_str.split(':')
                        minutes = int(parts[0])
                        seconds = int(parts[1])
                        timestamp = minutes * 60 + seconds
                    else:
                        timestamp = float(timestamp_str)
                    
                    lyrics_data.append((lyrics, timestamp))
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    except ValueError:
        print("Error: Could not parse timestamp")
        return []
    
    return lyrics_data


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