build:
	docker-compose build

up:
	docker-compose up

up-daemon:
	docker-compose up -d

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -it nz01 /bin/sh

shell-web:
	docker exec -it dz01 /bin/sh

shell-db:
	docker exec -it pz01 /bin/sh

log-nginx:
	docker-compose logs nginx

log-web:
	docker-compose logs web

log-db:
	docker-compose logs db

collectstatic:
	docker exec -it dz01 python manage.py collectstatic --noinput

adminuser:
	docker exec -it dz01 python manage.py createsuperuser
