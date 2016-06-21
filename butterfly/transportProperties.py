"BlockMeshDict class."
from foamfile import FoamFile
from collections import OrderedDict


class TransportProperties(FoamFile):
    """Transport Properties class."""

    # set default valus for this class
    __defaultValues = OrderedDict()
    __defaultValues['nu'] = 'nu [0 2 -1 0 0 0 0] 1e-05'
    __defaultValues['beta'] = 'beta [0 0 0 -1 0 0 0] 3e-03'
    __defaultValues['TRef'] = 'TRef [0 0 0 1 0 0 0] 300'
    __defaultValues['Pr'] = 'TRef [0 0 0 1 0 0 0] 300'
    __defaultValues['Prt'] = 'Prt [0 0 0 0 0 0 0] 0.7'
    __defaultValues['Cp0'] = '1000'

    def __init__(self, values=None):
        """Init class."""
        FoamFile.__init__(self, name='transportProperties', cls='dictionary',
                          location='constant', defaultValues=self.__defaultValues,
                          values=values)

# fv = TransportProperties()
# fv.save(r'C:\Users\Administrator\butterfly\innerflow_3')