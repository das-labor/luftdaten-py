import sys

import requests
import json
import osm2geojson
import shapely
import shapely.wkb

drs, shapefile_name, boundsfile_name = sys.argv[1:]
overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = """
[out:json];
area["ISO3166-1"="DE"];
rel["de:regionalschluessel"="%s"](area);
out geom;
""" % drs
# 059130000000 Regionalschl. Dortmund


response = requests.get(overpass_url, params={'data': overpass_query})
try:
    data = response.json()
except:
    print(response.content)
    raise

geos = osm2geojson.json2geojson(data)
print(geos)
fullgeom = shapely.ops.unary_union([shapely.geometry.shape(geo['geometry']) for geo in
                                    geos['features']])
print(fullgeom)

with open(shapefile_name, 'wb') as shapefile:
    shapefile.write(shapely.wkb.dumps(fullgeom))

with open(boundsfile_name, 'w') as boundsfile:
    boundsfile.write(' '.join(str(x) for x in fullgeom.bounds))
