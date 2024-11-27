.PHONY: db
db:
	docker compose up -d postgres

.PHONY: adminer
adminer:
	docker compose up -d adminer

.PHONY: build
build:
	docker compose up -d --build

.PHONY: logs
logs:
	docker compose logs

.PHONY: up
down:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: run
run:
	uvicorn freeline.main:app --reload --port 8000 --host 0.0.0.0
