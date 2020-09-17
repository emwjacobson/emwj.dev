
up:
	docker-compose -p portfolio -f docker-compose-prod.yml up --build

up-dev:
	docker-compose -p portfolio -f docker-compose-dev.yml up --build

down:
	docker-compose -p portfolio down --rmi all -v
