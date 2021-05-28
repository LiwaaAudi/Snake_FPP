.PHONY: help
.PHONY: venv
venv:
	: # Create venv (One time only)
	: test -d venv || virtualenv -p --nostite-packages venv;
	test -d venv || python3 -m venv venv;
	@echo "To activate the virtual environment run following command:"
	@echo "source venv/bin/activate"

.PHONY: dependencies
dependencies:
	# Install dependencies
	python3 -m pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: migrations
migrations:
	# Makemigrations
	python manage.py makemigrations

.PHONY: migrate
migrate:
	# Migrate
	python manage.py migrate

.PHONY: user
user:
	# Create Super User
	python manage.py createsuperuser

.PHONY: server
server:
	# Start server on 8000
	python manage.py runserver
.PHONY: play
play:
	# launch the game
	python snake.py
