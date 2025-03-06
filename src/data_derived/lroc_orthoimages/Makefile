# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

ORTHO = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/M108993634RE.map.tif
ORTHOGDAL = $(addsuffix _gdal.xml, $(notdir $(basename $(ORTHO))))

# MAPLBL = $(addsuffix .xml, $(notdir $(basename $(TESTMAP))))


.PHONY: all 

all:
	echo No overall target, review Makefile.

ortho:
	gdal_translate -of PDS4 $(ORTHO) $(CREATIONOPTS) $(ORTHOGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -c lroc_list.csv -y ortho.yml $(ORTHOGDAL)


validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf nac.m*ortho.xml

realclean: clean
	rm -rf nac.m*ortho.tif
