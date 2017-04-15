all: img/g.png
	feh $<

gen_graph.py: Makefile makefiletographviz.py
	./makefiletographviz.py < Makefile > $@

img/g.png: gen_graph.py
	python3.5 $<

clean:
	$(RM) -r img __pycache__ gen_*
