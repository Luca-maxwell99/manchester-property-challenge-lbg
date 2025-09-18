# Manchester Property Data Wrangling and Enrichment Summary

This document outlines the data preparation process for the Manchester Property Sales Challenge. The objective was to clean, transform, and enrich the provided datasets to support geospatial analysis, dashboard development, and challenge question responses.

---

## Datasets Used

- `pp_data_man.parquet`: Property transaction records across Greater Manchester
- `pc_man.parquet`: Postcode metadata including latitude and longitude

---

## Cleaning Steps

### 1. Column Renaming
- Renamed all columns using a dictionary comprehension for clarity and consistency.
- Original columns such as `"column_1"` were mapped to descriptive names including `"id"`, `"price"`, `"date"`, `"postcode"`, and others.

### 2. Price Column
- Removed commas and surrounding quotes from the `price` field.
- Cast the cleaned string to `Float64` to enable numerical analysis.

### 3. Date Column
- Stripped quotes from the `date` field.
- Parsed the full datetime string (`"%Y-%m-%d %H:%M"`) into a proper `Date` type using `str.strptime`.

### 4. Postcode Column
- Stripped quotes from the `postcode` field to standardize formatting.
- Renamed the join key in the postcode metadata (`pcds` to `postcode`) to enable merging.

---

## Geospatial Enrichment

- Performed a left join between the property dataset and postcode metadata using the cleaned `postcode` field.
- Appended `lat` and `long` columns to each transaction, enabling spatial filtering and mapping.

---

## Status

The dataset is now:
- Cleaned and typed correctly
- Enriched with geospatial metadata
- Ready for analysis, dashboarding, and answering challenge questions

---

## Next Steps

- Handle missing values and standardize categorical fields
- Begin answering challenge questions with documented methodology
- Build Power BI dashboard using enriched dataset
- Push notebook and cleaned data pipeline to GitHub
- Prepare final presentation with insights and process overview
