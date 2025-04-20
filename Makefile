up:
	docker-compose up --build

down:
	docker-compose down -v

logs:
	docker-compose logs -f

migrate:
	python3 app/models.py