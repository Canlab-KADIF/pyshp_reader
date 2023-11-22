import numpy as np
import math
from config import Config

from lib.pyshp import shapefile

class Point(object):
  def __init__(self, x, y):
    self._x = x
    self._y = y

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, x):
    self._x = x

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, y):
    self._y = y

  def distance_to(self, other):
    return math.hypot(self._x - other.x, self._y - other.y)

  def __repr__(self):
    return 'Point [%s, %s]' % (self._x, self._y)

class LineSegment(object):
  def __init__(self, name, seg_points):
    self._seg_name   = name
    self._seg_points = seg_points
    self._line_start = seg_points[0]
    self._line_end   = seg_points[-1]

  @property
  def seg_name(self):
      return self._seg_name

  @seg_name.setter
  def seg_name(self, seg_name):
      self._seg_name = seg_name

  @property
  def seg_points(self):
      return self._seg_points

  @seg_points.setter
  def seg_points(self, seg_points):
      self._seg_points = seg_points

  @property
  def line_start(self):
    return self._line_start

  @property
  def line_end(self):
      return self._line_end

class HDMap(object):
  def __init__(self):
    self._line_segments = []
    self._offset_hd_map = Config.OFFSET_HD_MAP

  @property
  def line_segments(self):
    return self._line_segments

  def load_hd_map(self, data_path = Config.EDGE_SHAPE_FILE_NAME):
    """
    See https://pypi.python.org/pypi/pyshp
    for a detailed explanation of the this library
    """
    shp_file_base = Config.EDGE_SHAPE_FILE_NAME
    dat_dir = Config.SHAPE_FILE_PATH + shp_file_base +'/'
    sf = shapefile.Reader(dat_dir+shp_file_base)
    record_link = sf.records()

    for id in range(len(sf.shapes())):
      shape_ex = sf.shape(id)

      if record_link[id][13] != '':
        self._line_segments.append(LineSegment(record_link[id][13],[Point((points-self._offset_hd_map)[0], (points-self._offset_hd_map)[1]) for points in shape_ex.points]))

if __name__ =='__main__':
  a = HDMap()
  a.load_hd_map()

  print(a.line_segments[0].line_start.x, a.line_segments[0].line_start.y)