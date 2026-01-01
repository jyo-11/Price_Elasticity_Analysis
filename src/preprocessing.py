import pandas as pd
def load_and_clean_data(filepath):
    try:
        df= pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File is not found:{filepath}")

    #check for required columns
    required_cols= ['Unit price','Quantity']
    missing_cols=[col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing required columns:{missing_cols}")

    #remove rows with empty values
    initial_rows= len(df)
    df=df.dropna(subset=['Unit price','Quantity'])
    
    if len(df)==0:
        raise ValueError("No valid data remaining after removing missing values")
    
    rows_removed= initial_rows- len(df)
    if rows_removed>0:
        print(f"Removed {rows_removed} rows with missing values in key columns")
    return df

def rename_columns(df):
    df=df.copy()
    #rename the names
    df= df.rename(columns={
        'Unit price': 'price',
        'Quantity': 'quantity'     
    })

#check for required columns
    required_cols= ['price','quantity']
    missing_cols=[col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing required columns:{missing_cols}")

#removing negative or zero values
    initial_rows=len(df)
    df= df[(df['price']>0)&(df['quantity']>0)]

    if len(df)==0:
        raise ValueError("No valid data: all prices or quantities are zero or negative")
    
    rows_removed= initial_rows -len(df)
    print(f"removed{rows_removed} rows with non-positive price or quantity")

    return df

def calculate_summary_stats(df):
    required_cols =['price','quantity']
    missing_cols=[col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing required columns:{missing_cols}")
    
    #calculating ststistics
    stats={
        'mean_price': df['price'].mean(),
        'median_price': df['price'].median(),
        'std_price': df['price'].std(),
        'mean_quantity':df['quantity'].mean(),
        'median_quantity':df['quantity'].median(),
        'std_quantity': df['quantity'].std(),
        'n_observations': len(df)
    }
    return stats
    

