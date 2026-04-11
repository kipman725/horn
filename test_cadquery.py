import cadquery as cq
from cadquery import *
from cadquery.vis import show


wp = cq.Workplane("front")

radii = [1.5, 2.0, 3.0, 5.0]
height = 3.0

for r in radii:
    wp = wp.circle(r)
    wp = wp.workplane(offset=height)
result = wp.loft()

show(result)