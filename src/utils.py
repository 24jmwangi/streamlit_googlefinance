def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Example preprocessing steps
    data.dropna(inplace=True)
    return data

def visualize_data(data):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.plot(data['x'], data['y'])
    plt.title('Sample Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()