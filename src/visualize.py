import matplotlib.pyplot as plt

def plot_temperature(df):
    plt.figure(figsize=(8,5))
    plt.scatter(df["air_temperature"], df["process_temperature"], c=df["tool_wear"], cmap="Oranges")
    plt.title("Temperature Relationship")
    plt.xlabel("Air Temp")
    plt.ylabel("Process Temp")
    plt.show()
