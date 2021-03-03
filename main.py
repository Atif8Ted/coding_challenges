from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print(spark.sql("select current_timestamp").show())
for i in range(1, 10):
    print(i)
