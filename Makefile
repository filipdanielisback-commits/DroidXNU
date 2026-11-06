PYTHON ?= python3

.PHONY: check validate test report report-html clean

check: validate test

validate:
	$(PYTHON) tools/validate_device_config.py
	$(PYTHON) tools/validate_hardware_inventory.py

test:
	$(PYTHON) -m unittest discover -s tools -p 'test_*.py' -v

report:
	$(PYTHON) tools/generate_research_report.py

report-html:
	$(PYTHON) tools/generate_research_report.py --html-output build/research-report.html

clean:
	rm -rf build
