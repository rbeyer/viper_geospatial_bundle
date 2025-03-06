# make sure to have done "conda activate vipersci"
#
# Each of the sfs-* targets will need manual adjustments to the produced XML after being 
# generated.

MAP_LABEL = ../map_label.py
MAP_TEMP = ../map_template.xml
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

HILL = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem_hs.tif
HILLLBL = viper_sfs_hillshade.xml
HILLGDAL = $(addsuffix _gdal.xml, $(basename $(HILLLBL)))
HILLYML = $(addsuffix .yml, $(basename $(HILLLBL)))
HILLTIFF = $(addsuffix .tif, $(basename $(HILLLBL)))

MASK = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_mask.tif
MASKLBL = viper_sfs_mask.xml
MASKGDAL = $(addsuffix _gdal.xml, $(basename $(MASKLBL)))
MASKYML = $(addsuffix .yml, $(basename $(MASKLBL)))
MASKTIFF = $(addsuffix .tif, $(basename $(MASKLBL)))

SLOPE = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_dem_slopes.tif
SLOPELBL = viper_sfs_slope.xml
SLOPEGDAL = $(addsuffix _gdal.xml, $(basename $(SLOPELBL)))
SLOPEYML = $(addsuffix .yml, $(basename $(SLOPELBL)))
SLOPETIFF = $(addsuffix .tif, $(basename $(SLOPELBL)))

WEIGHT = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_sfs_weight.tif
WEIGHTLBL = viper_sfs_weight.xml
WEIGHTGDAL = $(addsuffix _gdal.xml, $(basename $(WEIGHTLBL)))
WEIGHTYML = $(addsuffix .yml, $(basename $(WEIGHTLBL)))
WEIGHTTIFF = $(addsuffix .tif, $(basename $(WEIGHTLBL)))

MAXLIT = /Users/rbeyer/projects/viper/viper-maps/sfs/viper_max_lit.tif
MAXLITLBL = viper_maxlit.xml
MAXLITGDAL = $(addsuffix _gdal.xml, $(basename $(MAXLITLBL)))
MAXLITYML = $(addsuffix .yml, $(basename $(MAXLITLBL)))
MAXLITTIFF = $(addsuffix .tif, $(basename $(MAXLITLBL)))

LABELS = $(SFSLBL) $(COUNTLBL) $(HEIGHTELBL) $(HILLLBL) $(MASKLBL) $(SLOPELBL) $(WEIGHTLBL) $(MAXLITLBL)
TOCLEAN = $(SFSGDAL) $(SFSTIFF) \
	  $(COUNTGDAL) $(COUNTTIFF) \
	  $(HEIGHTEGDAL) $(HEIGHTETIFF) \
	  $(HILLGDAL) $(HILLTIFF) \
	  $(MASKGDAL) $(MASKTIFF) \
	  $(SLOPEGDAL) $(SLOPETIFF) \
	  $(WEIGHTGDAL) $(WEIGHTTIFF) \
	  $(MAXLITGDAL) $(MAXLITTIFF) \

CREATIONOPTS = -co IMAGE_FORMAT=GEOTIFF

.PHONY: all validate

all: dem count heighte hs mask slope weight maxlit

dem:
	gdal_translate -of PDS4 $(SFS) $(CREATIONOPTS) $(SFSGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(SFSLBL) -c viper_sfs_images.csv -y $(SFSYML) $(SFSGDAL)

count:
	gdal_translate -of PDS4 $(COUNT) $(CREATIONOPTS) $(COUNTGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(COUNTLBL) -c viper_ortho_images.csv -y $(COUNTYML) $(COUNTGDAL)

heighte:
	gdal_translate -of PDS4 $(HEIGHTE) $(CREATIONOPTS) $(HEIGHTEGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(HEIGHTELBL) -y $(HEIGHTEYML) $(HEIGHTEGDAL)

hs:
	gdal_translate -of PDS4 $(HILL) $(CREATIONOPTS) $(HILLGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(HILLLBL) -y $(HILLYML) $(HILLGDAL)

mask:
	gdal_translate -of PDS4 $(MASK) $(CREATIONOPTS) $(MASKGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(MASKLBL) -y $(MASKYML) $(MASKGDAL)

slope:
	gdal_translate -of PDS4 $(SLOPE) $(CREATIONOPTS) $(SLOPEGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(SLOPELBL) -y $(SLOPEYML) $(SLOPEGDAL)

weight:
	gdal_translate -of PDS4 $(WEIGHT) $(CREATIONOPTS) $(WEIGHTGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(WEIGHTLBL) -y $(WEIGHTYML) $(WEIGHTGDAL)

maxlit:
	gdal_translate -of PDS4 $(MAXLIT) $(CREATIONOPTS) $(MAXLITGDAL)
	$(MAP_LABEL) -t $(MAP_TEMP) -o $(MAXLITLBL) -y $(MAXLITYML) $(MAXLITGDAL)

validate:
	# $(VALIDATE) --skip-context-validation --target $(LABELS)
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(LABELS)

clean:
	rm -rf $(LABELS) $(TOCLEAN)

realclean: clean
	rm -rf $(addsuffix .tif, $(basename $(LABELS)))
