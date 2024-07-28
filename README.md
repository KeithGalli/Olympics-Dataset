# Olympics-Dataset

This repo contains a comprehensive dataset on summer & winter Olympic athletes & their results between 1896-2022 (will be updated with 2024 results after the upcoming Paris Games)

![Olympic Flame](./assets/olympic_flame.jpeg)

## Dataset info & collection process

This data comes from [olympedia.org](https://www.olympedia.org/) and was web scraped with the Python Beautiful Soup library (see [scrape_data.py](./scrape_data.py))

- [datalake/bronze/athletes/bios.csv](./datalake/bronze/athletes/bios.csv) contains the raw biographical information on each athlete<br/>
- [datalake/bronze/results/results.csv](./datalake/bronze/results/results.csv) contains a row-by-row breakdown of each event athletes competed in and their results in that event.

### Datalake structure
``` 
Olympics-Dataset/
└── datalake/
   ├── bronze/ ## here goes the raw data
   │     ├── athletes/
   │     │    └── bios.csv   
   │     └── results/
   │          └── results.csv
   └── silver/ ## here goes the clean data
        ├── bios.csv
        └── results.csv
```

Note, in the process of scraping this dataset, temporary CSV files were created to checkpoint scraping progress. For simplicity these checkpointed files have since been removed from the repository.

## Clean Data

Easier to analyze data can be found in [clean-data/](./clean-data/) folder. In addition to the results and bios info, you can find data files with additional lat/long location data for athletes, NOC region codes, and historic populations of countries over time.
