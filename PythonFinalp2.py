#To get this part to work, you must:
#   be running on Python 3.4.4
#   run IDLE in 3.4 in 34 Bit
#   make sure either PIL or pillow

import PIL
from PIL import Image

graph = Image.open("Rplot.jpeg")

graph.show()
