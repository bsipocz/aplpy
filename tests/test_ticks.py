import matplotlib
matplotlib.use('Agg')

import numpy as np
import pytest

import aplpy


def test_ticks_spacing():
    data = np.zeros((16, 16))
    f = aplpy.FITSFigure(data)
    f.ticks.set_xspacing(0.01)
    f.ticks.set_xspacing(0.1)
    f.ticks.set_yspacing(0.01)
    f.ticks.set_yspacing(0.1)
    f.close()


def test_ticks_length():
    data = np.zeros((16, 16))
    f = aplpy.FITSFigure(data)
    f.ticks.set_length(0)
    f.ticks.set_length(1)
    f.ticks.set_length(10)
    f.close()


def test_ticks_color():
    data = np.zeros((16, 16))
    f = aplpy.FITSFigure(data)
    f.ticks.set_color('black')
    f.ticks.set_color('#003344')
    f.ticks.set_color((1.0, 0.4, 0.3))
    f.close()


def test_ticks_linewidth():
    data = np.zeros((16, 16))
    f = aplpy.FITSFigure(data)
    f.ticks.set_linewidth(1)
    f.ticks.set_linewidth(3)
    f.ticks.set_linewidth(10)
    f.close()


def test_ticks_minor_frequency():
    data = np.zeros((16, 16))
    f = aplpy.FITSFigure(data)
    f.ticks.set_minor_frequency(1)
    f.ticks.set_minor_frequency(5)
    f.ticks.set_minor_frequency(10)
    f.close()
