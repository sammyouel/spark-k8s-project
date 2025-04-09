# Use an official Spark Python base image matching our PySpark version
FROM apache/spark:3.4.1-python3

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY process_data.py /app/

# Copy the data directory into the container
COPY data /app/data/

# Although PySpark is included, if you had other dependencies,
# you would copy a requirements.txt file and run pip install:
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# No ENTRYPOINT or CMD needed, Spark operator will specify the entry point