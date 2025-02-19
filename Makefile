SRCDIR = src
BUNDLEDIR = bundle
VALIDATE = validate

.PHONY: src bundle clean install realclean validate

src:
	$(MAKE) -C $(SRCDIR)

bundle:
	bundle_install -v $(SRCDIR) $(BUNDLEDIR)

install: bundle

validate:
	$(VALIDATE) --skip-context-validation --rule pds4.bundle --target $(BUNDLEDIR)/

clean:
	rm -rf $(BUNDLEDIR)

realclean: clean
	$(MAKE) -C $(SRCDIR) realclean
