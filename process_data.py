from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Application entry point
if __name__ == "__main__":
    print("Starting Spark Application...")

    # Create SparkSession
    # When running on K8s, SparkConf is usually handled by the submission process
    spark = SparkSession.builder \
        .appName("TitanicDataProcessing") \
        .getOrCreate()

    print("SparkSession Created.")

    # Define the path INSIDE the container where data will be
    # This path is determined by how we build the Docker image later
    input_path = "/app/data/train.csv"
    print(f"Reading data from {input_path}")

    try:
        # Read data
        df = spark.read.csv(input_path, header=True, inferSchema=True)
        print("Data loaded successfully.")
        df.printSchema()

        print(f"Total rows: {df.count()}")

        # Simple analysis: Count passengers by Sex
        print("Passenger Count by Sex:")
        passenger_counts = df.groupBy("Sex").agg(count("*").alias("count"))
        passenger_counts.show()

    except Exception as e:
        print(f"Error during Spark processing: {e}")

    finally:
        # Stop SparkSession
        print("Stopping SparkSession.")
        spark.stop()
        print("Spark Application Finished.")