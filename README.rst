PRODUCT REVIEW SEARCH
=====================

This project is about information retrieval system ,When a user can come and search their keywords
and based on that the review text with the highest review score and helpfulness should appear.

:License: Apache Software License 2.0


Features
---------

* Management command to load and index the complete dataset to database model
* UI for client for search the data and get the result
* Docker support using docker-compose_ for development and production



Setup
---------

* Note: move your foods.txt file in .data/ directory for loading the review data in db before using docker compose
* for using with docker-compose :  docker-compose -f local.yml build , docker-compose -f local.yml up
* for loading the foods.txt data in database need to run this management command :
        docker-compose -f local.yml run django python manage.py load_review_data

    when not using docker you can pass the file path and chunk_size(bulk_creation of records at a time)
       python manage.py load_review_data <file_path> <chunk_size>


Live Application : http://ec2-13-232-206-76.ap-south-1.compute.amazonaws.com/

