

##############
# dump

from nbval.plugin import dumpers

# hmm, no special dumpers
#dumpers[...] = ...

##############
# load

from nbval.plugin import loaders

# hmm, no special loaders
#loaders[...] = ...

##############
# compare

from nbval.plugin import comparers

def arraylike_equal(test,ref):
    # np assert array equal (so e.g. nan==nan)
    import numpy
    numpy.testing.assert_array_equal(test,ref)

def hv_equal(test,ref):
    import numpy as np
    import holoviews as hv
    from holoviews.element.comparison import Comparison
    Comparison.register() # Can't quite remember why you need this but you do
    Comparison.assertEqual(test, ref)


import holoviews
import numpy
import pandas
comparers[pandas.DataFrame] = arraylike_equal
comparers[numpy.ndarray] = arraylike_equal
comparers[holoviews.core.element.Element] = hv_equal

