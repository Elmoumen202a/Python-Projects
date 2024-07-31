import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def analyze_data(df):
    """Perform basic data analysis."""
    summary = df.describe()
    return summary

def save_data(df, file_path):
    """Save DataFrame to a CSV file."""
    df.to_csv(file_path, index=False)

def main():
    input_file = 'data.csv'
    output_file = 'summary.csv'
    
    # Load data
    df = load_data(input_file)
    
    # Analyze data
    summary_df = analyze_data(df)
    
    # Save analysis summary
    save_data(summary_df, output_file)
    print(f"Analysis summary saved to {output_file}")

if __name__ == "__main__":
    main()
