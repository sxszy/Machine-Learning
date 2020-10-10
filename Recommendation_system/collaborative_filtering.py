# -*- coding=utf-8 -*-
"""
collaborative_filtering: Train a collaborative filtering model and recommend for all users;
Author: Shi Zheyang
Date:2020/08/05
Modified Date: 2020/08/12
"""
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import StringIndexer, IndexToString
from pyspark.sql.types import *
from pyspark.sql.functions import col, array, lit, struct, explode
from functools import wraps
import time
import argparse


def timing(func):
    """
    Timing wrapper
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        """
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('[' + func.__name__ + ']used:' + str(end - start) + 's')
        return r

    return wrapper


def read_data_hive(spark, input_list, is_show=True):
    """Read data from hive, and select video_id, tags and default-language
    Args:
        spark: Spark session
        input_user: User column
        input_video: Video column
        input_rating: Rating column
        is_show: If true, the data would be shown
    Returns:
        data: Data including video_id, tags, and default_language
    """
    # TO DO
    input_string = ",".join(input_list)
    data = spark.sql(
        "select " + input_string + " from xxx where proc_date = " + proc_date)

    if is_show:
        data.printSchema()
        data.show()

    return data


def read_data_csv(spark, data_path, is_show=True):
    """Read data from csv
    Args:
        spark: Spark session
        data_path: The path of data
        is_show: If true, the data would be shown
    Returns:
        data: Data read fom csv
    """
    data = spark.read.option("header", "true").option('encoding', 'utf-8').csv(data_path)
    data = data.select(col("userId").cast(IntegerType()), col("movieId").cast(IntegerType()),
                       col("rating").cast(FloatType()))
    if is_show:
        data.printSchema()
        data.show()

    return data


def split_data(data):
    """Split data into train set and test set
    Args:
        data
    Returns:
        train_data
        test_data
    """
    train_data, test_data = data.randomSplit([0.9, 0.1])
    return train_data, test_data


def train_als(data, input_user, input_video, input_rating):
    """Train a als model
    Args:
        data: Data used for training
        input_user: User column
        input_video: Video column
        input_rating: Rating column
    Returns:
        best_model: Trained als model
        model1: StringIndexer of user
        model2: StringIndexer of video
    """
    print(proc_date)
    # Define StringIndexer
    user_indexer = StringIndexer(inputCol=input_user, outputCol=input_user + "_index")
    model1 = user_indexer.fit(data)
    index1_data = model1.transform(data)
    video_indexer = StringIndexer(inputCol=input_video, outputCol=input_video + "_index")
    model2 = video_indexer.fit(index1_data)
    index2_data = model2.transform(index1_data)

    newdata = index2_data.select(col(input_user + "_index").cast(IntegerType()),
                                 col(input_video + "_index").cast(IntegerType()), input_rating)

    # Split data
    train_data, test_data = split_data(newdata)

    # ALS model
    als = ALS(userCol=input_user + "_index", itemCol=input_video + "_index",
              ratingCol=input_rating, coldStartStrategy="nan", implicitPrefs=False)

    # Crossvalidator
    paramGrid = ParamGridBuilder() \
        .addGrid(als.maxIter, [5, 10]) \
        .addGrid(als.regParam, [0.01, 0.1]) \
        .addGrid(als.rank, [10, 20]) \
        .build()

    evaluator = RegressionEvaluator(metricName="rmse", labelCol=input_rating,
                                    predictionCol="prediction")
    crossval = CrossValidator(estimator=als, estimatorParamMaps=paramGrid,
                              evaluator=evaluator,
                              numFolds=3)

    model = crossval.fit(train_data)
    best_model = model.bestModel
    # Compute rmse
    predictions = best_model.transform(test_data).na.drop()
    rmse = evaluator.evaluate(predictions)
    print("RMSE: ", rmse)
    print("MAXIter: ", best_model._java_obj.parent().getMaxIter())
    print("RegParam: ", best_model._java_obj.parent().getRegParam())
    print("Rank: ", best_model._java_obj.parent().getRank())

    return best_model, model1, model2


def recommend_users(spark, input_user, input_video, model, user_indexer, video_indexer, user_language, video_language, num_recommend=20, is_show=True):
    """Use als model to recommend for users
    Args:
        spark: Spark session
        input_user:
        input_video:
        model: ALS model
        user_indexer:
        video_indexer:
        num_recommend: The maximum number of recommendation videos
        is_show: If true, the data would be shown
        user_language: The language of user
        video_language: The language of video
    """
    # Recommend for all users
    userRecs = model.recommendForAllUsers(num_recommend)

    # Turn index back string
    indexer_user = IndexToString(inputCol=input_user + "_index", outputCol=input_user, labels=user_indexer.labels)
    index_user = indexer_user.transform(userRecs)

    video_labels = array(*[lit(x) for x in video_indexer.labels])
    recommendations = array(*[struct(
        video_labels[col("recommendations")[i][input_video + "_index"]].alias(input_video),
        col("recommendations")[i][input_rating]
    ) for i in range(num_recommend)])

    recs = index_user.withColumn("recommendations", recommendations).select(input_user, "recommendations")
    explode_recs = recs.select(input_user, explode("recommendations").alias("recommendation")).\
                        select(input_user, "recommendation.*").\
                        select(input_user, input_video, col("col2").alias("score"))

    # Keep user and video have same language
    user_label = read_data_hive(spark, [input_user, user_language], is_show)
    video_label = read_data_hive(spark, [input_video, video_language, is_show])
    explode_recs_filter = explode_recs.join(user_label, input_user, "inner").join(video_label, input_video, "inner")
    explode_recs_filter = explode_recs_filter.filter(explode_recs_filter[user_language] == explode_recs_filter[video_language])
    if is_show:
        explode_recs_filter.show(20)
    explode_recs_filter.registerTempTable("temp_table")
    # Save the result
    # spark.sql('INSERT OVERWRITE TABLE common_dw.dws_video_collaborative_filtering PARTITION(proc_date) \
    #         SELECT ' + input_user + ','+ input_video + ', score,' + proc_date +' AS proc_date FROM temp_table')


@timing
def main(is_csv=True):
    if is_csv:
        data = read_data_csv(spark, "../data/ratings.csv").cache()
    else:
        data = read_data_hive(spark, [input_user, input_video, input_rating], True)
    als_model, user_indexer, video_indexer = train_als(data, input_user, input_video, input_rating)
    recommend_users(spark, input_user, input_video, als_model, user_indexer, video_indexer, num_recommend=num_recommend)


if __name__ == '__main__':
    # Read argument
    parser = argparse.ArgumentParser(description='Receive some parameters')
    parser.add_argument('--show', dest="show", action='store_true', help='show the data')
    parser.add_argument('--proc_date', dest="proc_date", type=str)
    parser.add_argument('--num_recommend', dest='num_recommend', type=int, help='Number of recommendation')
    args = parser.parse_args()
    is_show = args.show
    num_recommend = args.num_recommend
    proc_date = args.proc_date
    csv = True
    input_user = "userId"
    input_video = "movieId"
    input_rating = "rating"
    user_language = "xx"
    video_language = "xxx"
    # Create a session
    spark = SparkSession.builder.appName("collaborative_filtering"). \
        config('encoding', 'UTF-8'). \
        getOrCreate()

    main(csv)
    spark.stop()
