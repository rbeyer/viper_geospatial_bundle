# make sure to have done "conda activate vipersci"
#
# Each of the sfs-* targets will need manual adjustments to the produced XML after being 
# generated.

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
PROJ = ../viper.prj
VALIDATE = validate
CATALOG = ../../catalog23.xml



SFS = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem.tif
SFSXML = $(addsuffix .xml, $(notdir $(basename $(SFS))))
SFSYML = $(addsuffix .yml, $(notdir $(basename $(SFSXML))))
SFSTIFF = $(addsuffix .tif, $(notdir $(basename $(SFS))))

COUNT = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/counts.tif
COUNTXML = $(addprefix viper_, $(addsuffix .xml, $(notdir $(basename $(COUNT)))))
COUNTYML = $(addsuffix .yml, $(notdir $(basename $(COUNTXML))))
COUNTTIFF = $(addsuffix .tif, $(notdir $(basename $(COUNTXML))))

HEIGHTE = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_height_error.tif
HEIGHTEXML = $(addsuffix .xml, $(notdir $(basename $(HEIGHTE))))
HEIGHTEYML = $(addsuffix .yml, $(notdir $(basename $(HEIGHTEXML))))
HEIGHTETIFF = $(addsuffix .tif, $(notdir $(basename $(HEIGHTEXML))))

HILL = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem_hs.tif
HILLXML = viper_sfs_hillshade.xml
HILLYML = $(addsuffix .yml, $(basename $(HILLXML)))
HILLTIFF = $(addsuffix .tif, $(basename $(HILLXML)))

MASK = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_mask.tif
MASKXML = viper_sfs_mask.xml
MASKYML = $(addsuffix .yml, $(basename $(MASKXML)))
MASKTIFF = $(addsuffix .tif, $(basename $(MASKXML)))

SLOPE = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem_slopes.tif
SLOPEXML = viper_sfs_slope.xml
SLOPEYML = $(addsuffix .yml, $(basename $(SLOPEXML)))
SLOPETIFF = $(addsuffix .tif, $(basename $(SLOPEXML)))

WEIGHT = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_weight.tif
WEIGHTXML = viper_sfs_weight.xml
WEIGHTYML = $(addsuffix .yml, $(basename $(WEIGHTXML)))
WEIGHTTIFF = $(addsuffix .tif, $(basename $(WEIGHTXML)))

MAXLIT = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_max_lit.tif
MAXLITXML = viper_maxlit.xml
MAXLITYML = $(addsuffix .yml, $(basename $(MAXLITXML)))
MAXLITTIFF = $(addsuffix .tif, $(basename $(MAXLITXML)))

IMGLISTXML = viper_ortho_images.xml

LABELS = $(SFSXML) $(COUNTXML) $(HEIGHTEXML) $(HILLXML) $(MASKXML) $(SLOPEXML) $(WEIGHTXML) $(MAXLITXML) $(IMGLISTXML)
TOCLEAN = $(SFSTIFF) \
	  $(COUNTTIFF) \
	  $(HEIGHTETIFF) \
	  $(HILLTIFF) \
	  $(MASKTIFF) \
	  $(SLOPETIFF) \
	  $(WEIGHTTIFF) \
	  $(MAXLITTIFF) \

CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

.PHONY: all validate

all: dem count heighte hs mask slope weight maxlit

pre:
	@echo No pre target for sfs_terrain.

dem:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(SFSXML) -y $(SFSYML) $(SFS)

count:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(COUNTXML) -y $(COUNTYML) $(COUNT)

heighte:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(HEIGHTEXML) -y $(HEIGHTEYML) $(HEIGHTE)

hs:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(HILLXML) -y $(HILLYML) $(HILL)

mask:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(MASKXML) -y $(MASKYML) $(MASK)

slope:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(SLOPEXML) -y $(SLOPEYML) $(SLOPE)

weight:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(WEIGHTXML) -y $(WEIGHTYML) $(WEIGHT)

maxlit:
	$(MAP_LABEL) -t $(MAP_TEMP) -p $(PROJ) -o $(MAXLITXML) -y $(MAXLITYML) $(MAXLIT)

ortholist: $(IMGLISTXML)

$(IMGLISTXML):
	./viper_ortho_images.py -c viper_ortho_images.csv -o $@ -t viper_ortho_images_template.xml -y viper_ortho_images.yml

validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf $(LABELS) $(TOCLEAN)

realclean: clean
	rm -rf $(addsuffix .tif, $(basename $(LABELS)))
