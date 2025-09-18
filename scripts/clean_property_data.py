import polars as pl

# Rename raw column headers to descriptive names
def rename_columns(df):
    rename_map = {
        "column_1": "id",
        "column_2": "price",
        "column_3": "date",
        "column_4": "postcode",
        "column_5": "property_type",
        "column_6": "new",
        "column_7": "duration",
        "column_8": "paon",
        "column_9": "saon",
        "column_10": "street",
        "column_11": "locality",
        "column_12": "town_city",
        "column_13": "district",
        "column_14": "county"
    }
    return df.rename(rename_map)

# Clean price and date columns for analysis
def clean_price_and_date(df):
    df = df.with_columns([
        pl.col("price").str.replace_all(",", "").str.strip_chars('"').cast(pl.Float64),
        pl.col("date").str.strip_chars('"').str.strptime(pl.Date, "%Y-%m-%d %H:%M")
    ])
    return df

# Standardise postcode formatting
def clean_postcode(df):
    return df.with_columns([
        pl.col("postcode").str.strip_chars('"')
    ])

# Map categorical codes to readable labels
def map_categoricals(df):
    type_map = {"F": "Flat", "S": "Semi Detached", "D": "Detached", "T": "Terraced", "O": "Other"}
    new_map = {"Y": "New Build", "N": "Old Build"}
    duration_map = {"F": "Freehold", "L": "Leasehold"}

    df = df.with_columns([
        pl.col("property_type").map_dict(type_map),
        pl.col("new").map_dict(new_map),
        pl.col("duration").map_dict(duration_map)
    ])
    return df

# Add derived columns for year and postal sector
def add_derived_columns(df):
    df = df.with_columns([
        pl.col("date").dt.year().alias("year"),
        pl.col("postcode").str.split(" ").list.get(0).alias("postal_sector")
    ])
    return df

# Join postcode metadata to enrich with latitude and longitude
def join_postcodes(df, postcode_df):
    postcode_df = postcode_df.rename({"pcds": "postcode"})
    return df.join(postcode_df, on="postcode", how="left")

# Main cleaning pipeline
def clean_property_data(pp_path, pc_path, output_path):
    # Load raw data
    df = pl.read_parquet(pp_path)
    postcode_df = pl.read_parquet(pc_path)

    # Apply cleaning steps
    df = rename_columns(df)
    df = clean_price_and_date(df)
    df = clean_postcode(df)
    df = map_categoricals(df)
    df = add_derived_columns(df)
    df = join_postcodes(df, postcode_df)

    # Save cleaned dataset
    df.write_parquet(output_path)
    print("Cleaned data saved to:", output_path)

# Run the cleaning pipeline
if __name__ == "__main__":
    clean_property_data(
        pp_path="data/pp_data_man.parquet",
        pc_path="data/pc_man.parquet",
        output_path="data/clean_property_data.parquet"
    )
