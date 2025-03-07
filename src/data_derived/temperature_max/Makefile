# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

TMAX = /Users/rbeyer/projects/viper/viper-maps/temperature_max/viper_tmax.tif
TMAXLBL = viper_tmax.xml
TMAXTIF = $(addsuffix .tif, $(basename $(TMAXLBL)))
TMAXGDAL = $(addsuffix _gdal.xml, $(basename $(TMAXLBL)))
TMAXYML = $(addsuffix .yml, $(basename $(TMAXLBL)))

.PHONY: all clean realclean

all: tmax

$(TMAXLBL) $(TMAXTIF): $(TMAX) $(MAP_TEMP) $(TMAXYML)
	gdal_translate -of PDS4 $(TMAX) $(CREATIONOPTS) $(TMAXGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(TMAXLBL) -y $(TMAXYML) $(TMAXGDAL)

tmax: $(TMAXLBL) $(TMAXTIF)

validate:
	# $(VALIDATE) --skip-context-validation --target *.xml
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf viper_*.xml

realclean: clean
	rm -rf viper_*.tif
