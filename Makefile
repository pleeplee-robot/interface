REQUIREMENTS=requirements.txt
TRASH=**/*.pyc

init:
	pip3 install -r $(REQUIREMENTS)

clean:
	rm -rf $(TRASH)

.PHONY: init test
