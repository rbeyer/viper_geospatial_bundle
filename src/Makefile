VALIDATE = validate
CATALOG = catalog23.xml
COLLECTIONS = data_derived document browse
COLLECTIONSXML = $(foreach name, $(COLLECTIONS), $(name)/collection_$(name).xml)

.PHONY: all db collections bundle clean realclean clean collections

all: collections bundle


collections:
	$(foreach name, $(COLLECTIONS), $(MAKE) -C $(name);)


bundle:
	labelmaker -v bundle -c labelmaker_b.yml -t labelmaker_b_template.xml $(COLLECTIONSXML)

validate:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target bundle.xml

clean:
	rm -rf bundle.xml

cleancollections:
	$(foreach name, $(COLLECTIONS), $(MAKE) -C $(name) realclean;)

realclean: clean cleancollections
	rm -rf $(DBFILE)
