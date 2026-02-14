include make/Makefile.inc

ZENSICAL := zensical

FIGS_GEN_DIR := src/mrs/figs

.PHONY: serve build clean

## Serve site locally
serve: build
	@$(RUN) $(ZENSICAL) serve

## Build site
build: clean
	@$(RUN) $(ZENSICAL) build --clean

## Generate figures
generate-figures:
	@make -C $(FIGS_GEN_DIR) generate-example-figure generate-rot-sequences deploy

## Clean site
clean:
	@rm -rf site
