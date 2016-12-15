import numpy
import spikesortingvalidation

def test_match():
	from spikesortingvalidation.metrics import match
	spike_times  = numpy.arange(100)
	res = match.get_fp_fn_rate([spike_times + 1], spike_times, 2)
	assert res == [[0, 0]]