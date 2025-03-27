import geopy.distance
import pandas as pd

def calculate_distance(coord1, coord2):
    """
    Calculate the geodesic distance (in km) between two GPS coordinates.

    Args:
        coord1 (tuple): (latitude, longitude) of first location.
        coord2 (tuple): (latitude, longitude) of second location.

    Returns:
        float: Distance in kilometers.
    """
    return geopy.distance.geodesic(coord1, coord2).km

def is_vehicle_stationary(df, threshold_km=0.1):
    """
    Determines if the vehicle remains stationary based on GPS coordinates.

    Args:
        df (pd.DataFrame): DataFrame with 'location_lat' and 'location_lon' columns.
        threshold_km (float): Maximum distance threshold (in km) to consider stationary.

    Returns:
        bool: True if stationary, False otherwise.
    """
    coords = list(zip(df["location_lat"], df["location_lon"]))
    max_distance = max(calculate_distance(coords[0], coord) for coord in coords)
    return max_distance < threshold_km

def validate_dataframe(df):
    """
    Validates if the DataFrame contains all required columns.

    Args:
        df (pd.DataFrame): DataFrame to validate.

    Raises:
        ValueError: If required columns are missing.
    """
    required_columns = ["vehicle_id", "timestamp", "location_lat", "location_lon", "engine_status", "fuel_level"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

def convert_timestamp(df):
    """
    Converts 'timestamp' column to datetime format.

    Args:
        df (pd.DataFrame): DataFrame with a 'timestamp' column.

    Returns:
        pd.DataFrame: DataFrame with converted timestamps.
    """
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df
