PYTHON_CMD = python3
BUILD_SCRIPT = src/build.py

all: build

build:
	mkdir -p themes
	$(PYTHON_CMD) $(BUILD_SCRIPT)

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json

.PHONY: build package publish clean
