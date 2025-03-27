# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
PROJ = ../viper.prj
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

DICE = /Users/rbeyer/projects/viper/viper-maps/depth-to-ice/viper_dice.tif
DICEXML = viper_dice.xml
DICETIF = $(addsuffix .tif, $(basename $(DICEXML)))
DICEYML = $(addsuffix .yml, $(basename $(DICEXML)))

PDICE = /Users/rbeyer/projects/viper/viper-maps/depth-to-ice/viper_paleo_dice.tif
PDICEXML = viper_paleo_dice.xml
PDICETIF = $(addsuffix .tif, $(basename $(PDICEXML)))
PDICEYML = $(addsuffix .yml, $(basename $(PDICEXML)))

.PHONY: all clean realclean

all: dice pdice

pre:
	@echo No pre target for depth_to_ice.

$(DICEXML) $(DICETIF): $(DICE) $(DICEYML) $(MAP_TEMP)
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $@ -y $(DICEYML) $<

dice: $(DICEXML) $(DICETIF)

$(PDICEXML) $(PDICETIF): $(PDICE) $(PDICEYML) $(MAP_TEMP)
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $@ -y $(PDICEYML) $<

pdice: $(PDICEXML) $(PDICETIF)

validate:
	# $(VALIDATE) --skip-context-validation --target *.xml
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf viper_*.xml
	rm -rf viper_*.tif

realclean: clean
