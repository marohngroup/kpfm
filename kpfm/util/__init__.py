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
import io
import six
import h5py
import scipy
from distutils.version import LooseVersion
from decorator import decorator

# Fix errors on readthedocs by defining a dummy version of
# next_fast_len if scipy is "mocked" (see docs/conf.py)
try:
    if LooseVersion(scipy.__version__) > LooseVersion("0.18"):
        from scipy import fftpack
        next_fast_len = fftpack.next_fast_len
    else:
        from scipy.signal import signaltools
        next_fast_len = signaltools._next_regular
except TypeError:
    def next_fast_len(x):
        return x



def align_labels(axes_list,lim, axis='y'):
    for ax in axes_list:
        t = ax.yaxis.label.get_transform()
        x,y = ax.yaxis.label.get_position()
        if axis == 'y':
            ax.yaxis.set_label_coords(lim,y,t)
        else:
            ax.xaxis.set_label_coords(x, lim, t)

@decorator
def txt_filename(f, fname_or_fh, *args, **kwargs):
    if isinstance(fname_or_fh, six.string_types):
        with io.open(fname_or_fh, 'r') as fh:
            return f(fh, *args, **kwargs)
    else:
        return f(fname_or_fh, *args, **kwargs)

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


from kpfm.util.readtxt import kpfm_data