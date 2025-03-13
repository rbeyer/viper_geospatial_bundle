SRCDIR = src
BUNDLEDIR = bundle
VALIDATE = validate

.PHONY: src bundle clean install realclean validate

src:
	$(MAKE) -C $(SRCDIR)

pre:
	$(MAKE) -C $(SRCDIR) pre

bundle:
	bundle_install -v $(SRCDIR) $(BUNDLEDIR)

install: bundle
	cp $(SRCDIR)/data_derived/sfs_terrain/*csv $(BUNDLEDIR)/data_derived/sfs_terrain/

validate:
	$(VALIDATE) --skip-context-validation --rule pds4.bundle --target $(BUNDLEDIR)/

clean:
	rm -rf $(BUNDLEDIR)

realclean: clean
	$(MAKE) -C $(SRCDIR) realclean
