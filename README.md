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
