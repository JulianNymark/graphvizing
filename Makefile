all:
	python3.5 test.py
	feh img/g1.png

i:
	python3.5 -i test.py

clean:
	$(RM) -r img __pycache__
