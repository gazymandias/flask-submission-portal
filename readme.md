>  run db locally
docker compose up -d db
>  run python app
docker compose up --build flask-submission-portal
> check
localhost/
>  remove all volume data
docker-compose down --volumes