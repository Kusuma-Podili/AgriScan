.PHONY: help install run test lint docker-build docker-run clean

PYTHON ?= python
PIP ?= pip
PORT ?= 8000

help:
	@echo "AgriScan Precision Agriculture Platform"
	@echo "Available commands:"
	@echo "  make install      - Install Python dependencies"
	@echo "  make run          - Start platform locally"
	@echo "  make test         - Execute backend test suite"
	@echo "  make lint         - Run Flake8 static analysis"
	@echo "  make docker-build - Build Docker container"
	@echo "  make docker-run   - Run container on port $(PORT)"

install:
	$(PIP) install --upgrade pip
	$(PIP) install -r backend/requirements.txt
	$(PIP) install pytest pytest-cov flake8

run:
	$(PYTHON) main.py

test:
	cd backend && pytest -v --cov=app tests/

lint:
	flake8 backend/app --count --select=E9,F63,F7,F82 --show-source --statistics

docker-build:
	docker build -t agriscan:latest .

docker-run:
	docker run -p $(PORT):8000 agriscan:latest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
