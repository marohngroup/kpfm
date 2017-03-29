# -*- coding: utf-8 -*-
"""
========
utility
========

This module contains useful utility functions, decorators, and plotting helpers
that are useful throughout the ``kpfm`` package.

**Should my function go here?**
If you find yourself wanting it in many IPython notebooks, yes!
Just add a docstring and make sure the function is useful on its own
(not dependent on any external data, doesn't make assumptions that limit
broader usefulness of the code).
"""

from __future__ import division, print_function, absolute_import
import six
import h5py
import scipy
from distutils.version import LooseVersion
from decorator import decorator


if LooseVersion(scipy.__version__) > LooseVersion("0.18"):
    from scipy import fftpack
    next_fast_len = fftpack.next_fast_len
else:
    from scipy.signal import signaltools
    next_fast_len = signaltools._next_regular


@decorator
def h5filename(f, fname_or_fh, *args, **kwargs):
    """Decorator to allow seamless use of filenames rather than
    file handles for functions that operate on an HDF5 file.

    Usage
    ----- 
    To use this decorator, write the function to take an HDF5 file handle as
    the function's first argument.

    Example: We create a simple function and HDF5 file.

    >>> @h5filename
    >>> def h5print(fh):
    >>>     print(fh.values())
    >>>
    >>> fh = h5py.File('test.h5')
    >>> fh['x'] = 2

    We can call the function on the file handle

    >>> h5print(fh)
    [<HDF5 dataset "x": shape (), type "<i8">]
    
    or and call the function on the filename

    >>> fh.close()
    >>> h5print('test.h5')
    [<HDF5 dataset "x": shape (), type "<i8">]

    

    """
    if isinstance(fname_or_fh, six.string_types):
        with h5py.File(fname_or_fh, 'r') as fh:
            return f(fh, *args, **kwargs)
    else:
        return f(fname_or_fh, *args, **kwargs)