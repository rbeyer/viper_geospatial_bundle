=======================
VIPER Geospatial Bundle
=======================

This repo provides part of the basis for creating the whole VIPER Geospatial Bundle.

This repo does NOT contain binary data files, but does contain the framework of XML files,
Makefiles, etc., that can be used to build the VIPER Geospatial Bundle.

The src/ directory contains the "source" information for the bundle,
and contains a Makefile and a few files for the vipersci labelmaker program
that will help build the bundle label.

If the bundle and collection directories are "clean" then just
typing "make" at the top level here should build up all of the
products, collection, and bundle files.

And then "make install" should create a bundle/ directory with files ready to be delivered to PDS.


Getting Started
---------------

You will need to have `vipersci <https://github.com/NeoGeographyToolkit/vipersci>` installed.  As well as having the `PDS4 Validate Tool <https://nasa-pds.github.io/validate/>` available in the environment as "validate".
