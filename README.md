# Google Trends 

### Installation

```pip install pytrends```

```
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
```

```
kw_list = ["Blockchain"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
```

### API Methods

- Interest Over Time: returns historical, indexed data for when the keyword was searched most as shown on Google Trends' Interest Over Time section.

- Historical Hourly Interest: returns historical, indexed, hourly data for when the keyword was searched most as shown on Google Trends' Interest Over Time section. It sends multiple requests to Google, each retrieving one week of hourly data. It seems like this would be the only way to get historical, hourly data.

- Interest by Region: returns data for where the keyword is most searched as shown on Google Trends' Interest by Region section.

- Related Topics: returns data for the related keywords to a provided keyword shown on Google Trends' Related Topics section.

- Related Queries: returns data for the related keywords to a provided keyword shown on Google Trends' Related Queries section.

- Trending Searches: returns data for latest trending searches shown on Google Trends' Trending Searches section.

- Top Charts: returns the data for a given topic shown in Google Trends' Top Charts section.

- Suggestions: returns a list of additional suggested keywords that can be used to refine a trend search.

### Common API Parameters

- kw_list : Up to five terms in a list: ['Pizza', 'Italian', 'Spaghetti', 'Breadsticks', 'Sausage']
- cat : Defaults to no category. [Category List](https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories)
- geo : For example United States is 'US', Alabama would be 'US-AL'
- tz : Timezone Offset(in minutes)
- timeframe : Defaults last 5 years, ``` 'today 5-y' ```
  - Specific dates, 'YYYY-MM-DD YYYY-MM-DD' example '2016-12-14 2017-01-25'
  - By Month: ``` 'today #-m' ``` where # is the number of months. Seems to only work for 1,2,3 months only
  - Daily: ``` 'now #-d' ``` where # is the number of days. Seems to only work for 1,7 days only
  - Hourly: ``` 'now #-H' ``` where # is the number of hours. Seems to only work for 1,4 hours only
- gprop : What Google property to filter to. Example 'images'

- Interest Over Time

 ``` pytrends.interest_over_time() ```
 
 - Interest by Region
 
  ``` pytrends.interest_by_region(resolution='COUNTRY', inc_low_vol=True, inc_geo_code=False) ```
  - resolution :
    - CITY returns city level data
    - COUNTRY returns country level data
    - DMA returns dma metro level data
    - REGION returns region level data
   - inc_low_vol : True/False (includes google trends data for low volume countries/regions as well)
   - inc_geo_code : True/False (includes ISO codes of countries along with the names in the data)

- Related Topics : ``` pytrends.related_topics() ```
- Related Queries : ``` pytrends.related_queries() ```
- Trending Searches : ``` pytrends.trending_searches(pn='united_states') ```
- Suggestions : ```pytrends.suggestions(keyword)```
