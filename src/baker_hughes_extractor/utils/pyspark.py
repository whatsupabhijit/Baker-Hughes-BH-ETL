# Import libraries
import os
import logging
from pyspark.sql import SparkSession

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define data cleaning functions (assuming they're in a separate module)
from data_cleaning import clean_date, clean_rig_count, clean_state_province

# Get SparkSession (consider using environment variables for configuration)
spark = SparkSession.builder.getOrCreate()

# Load data from Excel files
us_df = spark.read.option("header", True).option("delimiter", "\t").csv("us_rig_counts.xlsx")
ca_df = spark.read.option("header", True).option("delimiter", "\t").csv("ca_rig_counts.xlsx")

# Clean and transform data (using separate functions)
us_df = us_df.withColumn("date", clean_date(us_df["date"])) \
            .withColumn("state", clean_state_province(us_df["State"])) \
            .withColumn("land_rigs", clean_rig_count(us_df["Land"])) \
            .withColumn("offshore_rigs", clean_rig_count(us_df["Offshore"])) \
            .select("date", "state", "land_rigs", "offshore_rigs") \
            .dropna(subset=["date", "state", "land_rigs", "offshore_rigs"])

ca_df = ca_df.withColumn("date", clean_date(ca_df["date"])) \
            .withColumn("province", clean_state_province(ca_df["Province"])) \
            .withColumn("land_rigs", clean_rig_count(ca_df["Land"])) \
            .withColumn("offshore_rigs", clean_rig_count(ca_df["Offshore"])) \
            .select("date", "province", "land_rigs", "offshore_rigs") \
            .dropna(subset=["date", "province", "land_rigs", "offshore_rigs"])

# Connect to PostgreSQL and write data (implement database connection and writing logic)
jdbc_url = "jdbc:postgresql://host:port/database"
jdbc_properties = {"user": "user", "password": "password"}

us_df.write.jdbc(url=jdbc_url, table="web_scrapes.rig_counts", mode="append", properties=jdbc_properties)
ca_df.write.jdbc(url=jdbc_url, table="web_scrapes.ca_rig_counts", mode="append", properties=jdbc_properties)


# Stop SparkSession
spark.stop()
