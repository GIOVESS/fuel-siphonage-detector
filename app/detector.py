import pandas as pd
from app.utils import validate_dataframe, convert_timestamp  

def detect_fuel_siphonage(df, fuel_drop_threshold=5.0):
    validate_dataframe(df)

    # Convert timestamp column
    df = convert_timestamp(df)

    # Calculate fuel drop difference
    df["fuel_drop"] = df["fuel_level"].diff()

    # Check if the engine is OFF
    df["is_engine_off"] = df["engine_status"].str.upper() == "OFF"

    # Check vehicle movement (minimal location change)
    df["location_change"] = df["location_lat"].diff().abs() + df["location_lon"].diff().abs()
    
    # Detect siphonage events (Significant fuel drop + Engine OFF + No movement)
    siphonage_events = df[
        (df["fuel_drop"] < -fuel_drop_threshold) &
        (df["is_engine_off"]) &
        (df["location_change"] < 0.0001)  # Minimal location change
    ]

    return siphonage_events[["timestamp", "vehicle_id", "fuel_drop", "location_lat", "location_lon"]]
