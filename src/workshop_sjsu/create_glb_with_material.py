import os
import json
from workshop_sjsu import DATA
from workshop_sjsu import WEB
from compas.datastructures import Mesh
from compas.files import GLTFContent
from compas.files import GLTFExporter
from compas.files.gltf.data_classes import MaterialData, PBRMetallicRoughnessData
from compas.files.gltf.extensions import KHR_materials_pbrSpecularGlossiness


name = "test02"

# 1. Load meshes
filepath = os.path.join(DATA, "mesh_data.json")

with open(filepath, 'r') as f:
    data = json.load(f)

meshes = [Mesh.from_data(mesh_data) for mesh_data in data]


# 2. Create GLTF content

content = GLTFContent()
scene = content.add_scene("half-sphere")


# 2.a create material
material = MaterialData()
material.name = 'Plaster'
material.pbr_metallic_roughness = PBRMetallicRoughnessData()
material.pbr_metallic_roughness.base_color_factor = [
    0.156862751, 0.831372559, 0.7764706, 1.0]
material.double_sided = True
pbr_specular_glossiness = KHR_materials_pbrSpecularGlossiness()
pbr_specular_glossiness.diffuse_factor = [
    0.156862751, 0.831372559, 0.7764706, 1.0]
pbr_specular_glossiness.specular_factor = [0.0, 0.0, 0.0]
pbr_specular_glossiness.glossiness_factor = 0.
material.add_extension(pbr_specular_glossiness)
content.add_material(material)

# 2.b add meshes
for i, cmesh in enumerate(meshes):
    key = "line_%05d" % i
    node = content.add_node_to_scene(scene, node_name=key)
    mesh_data = content.add_mesh_to_node(node, cmesh)
    # mesh_data.primitive_data_list[0].material = material # how to add material?

# 3. Export GLTF
filepath = os.path.join(os.path.join(WEB, "glb"), name + ".glb")
exporter = GLTFExporter(filepath, content, embed_data=True)
exporter.export()

# 4. write html
example_html = os.path.join(WEB, "example00.html")  # == template

with open(example_html) as f:
    contents = f.read()
contents = contents.replace("example00", name)

new_html = os.path.join(WEB, "%s.html" % name)
with open(new_html, 'w+') as f:
    f.write(contents)

# run localhost.py and visit
# http://127.0.0.1:8000/%s.html % name
