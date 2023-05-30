SOURCES=$(shell ls sources/*.glyphs)
CHECKS=check-fontbakery
OTFDIR=fonts/otf
TTFDIR=fonts/ttf
WOFF2DIR=fonts/webfonts
VARDIR=fonts/variable

generate-image: $(VARDIR)
	. venv/bin/activate
	python3 scripts/generateImage.py

check-ttf: $(TTFDIR)
	mkdir -p $(CHECKS)/ttf;
	for file in $(TTFDIR)/*.ttf; do \
		echo $$file; \
		filename=$$(basename $$file .ttf); \
		fontbakery check-universal -l DEBUG --html $(CHECKS)/ttf/fontbakery-check-$$filename.html --ghmarkdown $(CHECKS)/ttf/fontbakery-check-$$filename.md $$file; \
	done

check-otf: $(OTFDIR)
	mkdir -p $(CHECKS)/otf;
	for file in $(OTFDIR)/*.otf; do \
		echo $$file; \
		filename=$$(basename $$file .otf); \
		fontbakery check-universal -l DEBUG --html $(CHECKS)/otf/fontbakery-check-$$filename.html --ghmarkdown $(CHECKS)/otf/fontbakery-check-$$filename.md $$file; \
	done

check-variable: $(VARDIR)
	mkdir -p $(CHECKS)/variable;
	for file in $(VARDIR)/*.ttf; do \
		echo $$file; \
		filename=$$(basename $$file .ttf); \
		fontbakery check-universal -l DEBUG --html $(CHECKS)/variable/fontbakery-check-$$filename.html --ghmarkdown $(CHECKS)/variable/fontbakery-check-$$filename.md $$file; \
	done

check-fonts:
	make check-ttf; make check-otf; make check-variable

build: dependencies
	. venv/bin/activate
	mkdir -p $(TTFDIR)
	fontmake -g "$(SOURCES)" -o ttf --output-dir $(TTFDIR) -i --flatten-components --verbose DEBUG
	mkdir -p $(OTFDIR)
	fontmake -g "$(SOURCES)" -o otf --output-dir $(OTFDIR) -i --verbose DEBUG
	python3 scripts/build.py
	mkdir -p $(VARDIR)
	fontmake -g "$(SOURCES)" -o variable --output-dir $(VARDIR) --flatten-components

clearFolder:
	rm -rf $(TTFDIR)/*.ttf; rm -rf $(OTFDIR)/*.otf; rm -rf $(VARDIR)/*.ttf; rm -rf $(WOFF2DIR)/*.woff2
	rm -rf $(CHECKS)
	rm -rf documentation/images/*.png

dependencies:
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt

clean:
	rm -rf venv
	rm -rf master_ufo
	rm -rf instance_ufo