# Submission Portal

This is a **flask** based app that was designed to allow curated data submissions from users to populate a **PostGres** database.

This is a replacement for an earlier process where data was taken from excel files received via email. 


##  Prerequisites

1. install docker
2. install docker-compose
3. install git
4. clone repository: `git clone --recursive https://github.com/gazymandias/flask-submission-portal.git`


##  Getting Started


> Run the database locally (ensure **Docker** is running first)

`docker compose up -d db`


> Run the Python app

`docker compose up --build flask-submission-portal`

> Check the routes are working appropriately on localhost

`localhost/`

> **Shutting down** - remove all volume data

`docker-compose down --volumes`