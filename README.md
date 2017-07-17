# Data-Pipeline
A data pipeline to ingest data from Twitter Streaming API or (Elastic/Flume/Kibana/Logstash) sender on different hosts. Processes the data using kafka and Spark and stores it into document store or columnar.

* Data ingestion - Different producers (ElasticSearch/Flume/Kibana)
* Stream processing - Kafka and Spark
* storage - DynamoDB/Rethink/Redis/Cassandra
