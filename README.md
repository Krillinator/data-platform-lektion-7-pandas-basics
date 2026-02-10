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

Think of it as:

* SQL table 
* Excel sheet 
* CSV in memory

### Series

A Series represents a single column in a DataFrame.
```python
df["price"]
```

Most helper methods are called on a Series.

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

## String helpers (.str)

Used when cleaning text.

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