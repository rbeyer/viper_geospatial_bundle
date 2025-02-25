VIPER Geospatial data_derived/sfs_terrain
=========================================

The creation of PDS4 XML labels in this directory generally begins with a `gdal_translate` (see Makefile), and then a manual editing.


viper_sfs_images.csv
--------------------

In order to list all of the LROC NAC images that were input for the viper_sfs_dem, we decided to list them in viper_sfs_images.csv.

Unfortunately, at this time the LROC data is not fully indexed in the PDS4 registry, so it cannot be directly queried.  Instead, this required a process to query the PDS3 CUMINDEX data to extract the FILE_SPECIFICATION, to construct a URL to query to extract the LID and the VID of the LROC products.  That script (since it requires other data handling) is not in this repo, but it is run (on Ross's system) like this::

        > conda activate sfstools
        > ~/software/sanctum/return_lroc_lidvid_parq.py -p ~/projects/LROC_pds/lroc_cumulative_south_polar.parquet -c viper_sfs_images.csv ~/projects/viper/viper-maps/sfs/viper_sfs_images.txt



viper_ortho_images.csv
----------------------

Other products needed lists of the VIPER Orthoimages in urn:nasa:pds:viper_geospatial:lroc_orthoimages, which were just the ortho versions of the products listed in `viper_sfs_images.csv`.

This was created via::

        > ./images2ortho.py viper_sfs_images.csv viper_ortho_images.csv


