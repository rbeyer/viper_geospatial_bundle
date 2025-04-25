=========
Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
however, this project cannot adhere to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_
because of how PDS4 versioning works.

Since PDS4 versioning does not allow versions less than 1.0, we will use version 999.1 as we would usually use 0.1 in Semantic Versioning during preparation in the lead up to the 1.0 release.

When updating this file, please add an entry for your change under
Unreleased_ and one of the following headings:

- Added - for new features.
- Changed - for changes in existing functionality.
- Deprecated - for soon-to-be removed features.
- Removed - for now removed features.
- Fixed - for any bug fixes.
- Security - in case of vulnerabilities.

If the heading does not yet exist under Unreleased_, then add it
as a 3rd level heading, underlined with pluses (see examples below).

When preparing for a public release add a new 2nd level heading,
underlined with dashes under Unreleased_ with the version number
and the release date, in year-month-day format (see examples below).


Unreleased
----------


999.2 (2025-04-25)
------------------
This is the version that was submitted for PDS review.

The known issues are: 

- The Users Guide is not PDF1a compliant 
- The Beyer et al. VIPER Site Analysis paper is currently only "submitted" and does not have a proper DOI.

Added
^^^^^
- Added the PSR map to the bundle.
- Added DOIs for the UG and bundle provided by Trent.
- Added authors to the bundle and UG.
- LIDVID, title, and date now inserted into the TIFFTAGS for the GeoTIFFs.

Changed
^^^^^^^
- Made the viper_ortho_list a "full" product.
- Made the viper_ortho_list a Source_Product_Internal.



999.1 (2025-03-13)
------------------

- First draft.
