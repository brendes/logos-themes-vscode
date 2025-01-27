PYTHON_CMD = python3
BUILD_SCRIPT = src/build.py

build:
	mkdir -p themes
	$(PYTHON_CMD) $(BUILD_SCRIPT)

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json
	rm -rf src/__pycache__

.PHONY: build package publish clean
