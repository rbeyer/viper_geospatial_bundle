# make sure to have done "conda activate vipersci"
#
# Each of the sfs-* targets will need manual adjustments to the produced XML after being 
# generated.

MAP_LABEL = ./map_label.py
VALIDATE = validate
CATALOG = ../../catalog23.xml


SFS = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem.tif
SFSGDAL = $(addsuffix _gdal.xml, $(notdir $(basename $(SFS))))
SFSLBL = $(addsuffix .xml, $(notdir $(basename $(SFS))))
SFSYML = $(addsuffix .yml, $(notdir $(basename $(SFSLBL))))
SFSTIFF = $(addsuffix .tif, $(notdir $(basename $(SFS))))

COUNT = /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/counts.tif
COUNTGDAL = $(addprefix viper_, $(addsuffix _gdal.xml, $(notdir $(basename $(COUNT)))))
COUNTLBL = $(addprefix viper_, $(addsuffix .xml, $(notdir $(basename $(COUNT)))))
COUNTYML = $(addsuffix .yml, $(notdir $(basename $(COUNTLBL))))
COUNTTIFF = $(addsuffix .tif, $(notdir $(basename $(COUNTLBL))))

HEIGHTE = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_height_error.tif
HEIGHTEGDAL = $(addsuffix _gdal.xml, $(notdir $(basename $(HEIGHTE))))
HEIGHTELBL = $(addsuffix .xml, $(notdir $(basename $(HEIGHTE))))
HEIGHTEYML = $(addsuffix .yml, $(notdir $(basename $(HEIGHTELBL))))
HEIGHTETIFF = $(addsuffix .tif, $(notdir $(basename $(HEIGHTELBL))))

LABELS = $(SFSLBL) $(COUNTLBL) $(HEIGHTELBL)
TOCLEAN = $(SFSGDAL) $(SFSTIFF) \
	  $(COUNTGDAL) $(COUNTTIFF) \
	  $(HEIGHTEGDAL) $(HEIGHTETIFF) \

CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

.PHONY: all sfs-dem validate

all:
	echo No overall target, review Makefile.

sfs-dem:
	gdal_translate -of PDS4 $(SFS) $(CREATIONOPTS) $(SFSGDAL)
	$(MAP_LABEL) -t map_template.xml -o $(SFSLBL) -c viper_sfs_images.csv -y $(SFSYML) $(SFSGDAL)

sfs-count:
	gdal_translate -of PDS4 $(COUNT) $(CREATIONOPTS) $(COUNTGDAL)
	$(MAP_LABEL) -t map_template.xml -o $(COUNTLBL) -c viper_ortho_images.csv -y $(COUNTYML) $(COUNTGDAL)

sfs-heighte:
	gdal_translate -of PDS4 $(HEIGHTE) $(CREATIONOPTS) $(HEIGHTEGDAL)
	$(MAP_LABEL) -t map_template.xml -o $(HEIGHTELBL) -y $(HEIGHTEYML) $(HEIGHTEGDAL)


validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf $(LABELS) $(TOCLEAN)

realclean: clean
	rm -rf $(addsuffix .tif, $(basename $(LABELS)))
