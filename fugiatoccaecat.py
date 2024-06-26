import pandas as pd
import pyspark.sql.functions as F

# Create a Spark DataFrame
spark_df = spark.createDataFrame([(1, "Alice"), (2, "Bob"), (3, "Charlie")], ["id", "name"])

# Convert the Spark DataFrame to a pandas DataFrame
pandas_df = spark_df.toPandas()

# Now you can work with the pandas DataFrame
print(pandas_df.head())
