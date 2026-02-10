import pandas as pd

if __name__ == '__main__':

    # Create a pandas DataFrame (tabular data in memory)
    product_df = pd.DataFrame(
        {
            "id": ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"],
            "name": ["shoes", "pants", "shirts", "sweaters", "designer jacket"],
            "price": [760, 520, 450, 550, 4500],
            "currency": ["SEK", "SEK", "SEK", "SEK", "SEK"], # TODO - Missing Values for CSV files when loaded (Crash)
        }
    )

    print(product_df)  # Print dataframe (fast for small datasets)

    # Built-in pandas helpers for numeric analysis
    print(product_df["price"].max())  # Highest value
    print(product_df["price"].min())  # Lowest value
    print(product_df["price"].mean())  # Arithmetic mean
    print(product_df["price"].median())  # Median (robust to outliers)

    print(product_df.describe())
    # Summary statistics for numeric columns:
    # count, mean, std, min, 25%, 50%, 75%, max

    print(product_df.sort_values("price"))
    # Sort rows by column value (ascending by default)
    # NOTE: pandas does NOT guarantee a specific sorting algorithm

    # Export dataframe to CSV
    product_df.to_csv("products.csv", index=False)
    # Saved to current working directory (usually project folder)

    ######################################################
    ################## DIRTY DATAFRAME ###################
    ######################################################

    # Simulated messy / real-world input data
    dirty_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", "Sku-3", "sku_4", "SKU5 "],
            "name": [" Shoes", "pants ", "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", " 450", "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", "sek ", " SEK"],
        }
    )

    ## IMPORTANT ##
    # dirty_df["id"].str.strip() alone does NOT modify the dataframe
    # String operations return a new Series and must be reassigned
    dirty_df["id"] = dirty_df["id"].str.strip()  # Remove leading/trailing whitespace
    dirty_df["id"] = dirty_df["id"].str.upper()  # Normalize casing
    dirty_df["id"] = (
        dirty_df["id"]
        .str.replace(" ", "")  # Remove internal spaces
        .str.replace("_", "-")  # Normalize separators
    )

    ## EDGE CASES ##
    # SKU4  -> Missing "-" (not added automatically)
    # SKU--4 -> Multiple "-" would not be fixed
    # These require validation rules, not just cleaning

    dirty_df["price"] = dirty_df["price"].astype(float)
    # Explicit type casting: string -> float

    dirty_df["name"] = dirty_df["name"].str.strip()
    dirty_df["name"] = dirty_df["name"].str.title()
    dirty_df["name"] = dirty_df["name"].str.replace(
        r"\s+", " ", regex=True
    )
    # Regex explanation:
    # \s+  = one or more whitespace characters
    # Replaces multiple spaces with a single space

    print(dirty_df.values)  # Raw NumPy representation (loses column labels)

    #####################################################
    ############## MISSING DATA DATAFRAME ###############
    #####################################################

    # Dataset containing actual missing values (None -> NaN)
    missing_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", None, "sku_4", "SKU5 "],
            "name": [" Shoes", None, "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", None, "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", None, " SEK"],
        }
    )

    print(missing_df.isna()) # isna() detects true missing values (NaN / None)

    # Flag missing values per column
    # This keeps rows but allows decision-making later (drop, fix, reject, etc.)
    missing_df["id_missing"] = missing_df["id"].isna()
    missing_df["name_missing"] = missing_df["name"].isna()
    missing_df["price_missing"] = missing_df["price"].isna()
    missing_df["currency_missing"] = missing_df["currency"].isna()

    print(missing_df)