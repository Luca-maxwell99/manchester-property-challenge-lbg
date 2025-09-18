# Manchester Property Data Wrangling and Enrichment Summary

This document outlines the data preparation workflow for the Manchester Property Sales Challenge, submitted to Lloyds Banking Group. The objective was to clean, transform, and enrich the provided datasets to support geospatial analysis, dashboard development, and analytical responses to the challenge questions.

## Datasets Used

- `pp_data_man.parquet` — Property transaction records across Greater Manchester  
- `pc_man.parquet` — Postcode metadata including latitude and longitude

## Wrangling Steps

### 1. Column Renaming
- Renamed all columns using a dictionary comprehension for clarity and consistency.
- Mapped headers (e.g. `"column_1"`) to descriptive names, as used in the project brief, such as `"id"`, `"price"`, `"date"`, `"postcode"`, `"property_type"`, and others.

### 2. Price Cleaning
- Removed commas and quotes from the `price` field.
- Cast to `Float64` for numerical analysis and sorting.

### 3. Date Parsing
- Stripped quotes from the `date` field.
- Parsed into a proper datetime object using `str.strptime`.

### 4. Postcode Standardisation
- Cleaned the `postcode` field to ensure consistent formatting.
- Renamed the join key in postcode metadata (`pcds` to `postcode`) to enable merging.

### 5. Categorical Mapping
- Standardised key categorical fields:
  - `property_type`: Mapped codes (`"F"`, `"S"`, `"D"`, `"T"`, `"O"`) to full labels, as shown in the project brief, (`"Flat"`, `"Semi Detached"`, etc.)
  - `new`: Converted `"Y"` and `"N"` to `"New Build"` and `"Old Build"`
  - `duration`: Converted `"F"` and `"L"` to `"Freehold"` and `"Leasehold"`

### 6. Derived Columns
- Extracted `year` from the `date` column for time-based filtering.
- Created `postal_sector` from the postcode for spatial grouping.

### 7. Geospatial Enrichment
- Performed a left join between the property dataset and postcode metadata.
- Appended `lat` and `long` columns to each transaction, enabling spatial filtering and mapping.

### 8. Handled missing values
- identified and handled nulls
- dropped records that had missing lat and long data, since geospatial analysis was a key part of the project. 
  
### 9. Checked Data Ranges
- I checked whether all data was within the scope provided by the project brief and filtered out records that were outside the scope. 

### 10. Extracted Cleaned Data
- Finally, I extracted my cleaned dataframe to a new parquet, ready for analysis. 


## Final Status

The dataset is now:
- Cleaned and typed correctly  
- Enriched with geospatial metadata  
- Standardised for categorical analysis  
- Ready for dashboarding and answering all challenge questions

> All data transformation was performed using Polars, as required by the project brief. Pandas was not used.

## Next Steps

- Finalise Power BI dashboard visuals for all seven questions  
- Push cleaned pipeline and notebooks to GitHub  
- Prepare final presentation with insights, methodology, and stakeholder-ready visuals
