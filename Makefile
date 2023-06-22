build:
	docker compose -f dev.yml build

up:
	docker compose -f dev.yml up -d

down:
	docker compose -f dev.yml down && docker network prune --force