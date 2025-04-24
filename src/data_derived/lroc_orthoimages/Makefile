# make sure to have done "conda activate vipersci"

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
PROJ = ../viper.prj
VALIDATE = validate
CATALOG = ../../catalog23.xml
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

ORTHO = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/M108993634RE.map.tif

ORTHO_SRC_DIR = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps
# ORTHO_PATHS = $(ORTHO_SRC_DIR)/M108993634RE.map.tif $(ORTHO_SRC_DIR)/M1101075756LE.map.tif
ORTHO_PATHS = $(wildcard $(ORTHO_SRC_DIR)/M*.map.tif)


.PHONY: all 
XML_PATHS = $(addsuffix -ortho.xml, $(subst COG-,, $(basename $(wildcard COG-*.tif))))

%-ortho.xml %-ortho.tif: COG-%.tif $(MAP_LABEL) $(MAP_TEMP) ortho.yml
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -c lroc_list.csv -y ortho.yml -o $@ $<

# The symlinks target MUST be run before orthos.  There's probably a smarter way to do this, but
# I can't figure it out.
all: orthos

pre: symlinks

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
