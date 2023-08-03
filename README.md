# Big Data Analytics in the cloud Assignment
Student Name: Alicia Chong Tsui Ying  
Student ID: 20074290

### Dataset
Dataset can be downloaded from AWS S3 Bucket with the following command 
- `wget https://alicia-aws-bucket.s3.amazonaws.com/BookCorpus_small.zip`

### Codes
#### A. Conventional Method with Python
- **Script**
  - `mapper.py` - Mapper
  - `reducer.py`- Reducer  
- **Code Execution Command**
  - `$ time cat bookCorpus_small/* | ./mapper.py | sort | ./reducer.py > python_conven_wc.txt`
- **Results**
  - `python_conven_wc.txt`   

#### B. MapReduce with Python (HDFS)
- **Script**
  - `mapper.py` - Mapper
  - `reducer.py`- Reducer 
- **Code Execution Command**
```
$ time hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar 
      -input bookCorpus_small -output python_mr_wc 
      -file /home/hadoop/assignment/python/mapper.py 
      -mapper /home/hadoop/assignment/python/mapper.py 
      -file /home/hadoop/assignment/python/reducer.py 
      -reducer /home/hadoop/assignment/python/reducer.py
```
#### C. Spark on standalone in Masternode mode
- **Scirpt**
  - `spark_wc_local.py` - Mapper & Reducer
- **Code Execution Command**
  - `$ time spark-submit spark_wc_local.py`
- **Results**
  - `spark_wc_local.txt`

#### D. Spark on standalone in Cluster mode
- **Scirpt**   
  - `spark_wc_cluster.py` - Mapper & Reducer
- **Code Execution Command**
  - `$ time spark-submit spark_wc_cluster.py`
- **Results**
  - `spark_wc_cluster.txt`
  
