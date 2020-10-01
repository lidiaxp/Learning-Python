from createMatrizColina import createClareira

start = "<?xml version=\"1.0\" ?>\n\
<?xml-model href=\"http://sdformat.org/schemas/root.xsd\" schematypens=\"http://www.w3.org/2001/XMLSchema\"?>\n\
<sdf version=\"1.5\">\n\
  <world name=\"default\">\n"

pluginAttach = "<plugin name=\"mrs_gazebo_static_transform_republisher_plugin\" filename=\"libMRSGazeboStaticTransformRepublisher.so\"/>\n"

coordenadasSistema = "<spherical_coordinates> \n\
      <surface_model>EARTH_WGS84</surface_model>\n\
      <latitude_deg>37.411802</latitude_deg>\n\
      <longitude_deg>-121.995739</longitude_deg>\n\
      <elevation>0.0</elevation>\n\
      <heading_deg>0</heading_deg>\n\
    </spherical_coordinates>\n"

physicsEngine = "<physics name=\"default_physics\" default=\"0\" type=\"ode\">\n\
      <gravity>0 0 -9.8066</gravity>\n\
      <ode>\n\
        <solver>\n\
          <type>quick</type>\n\
          <iters>10</iters>\n\
          <sor>1.3</sor>\n\
          <use_dynamic_moi_rescaling>0</use_dynamic_moi_rescaling>\n\
        </solver>\n\
        <constraints>z\n\
          <cfm>0</cfm>\n\
          <erp>0.2</erp>\n\
          <contact_max_correcting_vel>1000</contact_max_correcting_vel>\n\
          <contact_surface_layer>0.001</contact_surface_layer>\n\
        </constraints>\n\
      </ode>\n\
      <max_step_size>0.004</max_step_size>\n\
      <real_time_factor>1</real_time_factor>\n\
      <real_time_update_rate>250</real_time_update_rate>\n\
      <magnetic_field>6.0e-06 2.3e-05 -4.2e-05</magnetic_field>\n\
    </physics>\n"

shadown = "<scene>\n\
      <shadows>false</shadows>\n\
      <sky>\n\
        <clouds/>\n\
      </sky>\n\
    </scene>\n"

sol = "<light type=\"directional\" name=\"sun\">\n\
      <cast_shadows>true</cast_shadows>\n\
      <pose>250 250 600 0 0 0</pose>\n\
      <diffuse>0.8 0.8 0.8 1</diffuse>\n\
      <specular>0.2 0.2 0.2 1</specular>\n\
      <attenuation>\n\
        <range>1000</range>\n\
        <constant>0.9</constant>\n\
        <linear>0.01</linear>\n\
        <quadratic>0.001</quadratic>\n\
      </attenuation>\n\
      <direction>0 0 -1</direction>\n\
    </light>\n"

groundPlane = "<model name=\"ground_plane\">\n\
      <static>true</static>\n\
      <link name=\"link\">\n\
        <collision name=\"collision\">\n\
          <pose>0 0 0 0 0 0</pose>\n\
          <geometry>\n\
            <plane>\n\
              <normal>0 0 1</normal>\n\
              <size>250 250</size>\n\
            </plane>\n\
          </geometry>\n\
          <surface>\n\
            <friction>\n\
              <ode>\n\
                <mu>1</mu>\n\
                <mu2>1</mu2>\n\
              </ode>\n\
            </friction>\n\
          </surface>\n\
        </collision>\n\
        <visual name=\"grass\">\n\
          <pose>0 0 0 0 0 0</pose>\n\
          <cast_shadows>false</cast_shadows>\n\
          <geometry>\n\
            <mesh>\n\
              <uri>file://grass_plane/meshes/grass_plane.dae</uri>\n\
            </mesh>\n\
          </geometry>\n\
        </visual>\n\
      </link>\n\
    </model>\n"

def createTree(n, x, y):
    tree = "<model name='tree_simple" + str(n) + "'>\n\
        <static>1</static>\n\
      <link name='link'>\n\
        <pose frame=''>0 0 0.1 0 -0 0</pose>\n\
        <collision name='collision_trunk'>\n\
          <pose frame=''>0 0 2 0 -0 0</pose>\n\
          <geometry>\n\
            <cylinder>\n\
              <radius>0.25</radius>\n\
              <length>4</length>\n\
            </cylinder>\n\
          </geometry>\n\
        </collision>\n\
        <collision name='collision_treetop'>\n\
          <pose frame=''>0 0 5.2 0 -0 0</pose>\n\
          <geometry>\n\
            <sphere>\n\
              <radius>1.5</radius>\n\
            </sphere>\n\
          </geometry>\n\
        </collision>\n\
        <visual name='trunk'>\n\
          <pose frame=''>0 0 2 0 -0 0</pose>\n\
          <geometry>\n\
            <cylinder>\n\
              <radius>0.25</radius>\n\
              <length>4</length>\n\
            </cylinder>\n\
          </geometry>\n\
          <material>\n\
            <script>\n\
              <uri>model://tree_simple/scripts</uri>\n\
              <uri>model://tree_simple/materials/textures</uri>\n\
              <name>TreeSimple/Trunk</name>\n\
            </script>\n\
          </material>\n\
        </visual>\n\
        <visual name='treetop'>\n\
          <pose frame=''>0 0 5.2 0 -0 0</pose>\n\
          <geometry>\n\
            <sphere>\n\
              <radius>1.5</radius>\n\
            </sphere>\n\
          </geometry>\n\
          <material>\n\
            <script>\n\
              <uri>model://tree_simple/scripts</uri>\n\
              <uri>model://tree_simple/materials/textures</uri>\n\
              <name>TreeSimple/Treetop</name>\n\
            </script>\n\
          </material>\n\
        </visual>\n\
        <self_collide>0</self_collide>\n\
        <kinematic>0</kinematic>\n\
      </link>\n\
      <pose frame=''>" + str(x) + " " + str(y) + " 0 0 -0 0</pose>\n\
    </model>\n"
    return tree


cameraSpawnObjects = "<model name='the_void'>\n\
      <static>1</static>\n\
      <link name='link'>\n\
        <pose frame=''>0 0 0.1 0 -0 0</pose>\n\
        <visual name='the_void'>\n\
          <pose frame=''>0 0 2 0 -0 0</pose>\n\
          <geometry>\n\
            <sphere>\n\
              <radius>0.25</radius>\n\
            </sphere>\n\
          </geometry>\n\
          <material>\n\
            <script>\n\
              <uri>file://media/materials/scripts/Gazebo.material</uri>\n\
              <name>Gazebo/Black</name>\n\
            </script>\n\
          </material>\n\
        </visual>\n\
        <self_collide>0</self_collide>\n\
        <enable_wind>0</enable_wind>\n\
        <kinematic>0</kinematic>\n\
      </link>\n\
      <pose frame=''>-1000 -1000 0 0 0 0</pose>\n\
    </model>\n"

userCamera = "<gui>\n\
      <camera name=\"camera\">\n\
        <pose>-60 -100 30 0 0.4 0.89</pose>\n\
      </camera>\n\
    </gui>\n"

gripperPlugin = "<plugin name=\"ros_link_attacher_plugin\" filename=\"libgazebo_ros_link_attacher.so\"/>\n"

guiFrameSinc = "<plugin name=\"mrs_gazebo_rviz_cam_synchronizer\" filename=\"libMRSGazeboRvizCameraSynchronizer.so\" >\n\
      <target_frame_id>gazebo_user_camera</target_frame_id>\n\
      <world_origin_frame_id>uav1/gps_origin</world_origin_frame_id>\n\
      <frame_to_follow>uav1::base_link</frame_to_follow>\n\
    </plugin>\n"

end = "</world>\n\
</sdf>\n"

def comment(string):
    return str(string) + "\n"

import numpy as np
import random
import matplotlib.pyplot as plt

size1, size2 = 55, 55
alfa = 0.5
beta = 0.82
matriz = np.ones((size1, size2))
for i in range(size1):
    for j in range(size2):
        if random.random() < beta: matriz[i][j] = 0
# matriz[i][j] = [[0 for i in range(size1)] for j in range(size2) if random.random() < beta]
matriz = createClareira(10, 10, 10, matriz, alfa)
matriz = createClareira(30, 40, 15, matriz, alfa)
# matriz = createClareira(80, 40, 25, matriz, alfa)
camX, camY = [], []
for i in range(size1):
    for j in range(size2):
        if matriz[i][j] == 1:
            camX.append(i)
            camY.append(j)

f = open("teste.world", "w")
f.write(start)
f.write(pluginAttach)
f.write(coordenadasSistema)
f.write(physicsEngine)
f.write(shadown)
f.write(sol)
f.write(groundPlane)
for i in range(len(camX)):
    f.write(createTree(i, camX[i], camY[i]))
f.write(cameraSpawnObjects)
f.write(userCamera)
f.write(gripperPlugin)
f.write(guiFrameSinc)
f.write(end)
f.close()

f = open("rotas.txt", "w")
f.write(comment(camX))
f.write(comment(camY))
f.close()

plt.imshow(matriz)
plt.show()




