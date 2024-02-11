# Baker-Hughes-BH-ETL

One of the research teams have requested to scrape data from Baker Hughes (BH) in order to understand changes in the weekly rig report. This repository will help to create a schema that will house the data and an ETL to extract the data from the excel file provided.

How to RUN locally

### Step1: Set the URL in terminal

`URL=https://github.com/whatsupabhijit/Baker-Hughes-BH-ETL/blob/main/requirements/`

### Step2: bulid the docker image

`cd src/baker_hughes_extractor/utils`
`docker build -t bh-rigs:0.0.1 .`

### Step3: run the image

`docker run -it \  bh-rigs:0.0.3 \                          
    --user=root \
    --password=root \
   --host=pg-database \ 
    --port=5432 \
    --db=bh_rigs \
    --table_name=bh_rigs_table \
    --url=${URL}`
