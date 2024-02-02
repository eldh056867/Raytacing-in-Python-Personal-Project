from Vector3D import Vector3D

objects = [ ##Properties of objects of type Vector3D
    {'center': Vector3D(-0.2, 0, -1), 'radius': 0.7, 'ambient': Vector3D(0.1,0,0), 'diffuse': Vector3D(0.7,0,0), 'specular': Vector3D(1,1,1), 'shininess': 100, 'reflection': 0.7},
    {'center': Vector3D(0.1, -0.3, 0), 'radius': 0.1, 'ambient': Vector3D(0.1,0,0.1), 'diffuse': Vector3D(0.7,0,0.7), 'specular': Vector3D(1,1,1), 'shininess': 100, 'reflection': 0.7},
    {'center': Vector3D(-0.3, 0, 0), 'radius': 0.15, 'ambient': Vector3D(0,0.1,0), 'diffuse': Vector3D(0,0.6,0), 'specular': Vector3D(1,1,1), 'shininess': 100, 'reflection': 0.7},
    {'center': Vector3D(0, -9000, 0), 'radius': 9000-0.7, 'ambient': Vector3D(0.1,0.1,0.1), 'diffuse': Vector3D(0.6,0.6,0.6), 'specular': Vector3D(1,1,1), 'shininess': 100, 'reflection': 1.0}
]

light = {'position': Vector3D(3,6,2), 'ambient': Vector3D(1,1,1), 'diffuse': Vector3D(1,1,1), 'specular': Vector3D(1,1,1)}




