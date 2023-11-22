import rospkg
import copy

import sys
sys.path.insert(0, '../lib/pyshp')

import shapefile
import numpy as np

map_parts = []
offset_hd_map = np.array([471632, 3965852])

def loadHDMap():
  global map_parts

  shp_file_base='C1_NODE'
  dat_dir=rospkg.RosPack().get_path('navigation') + '/src/data/shapefiles/'+shp_file_base +'/'
  sf = shapefile.Reader(dat_dir+shp_file_base)

  tmp_id = range(1,439)

  for id in range(len(sf.shapes())):
    shape_ex = sf.shape(id)
    points = []

    record = sf.records()

    for ip in range(len(shape_ex.points)):
      points.append(shape_ex.points[ip])

    map_parts.append(points)

  print('rest node : ', tmp_id)

def get_points():
  global map_parts

  points = []

  for part_id in range(len(map_parts)):
    part_points = []

    for p_id in range(len(map_parts[part_id])):
      point_x = map_parts[part_id][p_id][0]-offset_hd_map[0]
      point_y = map_parts[part_id][p_id][1]-offset_hd_map[1]

      part_points.append([point_x,point_y])

    if len(part_points) > 0:
      tmp_points = copy.deepcopy(part_points)
      points.append(tmp_points)

  return points

if __name__ == '__main__':
  loadHDMap()  
  points = get_points() 

  # print(points)
