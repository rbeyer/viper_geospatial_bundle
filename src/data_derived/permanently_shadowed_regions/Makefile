# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
PROJ = ../viper.prj
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

PSR = /Users/rbeyer/projects/viper/viper-maps/psr/viper_psr.tif
PSRLBL = viper_psr.xml
PSRTIF = $(addsuffix .tif, $(basename $(PSRLBL)))
PSRYML = $(addsuffix .yml, $(basename $(PSRLBL)))

.PHONY: all clean realclean

all: psr

pre:
	@echo No pre target for psr.

$(PSRLBL) $(PSRTIF): $(PSR) $(MAP_TEMP) $(PSRYML)
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(PSRLBL) -y $(PSRYML) $(PSR)

psr: $(PSRLBL) $(PSRTIF)

validate:
	# $(VALIDATE) --skip-context-validation --target *.xml
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf viper_*.xml

realclean: clean
	rm -rf viper_*.tif
