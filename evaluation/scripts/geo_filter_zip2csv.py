import sys
import zipfile
import os

#import shapely
#import shapely.wkb

input_name, output_name, boundsfile_name = sys.argv[1:]
def process():

   #with open(shapefile_name, 'rb') as shapefile:
   #    shape = shapely.wkb.loads(shapefile.read())
   #    bounds = shape.bounds

    with open(boundsfile_name, 'r') as boundsfile:
        bounds = [float(x) for x in boundsfile.read().split(' ')]

    with zipfile.ZipFile(input_name) as input_zip:
        with input_zip.open(
            os.path.basename(input_name).replace('.zip','.csv')) as input_csv:
                with open(output_name, 'w') as output_csv:
                    for i, line in enumerate(input_csv):
                        line = line.decode('utf-8')
                        if not i:
                            output_csv.write(line)
                            continue
                        if not line.strip() or ';' not in line:
                            continue
                        parts = line.strip().split(';')
                        lat, lon = parts[3:5]
                        if not lat or not lon:
                            continue
                        lat = float(lat)
                        lon = float(lon)

                        if bounds[0] <= lon <= bounds[2] and \
                           bounds[1] <= lat <= bounds[3]:
                             output_csv.write(line)


process()
