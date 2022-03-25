import os
output='C:/pdftopdf/'
for ff in os.listdir(output):
    os.remove(os.path.join(output,ff))
os.rmdir(output)