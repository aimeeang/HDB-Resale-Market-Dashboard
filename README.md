# Interactive HDB Resale Market Dashboard

This repository contains the code and resources for the Interactive HDB Resale Market Dashboard. The project uses data from data.gov.sg and the OneMap API to enhance the HDB resale flat dataset with geospatial information.

## Project Features
- **Data Enhancement**: Used Python and the OneMap API to generate missing latitude and longitude data.
- **Proximity Analysis**: Calculated the nearest MRT stations, including distance and walking time for each HDB Resale Flat transaction.
- **Educational and Commercial Insights**: Identified the top 5 closest schools and shopping malls for each flat with Python.
- **Interactive Dashboard**: Power BI dashboard that allows users to explore trends and proximity information.

## Screenshot
![Power BI Dashboard Screenshot](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/HDB_Dashboard_Screenshot.jpg) 
![Power BI Dashboard Screenshot](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/HDB_Dashboard_Screenshot_2.jpg) 

- [`HDB_TownAnalysis_Tool_Explanation.png`](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/HDB_TownAnalysis_Tool_Explanation.png): Town Analysis Explanation

## Project Presentation Slides
- [`HDB_Resale_OverviewPPT.pdf`](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/HDB_Resale_OverviewPPT.pdf): Project Presentation Slides

## Tools and Technologies
- Microsoft Power BI
- Python
- OneMap API

## Project Files
- [`geospatial_analysis.py`](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/geospatial_analysis.py): Python script for generating geospatial data.
- [`proximity_analysis.py`](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/proximity_analysis.py): Python script for calculating distances to MRT stations, schools, and malls.
- [`HDB-Resale-Market-Dashboard.pbix`](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/HDB%20Resale%20Flat%20Dashboard.pbix): Power BI dashboard file.
- [`README.md`](https://github.com/aimeeang/HDB-Resale-Market-Dashboard/blob/main/README.md): Project documentation.

## How to Run
1. Clone this repository.
2. Install required libraries.
3. Run the Python scripts to prepare the data.
4. Open the Power BI dashboard file to explore the visualizations.
