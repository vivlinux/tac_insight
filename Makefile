.PHONY: install run lint test clean

# Install all dependencies
install:
	pip install -r requirements.txt

# Run the main application
run:
	python main.py ${OPENAI_API_KEY:+--openai_key=$(OPENAI_API_KEY)}

# Lint the code using flake8
lint:
	flake8 .

# Run tests using pytest
test:
	pytest tests/test_*.py

# Clean up any generated files
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete