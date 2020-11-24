up:
	bash bash/start_project.sh

down:
	bash bash/stop_project.sh

build:
	bash bash/build_project.sh

clean:
	bash bash/clean_image.sh

migrate:
	docker-compose exec django python manage.py migrate

mgs:
	docker-compose exec django python manage.py makemigrations

mgs-migrate: mgs migrate

attach-django:
	bash bash/attach_django.sh