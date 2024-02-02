# Raytacing-in-Python-Personal-Project

After watching videos by Nvidia on the concept of raytracing, in addition to doing personal research, I undertook the challenge of coding a raytracer. I followed the guide of Omar Aflak, adding my own changes...

https://omaraflak.medium.com/ray-tracing-from-scratch-in-python-41670e6a96f9

### Introuction:

It took me a couple of days to wrap my head around the vector mathematics involved in a raytracer as well as attemping to understand how I would go about implementing vectors in the programming language. In other similar solutions, after researching online, I found that creating a vector class with three properties (XYZ) that has different vector operation methods would suit my use case more, and be more efficent than using a Numpy array and it's associated methods to represent the three (XYZ) coordinates. To do this, I created a Vector3D class. In additon to this, I researched more efficent methods and packages to speed up the running time. Finally, I implemented OpenCV display methods using them to display the image with a RGB color space instead of BGR.

### How Raytacing Works:

Essentially, by representing the viewpoint(display) as a vector with each pixel being represented as a vector, you can calculate the vector to each pixel of viewpoint from the origin to the camera and extrapolate it further into the scene. If the vector lands on an object, it will calculate if any objects of the scene are inbetween the reflected ray and the landed  ray. If it is, the object is in shadow. For each object, there are some properties of the object which can be calculated from the Vector, this is the Blinn-Phong algorithm. Then, for a set depth, the ray is reflected and each collision of the ray with an object is combined to form a final colour for that pixel of the image. 

Rinse and repeat this for each pixel of the image, and voila!

![image](https://github.com/eldh056867/Raytacing-in-Python-Personal-Project/assets/158150751/bff70693-8eb5-4c4d-a301-17d9dbd4f17d)

## A Ray-traced image!

Now unfortunately this is a very computationally taxing algorithm. However, it is relatively speaking simple compared to other algortihms. By increasing the image width and height, the time complexity increases by a factor of O(n^2). It is however, the most realistic algorithm as it can simulate light particles creating images identical to what would be produced in real life. Due to this, animation companies ray-trace their scences and this results in the most natural and authentic lighting as opposed to traditional lighting methods. In addition to this, games and PC's/Consoles have now got raytracing implementatitons, using dedicated hardware to calculate the vector mathematics to speed up the process. 

This is a greatly abstracted and simplified version of Ray-Tracing but from this project I have learned a lot about linear algebra as well as how the core of raytracing theory works. In addition to this, my Numpy knowledge has increased greatly thus helping me in future projects. 

Special thanks to Omar Aflak, 

-Eldho Rajan





