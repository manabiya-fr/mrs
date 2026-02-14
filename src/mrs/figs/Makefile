ROOT_DIR := ../../..
include $(ROOT_DIR)/make/Makefile.inc

OUT_DIR := out

define build_standalone_fig
	@pdflatex -jobname=$(OUT_DIR)/$(1) "\def\figureparam{$(OUT_DIR)/$(1).pgf} \input{tex/standalone_fig.tex}"
	@pdf2svg $(OUT_DIR)/$(1).pdf $(OUT_DIR)/$(1).svg
endef

## Generate example figure
generate-example-figure: | $(OUT_DIR)
	@$(RUN) example_figure.py
	$(call build_standalone_fig,example)

## Generate rotation sequence
generate-rot-sequences: | $(OUT_DIR)
	@$(RUN) rot_sequences.py --fixed-frame
	$(call build_standalone_fig,euler_xyz_around_fixed_frame)

	@$(RUN) rot_sequences.py --current-frame
	$(call build_standalone_fig,euler_zyz_around_current_frame)

deploy: ## Copy figures to docs
	@cp $(OUT_DIR)/*.svg $(ROOT_DIR)/docs/figures

clean: ## Clean generated files
	@rm -rf $(OUT_DIR) __pycache__

$(OUT_DIR):
	@mkdir -p $(OUT_DIR)
