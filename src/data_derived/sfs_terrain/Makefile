# make sure to have done "conda activate vipersci"
#
# Each of the sfs-* targets will need manual adjustments to the produced XML after being 
# generated.

VALIDATE = validate
CATALOG = ../../catalog23.xml


SFS = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem.tif
SFSLBL = $(addsuffix .xml, $(notdir $(basename $(SFS))))
COUNT = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/counts.tif
COUNTLBL = $(addprefix viper_, $(addsuffix .xml, $(notdir $(basename $(COUNT)))))
HEIGHTE = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_height_error.tif
HEIGHTELBL = $(addsuffix .xml, $(notdir $(basename $(HEIGHTE))))

LABELS = $(SFSLBL) $(COUNTLBL) $(HEIGHTELBL)
CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF \
	-co VAR_LOGICAL_IDENTIFIER=urn:nasa:pds:viper_geospatial:data_derived:viper_ \
	-co VAR_INVESTIGATION_AREA_NAME=VIPER \
	-co VAR_INVESTIGATION_AREA_LID_REFERENCE=urn:nasa:pds:viper \
	-co VAR_TARGET_TYPE=Satellite \
	-co VAR_target_type=satellite.earth.moon

.PHONY: all sfs-dem validate

all:
	echo No overall target, review Makefile.

sfs-dem:
	gdal_translate -of PDS4 $(SFS) -co IMAGE_FORMAT=GEOTIFF $(SFSLBL)

sfs-count:
	gdal_translate -of PDS4 $(COUNT) $(CREATIONOPTS) $(COUNTLBL)

sfs-heighte:
	gdal_translate -of PDS4 $(HEIGHTE) $(CREATIONOPTS) $(HEIGHTELBL)


validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf $(LABELS)

realclean: clean
	rm -rf $(addsuffix .tif, $(basename $(LABELS)))
