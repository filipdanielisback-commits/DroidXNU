PYTHON ?= python3

.PHONY: check validate test

check: validate test

validate:
	$(PYTHON) tools/validate_device_config.py
	$(PYTHON) tools/validate_hardware_inventory.py

test:
	$(PYTHON) -m unittest discover -s tools -p 'test_*.py' -v
