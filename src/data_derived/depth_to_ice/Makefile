# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

DICE = /Users/rbeyer/projects/viper/viper-maps/depth-to-ice/viper_dice.tif
DICELBL = viper_dice.xml
DICETIF = $(addsuffix .tif, $(basename $(DICELBL)))
DICEGDAL = $(addsuffix _gdal.xml, $(basename $(DICELBL)))
DICEYML = $(addsuffix .yml, $(basename $(DICELBL)))

PDICE = /Users/rbeyer/projects/viper/viper-maps/depth-to-ice/viper_paleo_dice.tif
PDICELBL = viper_paleo_dice.xml
PDICETIF = $(addsuffix .tif, $(basename $(PDICELBL)))
PDICEGDAL = $(addsuffix _gdal.xml, $(basename $(PDICELBL)))
PDICEYML = $(addsuffix .yml, $(basename $(PDICELBL)))

.PHONY: all clean realclean

all: dice pdice

pre:
	@echo No pre target for depth_to_ice.

$(DICELBL) $(DICETIF): $(DICE) $(DICEYML) $(MAP_TEMP)
	gdal_translate -of PDS4 $(DICE) $(CREATIONOPTS) $(DICEGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(DICELBL) -y $(DICEYML) $(DICEGDAL)

dice: $(DICELBL) $(DICETIF)

$(PDICELBL) $(PDICETIF): $(PDICE) $(PDICEYML) $(MAP_TEMP)
	gdal_translate -of PDS4 $(PDICE) $(CREATIONOPTS) $(PDICEGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(PDICELBL) -y $(PDICEYML) $(PDICEGDAL)

pdice: $(PDICELBL) $(PDICETIF)

validate:
	# $(VALIDATE) --skip-context-validation --target *.xml
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf viper_*.xml
	rm -rf viper_*.tif

realclean: clean
