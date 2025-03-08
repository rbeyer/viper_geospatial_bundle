# make sure to have done "conda activate vipersci"

VALIDATE = validate
LABELMAKER_TEMPLATE = ../labelmaker_c_template.xml
CATALOG = ../catalog23.xml
DOCS = geospatial_ug


.PHONY: all collection clean realclean

all: collection

collection_document.xml collection_document.csv: labelmaker_c.yml geospatial_ug.xml
	labelmaker -v collection -c $< -t $(LABELMAKER_TEMPLATE) $(addsuffix .xml, $(DOCS))


collection:
	labelmaker -v collection -c labelmaker_c.yml -t $(LABELMAKER_TEMPLATE) $(addsuffix .xml, $(DOCS))

validateone:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target geospatial_ug.xml

validate:
	$(VALIDATE) --skip-context-validation --catalog $(CATALOG) --target $(addsuffix .xml, $(DOCS)) collection_document.xml

clean:
	rm -rf collection_document.csv
	rm -rf collection_document.xml

realclean: clean

