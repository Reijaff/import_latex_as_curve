import bpy

from . import import_latex_as_curve

bl_info = {
    "name": "import_latex_as_curve",
    "author": "reijaff",
    "version": (0, 1, 0),
    "blender": (3, 4, 0),
    "location": "",
    "description": "render latex as curve",
    "warning": "",
    "doc_url": "https://example.com",
    "category": "3D View"}



def register():
    import_latex_as_curve.register()

def unregister():
    import_latex_as_curve.unregister()
