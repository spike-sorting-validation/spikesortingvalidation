import numpy
import spikesortingvalidation

def test_match():
    from spikesortingvalidation.metrics import match
    spike_times  = numpy.arange(100)
    res = match.get_fp_fn_rate([spike_times + 1], spike_times, 2)
    assert res == [[0, 0]]


def test_best_match():
    from spikesortingvalidation.metrics import bestmatch
    target  = numpy.arange(10)
    spike_times = [[0, 2, 4, 6, 8], [1, 3, 5], [7, 9]]
    res = bestmatch.best_match(spike_times, target, 2)
    assert res[0] == [0, 1, 2]
    assert res[1] == [0, 0]
