# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
PROJ = ../viper.prj
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

TMAX = /Users/rbeyer/projects/viper/viper-maps/temperature_max/viper_tmax.tif
TMAXLBL = viper_tmax.xml
TMAXTIF = $(addsuffix .tif, $(basename $(TMAXLBL)))
TMAXYML = $(addsuffix .yml, $(basename $(TMAXLBL)))

.PHONY: all clean realclean

all: tmax

pre:
	@echo No pre target for temperature_max.

$(TMAXLBL) $(TMAXTIF): $(TMAX) $(MAP_TEMP) $(TMAXYML)
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(TMAXLBL) -y $(TMAXYML) $(TMAX)

tmax: $(TMAXLBL) $(TMAXTIF)

validate:
	# $(VALIDATE) --skip-context-validation --target *.xml
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf viper_*.xml

realclean: clean
	rm -rf viper_*.tif
