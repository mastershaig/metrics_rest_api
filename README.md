### Task description
Sample dataset: https://gist.github.com/kotik/3baa5f53997cce85cc0336cb1256ba8b/

Expose the sample dataset through a single generic HTTP API endpoint, which is capable of filtering, grouping and sorting.<br/>
Dataset represents performance metrics (impressions, clicks, installs, spend, revenue) for a given date, advertising channel, country and operating system.<br/>
Dataset is expected to be stored and processed in a relational database.

Client of this API should be able to:
1) filter by time range (date_from+date_to is enough), channels, countries, operating systems
2) group by one or more columns: date, channel, country, operating system
3) sort by any column in ascending or descending order
4) see derived metric CPI (cost per install) which is calculated as cpi = spend / installs

Common API use-cases:
1) Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order. Hint:
```
=> select channel, country, sum(impressions) as impressions, sum(clicks) as clicks from sampledataset where date < '2017-06-01' group by channel, country order by clicks desc;
     channel      | country | impressions | clicks
------------------+---------+-------------+--------
 adcolony         | US      |      532608 |  13089
 apple_search_ads | US      |      369993 |  11457
 vungle           | GB      |      266470 |   9430
 vungle           | US      |      266976 |   7937
 ...
```
2) Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
3) Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
4) Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order. Please think carefully which is an appropriate aggregate function for CPI.

API endpoint is supposed to serve a dynamic dataset that corresponds to any combination of filters, breakdowns and sorting. Four use-cases are provided to give the general idea of its usage and capabilities. Please don't expect use-case number as an API parameter. Please don't create four API endpoints.

Make sure you have a single API endpoint that is compliant with all use-cases described above and **explicitly specify localhost urls for each of the 4 cases in your Readme**.
### Prerequisite
- Python version 3.9

### How to setup and run
- run ```pip install -r requirements.txt```
- run ``` python manage.py migrate ```
- to load data run ```python manage.py csv_to_model```
- run ```python manage.py runserver```

Common API use-cases:

1. Show the number of impressions and clicks that occurred before the 1st of June 2017, broken down by channel and country, sorted by clicks in descending order.
URL: http://localhost:8000/api/v1/metrics?group_by=channel,country&ordering=-clicks&date_to=2017-06-01
2. Show the number of installs that occurred in May of 2017 on iOS, broken down by date, sorted by date in ascending order.
URL: http://localhost:8000/api/v1/metrics?group_by=date&date_to=2017-05-31&os=ios&ordering=date
3. Show revenue, earned on June 1, 2017 in US, broken down by operating system and sorted by revenue in descending order.
URL: http://localhost:8000/api/v1/metrics?group_by=os&ordering=-revenue&country=US&date=2017-06-01
4. Show CPI and spend for Canada (CA) broken down by channel ordered by CPI in descending order.
URL: http://localhost:8000/api/v1/metrics?group_by=channel&cpi=true&ordering=-cpi&country=CA
