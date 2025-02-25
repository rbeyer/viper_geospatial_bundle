# make sure to have done "conda activate vipersci"
#
VALIDATE = validate
CATALOG = ../../catalog23.xml


TESTMAP = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/M108993634RE.map.tif
MAPLBL = $(addsuffix .xml, $(notdir $(basename $(TESTMAP))))

LABELS = $(MAPLBL)

.PHONY: all sfs-dem validate

all:
	echo No overall target, review Makefile.

map:
	gdal_translate -of PDS4 $(TESTMAP) -co IMAGE_FORMAT=GEOTIFF $(MAPLBL)
	./ortho_label.py -t ortho-template.xml -c lroc_list.csv $(MAPLBL)

validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf $(LABELS)

realclean: clean
	rm -rf $(addsuffix .tif, $(basename $(LABELS)))
