# make sure to have done "conda activate vipersci"

VALIDATE = /Users/rbeyer/opt/validate-3.4.1/bin/validate
CATALOG = ../catalog23.xml
DIRS = depth_to_ice lroc_orthoimages persistently_shadowed_regions sfs_terrain temperature_max

.PHONY: all pano collection clean realclean

all: dirs collection

dirs:
	$(foreach name, $(DIRS), $(MAKE) -C $(name);)

collection:
	labelmaker -v collection -c labelmaker_c.yml -t labelmaker_c_template.xml $(addsuffix /*.xml, $(DIRS))

validate:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target collection_data_derived.xml

clean:
	rm -rf collection_data_derived.csv
	rm -rf collection_data_derived.xml

cleandirs:
	$(foreach name, $(DIRS), $(MAKE) -C $(name) realclean;)

realclean: clean cleandirs
	rm -rf $(addsuffix .xml, $(IMAGES))
	rm -rf $(addsuffix .json, $(IMAGES))
	rm -rf $(addsuffix .tif, $(IMAGES))
