P=python2.7 -m unittest discover
T=python2.7 -m unittest discover test -p
N=nosetests --with-progressive
all: main

transitori:
	python2.7 calcul-transitori.py

main:
	time python2.7 main.py

sim_special:
	python2.7 -m unittest test.test_sim.TestSimulation.test_small_two

sim_queue:
	$T 'test_sim_queue.py'

chart:
	$T 'test_chart.py'

sim:
	$T 'test_sim.py'

statistic:
	$T 'test_statistic.py'

model:
	$T 'test_model.py'

rand:
	$T 'test_rand.py'


suite:
	$T 'test_suite.py'

nose:
	python2.7 /usr/bin/nosetests

t: tests

tests:
	$P test
