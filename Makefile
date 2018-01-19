REQUIREMENTS=requirements.txt
TRASH=**/*.pyc **/__pycache__

all: exec

exec:
	python3 -m pleepleeapp

init:
	pip3 install -r $(REQUIREMENTS)

doc:
	$(MAKE) -C docs/ html

clean:
	$(RM) -r $(TRASH)
	$(MAKE) -C docs/ clean

.PHONY: all init clean doc
