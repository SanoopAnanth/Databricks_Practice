import dlt

@dlt.table(
    name='demo_tbl'
)
def demo_tbl():
  return spark.range(100)