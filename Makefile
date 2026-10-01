init:
	uv sync

build: init
	uv run python src/build.py


vsix: build
	vsce package

publish: vsix
	vsce publish

clean:
	rm -f *.vsix themes/*.json

watch:
	find src/* | entr -c make build

table:
	@uv run python -c "\
import tomllib; \
d = tomllib.load(open('src/theme.toml', 'rb'))['palettes']; \
rows = sorted(((v['name'].removeprefix('Logos ').lower(), v['type'].lower(), v['base_0'].lower()) for v in d.values()), key=lambda r: r[2], reverse=True); \
print('| theme | type | base |'); \
print('|------|------|------|'); \
[print(f'| {n} | {t} | {b} |') for n, t, b in rows]"

.PHONY: init build package publish clean watch table
