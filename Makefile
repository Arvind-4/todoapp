.PHONY: all help test collect run


# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile


# target: test - calls the "test" django command
test:
	set -a
	source .env
	set -a 
	python manage.py test

# target: collect - calls the "collectstatic" django command
collect:
	python manage.py collectstatic --noinput

# target: run - calls the "runserver" django command
run:
	python manage.py runserver 8000 & pnpm watch
