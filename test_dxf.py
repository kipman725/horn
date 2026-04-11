import cadquery as cq
from cadquery import *
from cadquery.vis import show

height = 60.0
width = 80.0
thickness = 10.0
diameter = 22.0
padding = 12.0

# make the base
result = (
    cq.Workplane("XY")
    .box(height, width, thickness)
    .faces(">Z")
    .workplane()
    .hole(diameter)
    .faces(">Z")
    .workplane()
    .rect(height - padding, width - padding, forConstruction=True)
    .vertices()
    .cboreHole(2.4, 4.4, 2.1)
    .edges("|Z")
    .fillet(2.0)
)

# Render the solid
test_output = result.section()
test_output.export("result.step")
# Export
#cq.exporters.export(result, "result.stl")
#cq.exporters.exportDXF(result.section(), "result.dxf", approx="arc", doc_units = 4)
cq.exporters.exportDXF(result.section(), "result.dxf")
#cq.exporters.export(result, "result.step")