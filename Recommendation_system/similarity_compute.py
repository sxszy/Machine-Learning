# -*- coding=utf-8 -*-
"""
similarity: Turn tags into vectors using count vector, and use lsh(minihash) to search
Author: Shi Zheyang
Date:2020/07/27
Modified Date: 2020/07/30
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.ml.feature import CountVectorizer
from pyspark.ml.feature import MinHashLSH
from pyspark.sql.functions import col
from functools import wraps
import sys
import time
import argparse


def timing(func):
    """
    计时装饰器
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        装饰函数
        """
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('[' + func.__name__ + ']used:' + str(end - start) + 's')
        return r

    return wrapper


def read_data_json(spark, data_path, is_show=True):
    """Read data from json, and select id, tags and default-language
    Args:
        spark: Spark session
        data_path: The path of data
        is_show: If true, the data would be shown
    Returns:
        data: data including video_id, tags, and default_language
    """
    data = spark.read.option("header", "true").option('encoding', 'utf-8').json(data_path)
    data.printSchema()
    data = data.filter(data['tags'] != "null").select('video_id', 'tags', 'default_language')
    if is_show:
        data.show()

    return data


def read_data_hive(spark, is_show=True):
    """Read data from hive, and select video_id, tags and default-language
    Args:
        spark: Spark session
        data_path: The path of data
        is_show: If true, the data would be shown
    Returns:
        data: data including video_id, tags, and default_language
    """
    data = spark.sql("select vedio_id, tags, default_language from common_dw.dim_video where tags != null AND proc_date = " + proc_date)
    if is_show:
        data.printSchema()
        data.show()

    return data


def process_data(data, is_show=True):
    """Split data using udf(sep=#)
    e.g.: "car#house#people" => [car, house, people]
    Args:
        data: Input data
        is_show: If true, the data would be shown
    Returns:
        data: Data including video_id, tags, default_language, tokens
    """
    auto_tokenizer = udf(lambda x: x.split(sep="#"), ArrayType(StringType()))
    data = data.withColumn("tokens", auto_tokenizer(col('tags')))
    if is_show:
        data.show(10)

    return data


def count_vector(data, vocabSize=1000000, is_show=True):
    """Use Countvectorizer to transform data
    Args:
        data: Input data
        vocabSize: The parameter used in CountVectorizer, which indicates the maximum number of vocab
        is_show: If true, the data would be shown
    Returns:
        result: The result of Countvectorizer
    """
    # minDF表示词语至少要在几篇文档中出现
    cv = CountVectorizer(inputCol="tokens", outputCol="result", vocabSize=vocabSize, minDF=2.0)
    model = cv.fit(data)
    isnonezero = udf(lambda x: x.numNonzeros() > 0, BooleanType())
    result = model.transform(data).filter(isnonezero(col("result"))).select('video_id', 'result', 'tags', 'default_language')
    if is_show:
        result.show(10)

    return result


def minilsh_sim(data, is_show=True, is_save=True):
    """Use minilsh to compute similarity
    Args:
        data: Input data
        is_show: If true, the data would be shown
        is_save: If true, the data would be saved
    """
    mh = MinHashLSH(inputCol='result', outputCol='hashes', numHashTables=5)
    print("minihash")
    data.show()
    mini_model = mh.fit(data)
    minilsh_data = mini_model.transform(data)
    if is_show:
        minilsh_data.show()

    # minilsh must not be all-zero vector
    # minilsh use jaccard distance:
    minilsh_result = mini_model.approxSimilarityJoin(minilsh_data, minilsh_data, 0.6, distCol="JaccardDistance"). \
        select(col("datasetA.video_id").alias("video_idA"), \
               col("datasetB.video_id").alias("video_idB"), \
               col("datasetA.tags").alias("tagsA"), \
               col("datasetB.tags").alias("tagsB"), \
               col("JaccardDistance"), \
               col('datasetA.default_language').alias('dlA') , \
               col('datasetB.default_language').alias('dlB')). \
        sort('video_idA')
    minilsh_result_filter = minilsh_result.filter(minilsh_result.video_idA != minilsh_result.video_idB).\
                                           filter(minilsh_result.dlA == minilsh_result.dlB)

    if is_show:
        minilsh_result_filter.show()

    if is_save:
        # minilsh_result_filter.toPandas().to_csv("final_result_mini.csv")
        # print("final_result_mini.csv has been saved")
        # Save dataframe in hive
        # First, you should have created a table in Hive
        # Second, Create a temp view for dataframe
        minilsh_result_filter.createTempView('temp_table')
        # Third, Insert the table using spark sql(should pass a proc_data to sql)
        spark.sql('INSERT OVERWRITE TABLE common_dw.dws_video_similiarity_recommend PARTITION(proc_date) \
        SELECT video_idA, video_idB, JaccardDistance,' + proc_date +' AS proc_date FROM temp_table')
        print("dws_video_similarity has been saved")

@timing
def count_lsh(spark, data_path, is_show=True, is_save=True, vocabSize=1000000):
    """Main procedure:
    1. Read data
    2. Preprocess data
    3. Use Countvetorizer to transform the result
    4. Use Minilsh to compute similarity
    """
    # Read
    tags_result = read_data_json(spark, data_path, is_show=is_show)
    # Process
    process_result = process_data(tags_result, is_show=is_show)
    # countvector
    countvector_result = count_vector(process_result, vocabSize=vocabSize, is_show=is_show)
    # lsh_sim
    minilsh_sim(countvector_result,  is_show=is_show, is_save=is_save)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Receive some parameters')
    parser.add_argument('--show', dest="show", action='store_true', help='show the data')
    parser.add_argument('--save', dest='save', action='store_true', help='save the result')
    parser.add_argument('--vocabSize', dest="vocabSize", type=int, help='The size of vocab')
    parser.add_argument('--proc_date', dest="proc_date", type=str)
    args = parser.parse_args()

    data_path = "../data/keep_drop_video.json"
    show = args.show
    save = args.save
    vocabSize = args.vocabSize
    proc_date = args.proc_date

    # Create a session
    spark = SparkSession.builder.appName("similarity_compute"). \
        config('encoding', 'UTF-8').\
        getOrCreate()

    count_lsh(spark, data_path, show, save)
    spark.stop()

