from pytrends.request import TrendReq
import pandas as pd
import numpy as np
import json
from datetime import datetime

pytrends = TrendReq(hl='tr-TR', tz=360, timeout=(10, 25))


def set_new_query(kwords, timeframe): # determines the query for searching
    pytrends.build_payload(kwords, cat=0, timeframe=timeframe, geo='TR', gprop='')
    return kwords


def get_interest_over_time(): # returns time-dependent search results
    df_ = pytrends.interest_over_time()
    df_.drop(['isPartial'], axis='columns', inplace=True)
    df_.reset_index(inplace=True)
    df_.date = pd.to_datetime(df_.date, format='%Y-%m-%d')
    df_.rename(columns={'date': 'Date'}, inplace=True)
    return df_


def get_interest_by_region(): # returns region-dependent search results
    df_ = pytrends.interest_by_region(resolution='COUNTRY')
    df_ = df_.loc[~(df_ == 0).all(axis=1)]
    df_.reset_index(inplace=True)
    df_.rename(columns={'geoName': 'Region'}, inplace=True)
    return df_


def get_related_queries(): # get related query about keywords
    return pytrends.related_queries()


def get_related_topics(): #get related topics about keywords
    return pytrends.related_topics()


def table_related_queries(kwords, queries, n=10): # convert table related queries result
    for each in kwords:
        df_rq_top = pd.DataFrame(queries[each]['top'])
        df_rq_rising = pd.DataFrame(queries[each]['rising'])
        df_rq = pd.concat([df_rq_top, df_rq_rising], axis=1, keys=(["Top", "Rising"])).reset_index(drop=True)
        df_rq.index = np.arange(1, len(df_rq) + 1)
        print(each + " related queries")
    return df_rq.head(n)


def table_related_topics(kw):# convert table related topic result
    related_topic = pytrends.related_topics()
    related_topic = related_topic[kw[0]]['rising'].drop(['link', 'topic_mid'], axis=1)
    return related_topic


def df_to_json_datetime(df_): #df to json include datetime column
    json_file = df_.to_json(orient="records", date_format='iso', date_unit='s')
    parsed = json.loads(json_file)
    for i in parsed:
        i["Date"] = datetime.fromisoformat(i["Date"][:-1])
    return parsed

def df_to_json(df_): #df to json exclude datetime column
    json_file = df_.to_json(orient="records", date_format='iso', date_unit='s')
    parsed = json.loads(json_file)
    return parsed

kw_list = set_new_query(["Apranax"], "today 12-m")

df = get_interest_over_time()
search_json = df_to_json_datetime(df)


df_by_region = get_interest_by_region()
region_json = df_to_json(df_by_region)


df_related_queries = table_related_queries(kw_list, get_related_queries())
related_query_json = df_to_json(df_related_queries)

df_related_topics = table_related_topics(kw_list)
related_topic_json = df_to_json(df_related_topics)

