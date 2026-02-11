# Pandas Data Cleaning & Helper Methods

Small demo project showing how to work with pandas DataFrames, clean messy data, and use common helper methods.
Used as an introduction to transformations, data quality, and basic ETL thinking.

---

## Clone
```bash
git clone <REPO_URL>
cd <REPO_NAME>
```

---

## Environment (uv + .venv)

This project uses **uv** with a local virtual environment.

### Install dependencies (including pandas)
```bash
uv add pandas
uv sync
```

### Run the script
```bash
uv run python main.py
```

---

## Core Concepts
### DataFrame

A DataFrame is a table-like structure with rows and columns.

```python
df = pd.DataFrame({...})
```

```python
    product_df = pd.DataFrame(
        {
            "id": ["SKU-1", "SKU-2", "SKU-3", "SKU-4", "SKU-5"],
            "name": ["shoes", "pants", "shirts", "sweaters", "designer jacket"],
            "price": [760, 520, 450, 550, 4500],
            "currency": ["SEK", "SEK", "SEK", "SEK", "SEK"], # TODO - Missing Values for CSV files when loaded (Crash)
        }
    )
```

Think of it as:

* SQL table 
* Excel sheet 
* CSV in memory

<img width="609" height="497" alt="Screenshot 2026-02-10 at 13 53 25" src="https://github.com/user-attachments/assets/23ead47b-1544-47dc-8895-3d88e7d07b83" />


### Series

A Series represents a single column in a DataFrame.
```python
df["price"]
```

Most helper methods are called on a Series. Therefore it's important to understand the datatypes that are returned

<img width="684" height="390" alt="Screenshot 2026-02-10 at 13 53 43" src="https://github.com/user-attachments/assets/9ec90df9-69b5-4f74-8e84-3b66d103478f" />

---


## Helper Methods
### Numeric helpers 

Used for basic analysis and sanity checks.

```python
df["price"].min()     # Lowest value
df["price"].max()     # Highest value
df["price"].mean()    # Average (mean)
df["price"].median()  # Middle value (robust to outliers)
```
### Sorting 

Sort rows by a column.

```python
df.sort_values("price")              # Ascending
df.sort_values("price", ascending=False)  # Descending
```

## DataFrame overview 

Quick stats for numeric columns.
```python
df.describe()
```

<img width="161" height="202" alt="Screenshot 2026-02-10 at 13 55 28" src="https://github.com/user-attachments/assets/e3557087-e4e2-4365-9aa6-e77ec62cacdf" />


## String helpers (.str)

Consider the following Dataframe

```python
    dirty_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", "Sku-3", "sku_4", "SKU-5 "],
            "name": [" Shoes", "pants ", "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", " 450", "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", "sek ", " SEK"],
        }
    )
```

Transformation of data often requires cleaning data, that's when datatype helpers can come in handy.

### Used when cleaning text.

```python
df["id"].str.strip()     # Remove whitespace start/end
df["name"].str.upper()   # ALL CAPS
df["name"].str.title()   # Title Case
```

### split


Split strings into parts (returns lists).

```python
df["id"].str.split("-")  # Example: "SKU-1" -> ["SKU", "1"]
```


Tip: if you need a specific part:

```python
df["id"].str.split("-").str[0]  # "SKU"
df["id"].str.split("-").str[1]  # "1"
```

### Missing values 

Detect real missing values (None / NaN).

```python
df.isna()            # DataFrame of True/False
df["price"].isna()   # Series of True/False
```

Common pattern: flag columns for later decisions.

```python
df["price_missing"] = df["price"].isna()
```

### Type casting

Convert a column to a new type.

```python
df["price"] = df["price"].astype(float)
```

Common use cases:
* numbers loaded as strings 
* calculations failing because dtype is wrong

---

## Import helpers (from_*)

Load data from files.

```python
pd.read_csv("products.csv")
pd.read_json("products.json")              # normal JSON
pd.read_json("products.jsonl", lines=True) # JSONL (one JSON per line)
```

## Export helpers (to_*)

Write DataFrames to files.

```python
df.to_csv("output.csv", index=False)
df.to_json("output.json", orient="records")
```

---

## Transform vs Validation - best practice 

Transform: clean/normalize/format (strip, upper, title, astype)

Validate: check rules (missing, negative price, wrong formats)

Example:
```
" 760 " -> 760.0 (transform)

missing price -> flag/reject decision (validate)
```
