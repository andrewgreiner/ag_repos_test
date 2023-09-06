# Databricks notebook source
df = spark.read.table("homesales_demo.home_sales_brooklyn.brooklyn_sales")

display(df)

# COMMAND ----------

df.show()
