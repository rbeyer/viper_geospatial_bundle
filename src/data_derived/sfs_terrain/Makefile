# make sure to have done "conda activate vipersci"
#
#
# Manual build of LIDVIDS for viper_sfs_dem.xml
# Use the sfstools environment and:
# $> ~/software/sanctum/return_lroc_lidvid_parq.py -p ~/projects/LROC_pds/lroc_cumulative_south_polar.parquet -x lidvids.xml viper_sfs_images.txt
# The resulting XML can then be manually inserted into the viper_sfs_dem.xml file.

VALIDATE = /Users/rbeyer/opt/validate-3.6.3/bin/validate
CATALOG = ../../catalog23.xml
SFS = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem.tif
SFSLBL = viper_sfs_dem.xml
LABELS = $(SFSLBL)

.PHONY: all sfs-dem validate

all:
	echo No overall target, review Makefile.

sfs-dem:
	gdal_translate -of PDS4 $(SFS) -co IMAGE_FORMAT=GEOTIFF $(SFSLBL)

validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf $(LABELS)

realclean: clean
	rm -rf $(addsuffix .tif, $(basename $(LABELS)))
