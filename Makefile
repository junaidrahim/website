update-theme:
	git submodule update --init --recursive
	git submodule update --recursive --remote

server:
	hugo server

build:
	hugo

	
	
