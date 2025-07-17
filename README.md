# market_data_analysis
Assessment to analyze data (e.g., technology, agriculture, etc.), generate a markdown report using Gemini AI, and provide a secure API endpoint to get it.
created virtual environment and installed libraries(included requirements.txt)
Technologies used:
    1. Framework-Django
    2.Authentication- JWT tokens
    3.AI Analysis- Google gemini API
    4.Django rate-limit
    5.Input validation - Djagorestframework API
created project- 'analyze_market_data' and app named 'analysis_app'
created username and password using python manage.py createsuperuser.
In the project's urls.py , added 3 URLs to:
    1. to get tokens by giving username and password
    2. to obtain access token if access token has expired(access expires in token is short time)
    3. to get the analysis of sector provided(use access toke for Authentication).
Increased the time limit of tokens in settings.py as default expiry time  is 5 min.
Used Google Gemini API for AI analysis
Tested the API's using Postman

