py2: example.h example.i
	swig -c++ -python -modern example.i
	g++ -fpic -c example_wrap.cxx -I/usr/include/python2.7
	g++ -shared example_wrap.o -o _example.so

.PHONY: test clean

test:
	python2 test.py


clean:
	rm -f example.py example_wrap.cxx example_wrap.o _example.so example.pyc
