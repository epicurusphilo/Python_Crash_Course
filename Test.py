import random
import sys
import os

tech_drawings = {'DRAW-0001' : 'folder technvdo',
                 'DRAW-0002' : 'folder nvdoops',
                 'DRAW-0003' : 'folder opstech'}

print(tech_drawings['DRAW-0002'])

print(len(tech_drawings))

print(tech_drawings.keys())

print(tech_drawings.values())

tech_drawings['DRAW-0002'] = 'titanops'

print(tech_drawings.get('DRAW-0002'))

print(tech_drawings.keys())

print(tech_drawings.values())

print(tech_drawings['DRAW-0002'])



