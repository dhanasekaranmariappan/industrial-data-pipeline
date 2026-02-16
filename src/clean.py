def clean_data(df):
    df = df.drop_duplicates()
    df = df.ffill()
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    return df