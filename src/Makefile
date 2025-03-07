VALIDATE = validate
CATALOG = catalog23.xml
COLLECTIONS = data_derived document
COLLECTIONSXML = $(foreach name, $(COLLECTIONS), $(name)/collection_$(name).xml)

.PHONY: all collections bundle clean realclean cleancollections

all: collections bundle


collections:
	$(foreach name, $(COLLECTIONS), $(MAKE) -C $(name);)


bundle.xml: labelmaker_b.yml labelmaker_b_template.xml $(COLLECTIONSXML)
	labelmaker -v bundle -c $< -t $(wordlist 2, $(words $^), $^)

bundle: bundle.xml

validate:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target bundle.xml

clean:
	rm -rf bundle.xml

cleancollections:
	$(foreach name, $(COLLECTIONS), $(MAKE) -C $(name) realclean;)

realclean: clean cleancollections
