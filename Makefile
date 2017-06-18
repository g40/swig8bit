py2:
	swig -c++ -python -modern example.i
	g++ -fpic -c example_wrap.cxx -I/usr/include/python2.7
	g++ -shared example_wrap.o -o _example.so

py3:
	swig -c++ -python -modern -py3 example.i
	g++ -fpic -c example_wrap.cxx -I/usr/include/python3.5
	g++ -shared example_wrap.o -o _example.so

.PHONY: test2 test3 clean

test2:
	python2 test.py

test3:
	python3 test.py

clean:
	rm -f example.py example_wrap.cxx example_wrap.o _example.so example.pyc
