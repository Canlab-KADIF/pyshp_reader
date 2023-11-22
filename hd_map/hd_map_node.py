import rospy

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point

import sys
sys.path.insert(0, '../lib/pyshp')

import shapefile
import numpy as np
import copy

pub = rospy.Publisher('hd_map', MarkerArray,queue_size=1)
map_parts = []
offset_hd_map = np.array([471632, 3965852])

def loadHDMap():
  global map_parts

  shp_file_base='A1_LANE'
  dat_dir='../data/shapefiles/'+shp_file_base +'/'
  sf = shapefile.Reader(dat_dir+shp_file_base)

  for id in range(len(sf.shapes())):
    shape_ex = sf.shape(id)
    points = []

    record = sf.records()

    for ip in range(len(shape_ex.points)):
        points.append(shape_ex.points[ip])

    map_parts.append(points)

def visualizeHDMap(event):
  global map_parts

  hd_map_marker = MarkerArray()

  hd_map_marker_part = Marker()

  hd_map_marker_part.header.frame_id = '/map'
  hd_map_marker_part.header.stamp = rospy.Time.now()
  hd_map_marker_part.type = Marker.LINE_STRIP
  hd_map_marker_part.action = Marker.ADD

  # POINTS Markers use x and y sacle for width/height respectively
  hd_map_marker_part.scale.x = 0.3
  hd_map_marker_part.scale.y = 0.3

  # Points are white
  hd_map_marker_part.color.r = 1.0
  hd_map_marker_part.color.g = 1.0
  hd_map_marker_part.color.b = 1.0
  hd_map_marker_part.color.a = 1.0

  hd_map_marker_part.lifetime = rospy.Duration()

  for part_id in range(len(map_parts)):
    hd_map_marker_part.id = part_id
    hd_map_marker_part.points = []

    for p_id in range(len(map_parts[part_id])):
      point = Point()

      point.x = map_parts[part_id][p_id][0]-offset_hd_map[0]
      point.y = map_parts[part_id][p_id][1]-offset_hd_map[1]
      point.z = 0

      hd_map_marker_part.points.append(point)

    if len(hd_map_marker_part.points) > 0:
      tmp_marker = copy.deepcopy(hd_map_marker_part)
      hd_map_marker.markers.append(tmp_marker)

  pub.publish(hd_map_marker)

if __name__ == '__main__':
    try:
      rospy.init_node('hd_map', anonymous=True)

      loadHDMap()

      timer = rospy.Timer(rospy.Duration(1), visualizeHDMap)

      rospy.spin()
      timer.shutdown()

    except rospy.ROSInterruptException:
        pass
