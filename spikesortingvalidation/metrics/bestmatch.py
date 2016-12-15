import numpy
from spikesortingvalidation.metrics import match

def best_match(spike_trains, target, jitter):
    '''Return the best combination of spike trains that will reduce
    as much as possible the total error while reconstructing the target
    spike train, the error being defined as the mean between false 
    positive and false negatives. 

    The function returns a list of the selected units, and the corresponding
    errors [false postive, false negative]'''

    results = []

    assert numpy.iterable(spike_trains[0]), "spike_trains should be a list of spike trains"


    selection  = []
    error      = [1, 1]
    find_next  = True
    sel_spikes = []

    while (find_next == True):

        to_explore   = numpy.setdiff1d(numpy.arange(len(spike_trains)), numpy.unique(selection))
            
        if len(to_explore) > 0:

            new_spike_trains = []
            for idx in to_explore:
                new_spike_trains += [list(spike_trains[idx]) + sel_spikes]

            local_errors = match.get_fp_fn_rate(new_spike_trains, target, jitter)
            errors       = numpy.mean(local_errors, 1)

            if numpy.min(errors) <= numpy.mean(error):
                idx         = numpy.argmin(errors)
                selection  += [to_explore[idx]]
                error       = local_errors[idx]
                sel_spikes  = new_spike_trains[idx]
            else:
                find_next = False
        else:
            find_next = False

    return selection, error
