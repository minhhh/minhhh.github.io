##

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:.* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

clean: # clean
	rm -fr venv

install: # install
	virtualenv venv
	. venv/bin/activate && pip install -r requirements.txt

run: run # run
	. venv/bin/activate && cd blog && make devserver && make regenerate && make stopserver

stop: stop # stop
	. venv/bin/activate && cd blog && make stopserver

publish: # publish to master
	. venv/bin/activate && cd blog && git checkout source && make html && git checkout gh-pages && ghp-import output && git checkout master && git merge gh-pages && git push --all && git checkout source
