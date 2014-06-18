all: init test dev deploy

init:
	pip install -r requirements.txt
test:
	make init
	python tests.py
dev:
	make init
	python app.py
deploy:
	make init
	# does nothing currently, but install stuffs
	# it should prob hookup with cBednarski's deploy stuffs