# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

ORTHO = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/M108993634RE.map.tif
ORTHOGDAL = $(addsuffix _gdal.xml, $(notdir $(basename $(ORTHO))))

ORTHO_SRC_DIR = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/
# ORTHO_PATHS = $(wildcard $(ORTHO_SRC_DIR)/*tif)
ORTHO_PATHS = $(ORTHO_SRC_DIR)/M108993634RE.map.tif $(ORTHO_SRC_DIR)/M1101075756LE.map.tif
XML_PATHS = $(addsuffix -ortho.xml, $(subst COG-,, $(basename $(wildcard COG-*.tif))))


.PHONY: all 

%-ortho.xml: COG-%.tif
	gdal_translate -of PDS4 $< $(CREATIONOPTS) $(addsuffix _gdal.xml, $(notdir $(basename $<)))
	$(MAP_LABEL) -t $(MAP_TEMP) -c lroc_list.csv -y ortho.yml $(addsuffix _gdal.xml, $(notdir $(basename $<)))

all:
	@echo No overall target, but make symlinks, then make orthos.

symlinks:
	./cog_symlink.py $(ORTHO_PATHS)

orthos: $(XML_PATHS)


validate:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target *.xml

clean:
	rm -rf nac.m*ortho.xml
	rm -rf nac.m*ortho.tif

realclean: clean
	rm -rf COG-*tif
