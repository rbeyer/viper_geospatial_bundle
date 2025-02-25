VIPER Geospatial data_derived/lroc_orthoimages
==============================================

The creation of PDS4 XML labels in this directory generally begins with a `gdal_translate` followed by a `\.ortho_label.py` (see Makefile), to condition the XML and produce a better label.


lroc_list.csv
-------------

For each ortho product here, we must obtain the PDS4 LROC LIDVIDS.  These are a longer list consisting of all LROC NAC images that crossed the VIPER Extended Mission Area, not just those that were used for the SfS solution and listed in urn:nasa:pds:viper_geospatial:sfs_terrain.

Unfortunately, at this time the LROC data is not fully indexed in the PDS4 registry, so it cannot be directly queried.  Instead, this required a process to query the PDS3 CUMINDEX data to extract the FILE_SPECIFICATION, to construct a URL to query to extract the LID and the VID of the LROC products.  That script (since it requires other data handling) is not in this repo, but it is run (on Ross's system) like this::

        > conda activate sfstools
        > ~/software/sanctum/return_lroc_lidvid_parq.py -p ~/projects/LROC_pds/lroc_cumulative_south_polar.parquet -c lroc_list.csv /Users/rbeyer/projects/viper/viper-maps/lroc-nac-maps/M*tif

