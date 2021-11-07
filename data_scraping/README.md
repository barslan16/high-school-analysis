DATA SCRAPING
# Data Scraping Part
The Council of Higher Education shared various data about universities between 2018-2020 on its website. In the study, these data were scrapped and an analysis was made.

The program scrapes the data of students in a total of 10617 departments from 223 different universities.

Each department has 30 different datasheets. In this study, 3 datasheets were used to perform the necessary analyzes. Variables of other datasheets are shared at the end of the yok_data_scraper.py file for use in future studies.

Each university is shown with a code on the website where the data was scraped. These codes are in the university_code.xlsx.

Not all data are included in this repo. Only sample data for each university type are included.

## Starting Scraping

1. Change directory to the directory where yok_data_scraper.py is located.


  ```pyfunctiontypecomment
   cd [Path]
   ```

2. Run:

 ```pyfunctiontypecomment
   python yok_data_scraper.py
   ```
   in your shell.
