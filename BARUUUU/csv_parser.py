import pandas as pd
import re
import argparse

def parse_message(msg):
    match = re.search(
        (
            r"Longitude:\s*(-?\d+\.\d+)\s+"
            r"Latitude:\s*(-?\d+\.\d+)\s+"
            r"Height:\s*(\d+\.\d+)\s+"
            r"X_velocity:\s*(-?\d+\.\d+)\s+"
            r"Y_velocity:\s*(-?\d+\.\d+)\s+"
            r"Z_velocity:\s*(-?\d+\.\d+)"
        ),
        msg
    )
    if match:
        return match.groups()
    return [None] * 6

def parse_dji_log(input_csv_path, output_csv_path):
    # Load CSV
    df = pd.read_csv(input_csv_path)

    # Filter for DJI Mavic DAT Log
    df_filtered = df[df['source_long'] == 'DJI Mavic DAT Log'].copy()

    # Extract message values
    df_filtered[['Longitude', 'Latitude', 'Height', 'X_velocity', 'Y_velocity', 
                 'Z_velocity']] = df_filtered['message'].apply(
                    lambda x: pd.Series(parse_message(x))
    )

    # Keep and rename columns
    df_final = df_filtered[['datetime', 'Longitude', 'Latitude', 'Height', 
                            'X_velocity', 'Y_velocity', 'Z_velocity', 
                            'display_name']].copy()
    df_final = df_final.rename(columns={'datetime': 'timestamp', 
                                        'display_name': 'path'})

    # Save to CSV
    df_final.to_csv(output_csv_path, index=False)
    print(f"Saved as {output_csv_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Parse DJI Mavic DAT Log from CSV.")
    parser.add_argument("input", help="Path to input CSV file")
    parser.add_argument("output", help="Path to output CSV file")
    args = parser.parse_args()

    parse_dji_log(args.input, args.output)
