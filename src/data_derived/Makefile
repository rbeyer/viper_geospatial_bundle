# make sure to have done "conda activate vipersci"

VALIDATE = validate
CATALOG = ../catalog23.xml
LABELMAKER_TEMPLATE = ../labelmaker_c_template.xml
DIRS = depth_to_ice lroc_orthoimages permanently_shadowed_regions sfs_terrain temperature_max
TESTDIRS = lroc_orthoimages temperature_max

.PHONY: all collection clean realclean
.SECONDEXPANSION:

all: dirs collection

pre:
	$(foreach name, $(DIRS), $(MAKE) -C $(name) pre;)

# $(addsuffix /%.xml, $(TESTDIRS)): $(addsuffix /%.yml, $(TESTDIRS))
# 	$(foreach name, $(TESTDIRS), $(MAKE) -C $(name);)
# 
# testall: testdir test
# 
# testdir: $(addsuffix /*.xml, $(TESTDIRS))
# 	
# test: labelmaker_c.yml $(LABELMAKER_TEMPLATE) $$(foreach name, $(TESTDIRS), $$(name)/*.xml)
# 	echo $<
# 	echo $^
# 	echo $(wordlist 2, $(words $^), $^)
# 	echo $$(foreach name, $(TESTDIRS), $$(wildcard $$(name)/*.xml))

$(addsuffix /%.xml, $(DIRS)): $(addsuffix /%.yml, $(DIRS))
	$(foreach name, $(DIRS), $(MAKE) -C $(name);)

dirs: $(addsuffix /*.xml, $(DIRS))

collection_data_derived.xml: labelmaker_c.yml $(LABELMAKER_TEMPLATE) $$(foreach name, $(DIRS), $$(name)/*.xml)
	labelmaker -v collection -c $< -t $(filter-out sfs_terrain/viper_ortho_images_template.xml, $(wordlist 2, $(words $^), $^))

collection: collection_data_derived.xml
	
validate:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target collection_data_derived.xml

clean:
	rm -rf collection_data_derived.csv
	rm -rf collection_data_derived.xml

cleandirs:
	$(foreach name, $(DIRS), $(MAKE) -C $(name) realclean;)

realclean: clean cleandirs
