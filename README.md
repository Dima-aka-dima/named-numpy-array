# Named numpy array
Creates a class that behaves like numpy array, but has user defined addressable attributes

Creating the class (last argument is just a type hint)
```
Point = getNamedNumpyClass('Point', ['x', 'y'])
Color = getNamedNumpyClass('Color', ['r', 'g', 'b'], np.uint8)
```
Using the class
```
point = Point(np.zeros(2))
color = Color(np.array([0, 255, 0], dtype = np.uint8))

print(point.x, point.y)
point += 1
print(point)
```

`getNamedNumpyArrayClass` names last axis. 
```
PointArray = getNamedNumpyArrayClass('PointArray', ['x', 'y'])
points = PointArray(np.arange(20).reshape(10, 2))
```
This is not safe because `points[0]` will return `Point`, which is okay, but so will `points.x` which is wrong.

Both functions raise assertion error for the wrong number of dimensions.

