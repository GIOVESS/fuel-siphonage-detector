import streamlit as st
import pandas as pd
from detector import detect_fuel_siphonage  

# Streamlit Page Configuration
st.set_page_config(page_title="Fuel Siphonage Detector", layout="wide")

st.title("Fuel Siphonage Detection System")
st.write("Upload vehicle telemetry logs to detect fuel siphonage events.")

# File Upload
uploaded_file = st.file_uploader(" Upload CSV file", type=["csv"])

if uploaded_file:
    # Load CSV into DataFrame
    df = pd.read_csv(uploaded_file)

    # Display uploaded data
    st.subheader("Uploaded Data Preview")
    st.dataframe(df.head())

    # Run Detection
    if st.button(" Detect Fuel Siphonage"):
        siphonage_events = detect_fuel_siphonage(df)

        if not siphonage_events.empty:
            st.success(f"{len(siphonage_events)} potential siphonage events detected!")
            st.dataframe(siphonage_events)

            # Download results
            csv = siphonage_events.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="Download Results",
                data=csv,
                file_name="detected_siphonage.csv",
                mime="text/csv"
            )
        else:
            st.info("ℹNo siphonage events detected.")

# Footer
st.markdown(" Developed by **Giovanni Bwayo**")
