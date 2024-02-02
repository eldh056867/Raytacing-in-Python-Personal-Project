import math
from math import sqrt
import numpy as np
class Vector3D: ##Vector3D class that has Dunder methods to represent each operation. Has parameters XYZ to represent XYZ coordinates
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __truediv__(self, scalar):
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def nummult(self, other):
        return Vector3D(self.x*other.x, self.y*other.y, self.z*other.z)



    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector3D(0, 0, 0)
        return self / mag

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    @staticmethod #Calculating if sphere intersects ray by calculating discriminant
    def sphere_intersect(center, radius, ray_origin, ray_direction):
        ray_origin_minus_center = ray_origin-center
        b = 2 * ray_direction.dot(ray_origin_minus_center)
        c = Vector3D.magnitude(ray_origin_minus_center)**2 - radius ** 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + sqrt(delta)) / 2
            t2 = (-b - sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return None

    @staticmethod
    def nearest_intersected_object(objects, ray_origin, ray_direction): ##Calculating nearest object by finding min distance to objects in object list and returning closest object with its corresponding distance
        distances = [Vector3D.sphere_intersect(obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
        nearest_object = None
        min_distance = np.inf
        for index, distance in enumerate(distances):
            if distance and distance < min_distance:
                min_distance = distance
                nearest_object = objects[index]
        return nearest_object, min_distance
    @staticmethod
    def reflection(vector, axis): ##Calculating reflection of vector to surface
        return vector - axis*(vector.dot(axis))*2

