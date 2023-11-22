import rospkg
import numpy as np
import sys
sys.path.insert(0, '../lib/')

class Config():
  # This value get by averaging all points
  OFFSET_HD_MAP = np.array([471632, 3965852])
  NODE_SHAPE_FILE_NAME = 'C1_NODE'
  EDGE_SHAPE_FILE_NAME = 'A3_LINK'
  SHAPE_FILE_PATH = rospkg.RosPack().get_path('navigation') + '/src/data/shapefiles/'

  # ROS topic name
  GPS_TOPIC = '/gps_pose'
  EKF_TOPIC = '/ekf_pose'
  FUSED_POSE_TOPIC = '/fix_vehicle'

  # ROS service name
  REQ_HOTSTART_SERVICE_NAME = '/req_reset_gps'

  # Load configuration
  MIN_LOAD_WIDTH = 2.75
  MAX_LOAD_WIDTH = 3.5
