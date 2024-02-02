import cv2
import numpy as np
import matplotlib.pyplot as plt
import Objects
from Vector3D import Vector3D
width = 600
height = 300
max_depth = 7

camera = Vector3D(0, 0, 1) ##Global co-ordinates and constants
ratio = float(width / height)
screen = (-1, 1 / ratio, 1, -1 / ratio)
image = np.zeros((height, width, 3))

def renderer():
    for i, y in enumerate(np.linspace(screen[1], screen[3], height)): ##going through each pixel in screen with a corresponding ratio on screen
        for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
            
            pixel = Vector3D(x, y, 0)
            origin = camera
            direction = (pixel - origin).normalize() ##calculating the direction vector

            color = Vector3D(0, 0, 0)
            reflection = 1 ##the summation of all the reflections

            for k in range(max_depth): ##how many reflections there will be
                nearest_object, min_distance = Vector3D.nearest_intersected_object(Objects.objects, origin, direction) ##getting nearest obj and min_distance
                if nearest_object is None: ##remove unnecessary computations if the ray did not intersect an object
                    break

                intersection = origin + (direction * min_distance) ##after getting the min_distance finding the intersection point

                normal_to_surface = (intersection - nearest_object['center']).normalize() ##finding normal to surface and slightly changing pos to prevent issues with rays reflecting back to camera
                shifted_point = intersection + (normal_to_surface * 1e-5)

                intersection_to_light = (Objects.light['position'] - shifted_point).normalize()

                _, min_distance = Vector3D.nearest_intersected_object(Objects.objects, shifted_point, ##finding if the object is in shadow if it is inbetween another object and light
                                                                      intersection_to_light)

                intersection_to_light_distance = (Objects.light['position'] - intersection).magnitude()
                is_shadowed_bool = min_distance < intersection_to_light_distance
                if is_shadowed_bool:
                    break ##if ray is shadowed break to prevent unneccesary computations
                illumination = Vector3D(0, 0, 0)

                illumination += nearest_object['ambient'].nummult(Objects.light['ambient']) #calculating illumination vector from diffuse, ambient, specular, shininess and reflection (Blinn-Phong)

                illumination += nearest_object['diffuse'].nummult(Objects.light['diffuse']) * intersection_to_light.dot(
                    normal_to_surface)

                intersection_to_camera = (camera - direction).normalize()
                h = (intersection_to_light + intersection_to_camera).normalize()
                illumination += nearest_object['specular'].nummult(Objects.light['specular']) * normal_to_surface.dot(
                    h) ** (nearest_object['shininess'] // 4)

                color += illumination * reflection
                reflection *= nearest_object['reflection']
                origin = shifted_point ##calculating the next ray
                direction = Vector3D.reflection(direction, normal_to_surface)
            image[i, j] = np.core.umath.maximum(np.core.umath.minimum([color.x, color.y, color.z], 1), 0) ##bounding rgb values between 1-0 (Unit RGB)
        print("Progress", i+1, "Out of", height) ##Progress counter
    plt.imsave('image.png', image) ##Displaying the image and reversing the color space to BGR from RGB
    cv2.imshow("product", image[:,:,::-1])
    cv2.waitKey(0)


if __name__ == "__main__":
    renderer() ##running the main method












