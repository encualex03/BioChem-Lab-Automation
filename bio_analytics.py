import pandas as pd
import numpy as np

def process_lab_results(input_file, output_file):
    print(f"🚀 Starting processing for: {input_file}...")
    
    try:
        # 1. Data Ingestion
        # Here I load the raw laboratory data from a CSV file into 
        # a Pandas DataFrame.
        df = pd.read_csv(input_file)
        
        # 2. Data Cleaning
        # Here I convert the 'Absorbance' column to numeric. 
        # By using errors='coerce', I ensure that any non-numeric 
        # entries (like 'ERROR' or text) are turned into NaN (Not a Number).
        initial_count = len(df)
        df['Absorbance'] = pd.to_numeric(df['Absorbance'], errors='coerce')
        
        # Here I drop the NaN values to ensure the dataset 
        # only contains processable numbers.
        df = df.dropna(subset=['Absorbance'])
        
        # Here I filter out physically impossible values 
        # (Absorbance cannot be negative).
        df = df[df['Absorbance'] >= 0]
        
        cleaned_count = len(df)
        print(f"✅ Cleaning complete. Removed {initial_count - cleaned_count} erroneous entries.")

        # 3. Scientific Calculation (Beer-Lambert Law)
        # Here I define the constants: Molar Extinction Coefficient (EPSILON)
        # and path length.
        EPSILON = 5500
        PATH_LENGTH = 1
        
        # Here I perform a vectorized calculation to determine the concentration 
        # for all samples at once.
        df['Concentration_M'] = df['Absorbance'] / (EPSILON * PATH_LENGTH)

        # 4. Statistical Insights
        # Here I calculate key metrics to provide a quick overview 
        # of the experimental results.
        avg_conc = df['Concentration_M'].mean()
        max_conc = df['Concentration_M'].max()
        
        # 5. Export Reporting
        # Here I export the final, cleaned, and calculated dataset 
        # to a new CSV file for further use.
        df.to_csv(output_file, index=False)
        print(f"📊 Analysis complete! Mean: {avg_conc:.6f} M | Max: {max_conc:.6f} M")
        print(f"💾 Results saved to: {output_file}")

    except FileNotFoundError:
        print("❌ Error: The input file was not found!")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# --- SIMULATION EXECUTION ---
if __name__ == "__main__":
    # Here I generate a mock dataset to demonstrate the script's 
    # ability to handle dirty data.
    test_data = {
        'Sample_ID': [f'S_{i}' for i in range(1, 11)],
        'Absorbance': [0.45, 0.12, 'DATA_CORRUPT', 0.89, -0.05, 0.33, 0.21, 0.44, 0.90, 0.15]
    }
    pd.DataFrame(test_data).to_csv('raw_lab_data.csv', index=False)
    
    # Here I call the main processing function.
    process_lab_results('raw_lab_data.csv', 'final_analysis_report.csv')