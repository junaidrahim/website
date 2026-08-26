update-theme:
	git submodule update --init --recursive
	git submodule update --recursive --remote

server:
	hugo server

build:
	hugo

lint:
	npx prettier content --write

notebook-status:
	uv run --frozen python main.py status

notebook-doctor:
	uv run --frozen python main.py doctor

notebook-test:
	uv run --frozen python -m unittest main.NotebookCliTest
