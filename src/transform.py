def add_features(df):
    df["power"] = df["torque_[nm]"] * df["rotational_speed_[rpm]"]
    df["temp_diff"] = df["process_temperature_[k]"] - df["air_temperature_[k]"]
    return df