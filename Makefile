ifeq ($(XDG_CONFIG_HOME),)
ZED_CONFIG_DIR := $(HOME)/.config/zed
else
ZED_CONFIG_DIR := $(XDG_CONFIG_HOME)/zed
endif

COPY := $$(command -v cp) -v

init:
	uv sync

build: init
	uv run python src/build.py

zed: build
	$(COPY) -r themes/zed/*.json $(ZED_CONFIG_DIR)/themes/

all: build zed

vsix: build
	vsce package

publish: vsix
	vsce publish

clean:
	rm -f *.vsix themes/vscode/*.json themes/zed/*.json

watch:
	find src/* | entr -c make build

table:
	@uv run python -c "\
import tomllib; \
d = tomllib.load(open('src/colors.toml', 'rb'))['palettes']; \
rows = sorted(((v['name'].removeprefix('Logos ').lower(), v['type'].lower(), v['color_base_00'].lower()) for v in d.values()), key=lambda r: r[2], reverse=True); \
print('| theme | type | base |'); \
print('|------|------|------|'); \
[print(f'| {n} | {t} | {b} |') for n, t, b in rows]"

.PHONY: init build vsix publish zed clean watch table
