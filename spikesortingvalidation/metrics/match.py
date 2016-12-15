import numpy

def get_fp_fn_rate(spike_trains, target, jitter):
    '''Return the false positive and false negative rates for a given
    spike train target compared to a list of spike trains. All matches
    are established up to a certain jitter, expressedd in time steps.'''

    results = []

    assert numpy.iterable(spike_trains[0]), "spike_trains should be a list of spike trains"

    for spk in spike_trains:
        count = 0
        for spike in spk:
            idx = numpy.where(numpy.abs(target - spike) < jitter)[0]
            if len(idx) > 0:
                count += 1
        if len(spk) > 0:
            fp_rate = count/float(len(spk))

        count = 0
        for spike in target:
            idx = numpy.where(numpy.abs(spk - spike) < jitter)[0]
            if len(idx) > 0:
                count += 1
        if len(target) > 0:
            fn_rate  = count/(float(len(target)))
        
        results += [[1 - fp_rate, 1 - fn_rate]]

    return results