# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

DICE = /Users/rbeyer/projects/viper/viper-maps/depth-to-ice/viper_dice.tif
DICELBL = viper_dice.xml
DICEGDAL = $(addsuffix _gdal.xml, $(basename $(DICELBL)))
DICEYML = $(addsuffix .yml, $(basename $(DICELBL)))

.PHONY: all clean realclean

all: dice

dice:
	gdal_translate -of PDS4 $(DICE) $(CREATIONOPTS) $(DICEGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(DICELBL) -y $(DICEYML) $(DICEGDAL)

validate:
	# $(VALIDATE) --skip-context-validation --target *.xml
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf viper_*.xml

realclean: clean
	rm -rf viper_*.tif
