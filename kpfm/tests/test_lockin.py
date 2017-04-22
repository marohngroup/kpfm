# -*- coding: utf-8 -*-
from __future__ import division, absolute_import, print_function
from numpy.testing import assert_array_almost_equal
import numpy as np

from kpfm.lockin import LockIn


def test_lockin_even_fir():
    xb = np.array([-1, -np.sqrt(2)/2, 0, np.sqrt(2)/2,
                    1, np.sqrt(2)/2, 0, -np.sqrt(2)/2])
    repeats = 128
    N = xb.size * repeats
    x = np.tile(xb, repeats)
    t = np.arange(N)/16.0
    li = LockIn(t, x, fs=16.0)
    fir = np.ones(16)/16.0
    li.run(f0=2.0, fir=fir)
    li.manual_phase(0.0)
    assert_array_almost_equal(-np.ones_like(li("z"), dtype=np.complex128),
                              li("z"))


def test_lockin_odd_fir():
    xb = np.sin(2*np.pi/9 * np.arange(9))
    repeats = 96
    N = xb.size * repeats
    x = np.tile(xb, repeats)
    t = np.arange(N)/27.0
    li = LockIn(t, x, fs=27.0)
    fir = np.ones(27)/27.0
    li.run(f0=3.0, fir=fir)
    li.manual_phase(0.0)
    assert_array_almost_equal(-1j*np.ones_like(li("z"), dtype=np.complex128),
                              li("z"))