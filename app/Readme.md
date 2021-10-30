# Execute shell commands in docker container

docker-compose up -d --build
docker-compose exec web python manage.py migrate --noinput
docker-compose exec web python manage.py flush --no-input
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py shell

# Built from guide at :

# https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/

# REST API : https://medium.com/swlh/build-your-first-rest-api-with-django-rest-framework-e394e39a482c
