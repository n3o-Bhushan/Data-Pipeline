# Data-Pipeline
A data pipeline to ingest data from Twitter Streaming API. Processes the data using kafka and Spark and stores it into document store or columnar.

* Data ingestion - Different producers (ElasticSearch/Flume/Kibana)
* Stream processing - Kafka and Spark
* storage - DynamoDB/Rethink/Redis/Cassandra
* Feature - Use RethinkDB features to perform operations on change of the feed. Event based system.


[![Build Status](https://travis-ci.org/n3o-Bhushan/Data-Pipeline.svg?branch=master)](https://travis-ci.org/n3o-Bhushan/Data-Pipeline)
