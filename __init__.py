import bpy

from . import import_latex_as_curve

bl_info = {
    "name": "import_latex_as_curve",
    "author": "Reijaff",
    "version": (0, 0, 1),
    "blender": (2, 8, 0),
    "location": "",
    "warning": "",
    "category": "3D View"}



def register():
    import_latex_as_curve.register()

def unregister():
    import_latex_as_curve.unregister()
