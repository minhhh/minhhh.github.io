##

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:.* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

install: # install
	pipenv install --dev

run: # run
	cd blog && pipenv run make devserver PORT=8080 && pipenv run make stopserver

stop: # stop
	cd blog && pipenv run make stopserver

publish: # publish to master
	cd blog && git checkout source && make publish && git checkout gh-pages && ghp-import output && git checkout master && git merge gh-pages && git push --all && git checkout source
