PYTHON_CMD = python3
PIP_CMD = pip
BUILD_SCRIPT = src/build.py
VENV_DIR = .venv

all: build

setup:
	$(PYTHON_CMD) -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/$(PIP_CMD) install -r requirements.txt

build: setup
	$(VENV_DIR)/bin/$(PYTHON_CMD) $(BUILD_SCRIPT)

package: build
	vsce package

clean:
	rm -f *.vsix

.PHONY: setup build package clean
