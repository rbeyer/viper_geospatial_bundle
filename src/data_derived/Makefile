# make sure to have done "conda activate vipersci"

VALIDATE = validate
CATALOG = ../catalog23.xml
LABELMAKER_TEMPLATE = ../labelmaker_c_template.xml
DIRS = depth_to_ice lroc_orthoimages sfs_terrain temperature_max
LABELS = $(addsuffix /*.xml, $(DIRS))

.PHONY: all collection clean realclean

all: dirs collection

dirs:
	$(foreach name, $(DIRS), $(MAKE) -C $(name);)

collection_data_derived.xml collection_data_derived.csv: labelmaker_c.yml $(LABELMAKER_TEMPLATE) $(LABELS)
	labelmaker -v collection -c $< -t $(wordlist 2, $(words $^), $^)

collection: collection_data_derived.xml collection_data_derived.csv
	
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
