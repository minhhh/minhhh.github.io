##

help: # show help
	@echo ""
	@grep "^##" $(MAKEFILE_LIST) | grep -v grep
	@echo ""
	@grep "^[0-9a-zA-Z\-]*:.* #" $(MAKEFILE_LIST) | grep -v grep
	@echo ""

run: run # run
	cd blog && make devserver && make regenerate && make stopserver

stop: stop # stop
	cd blog && make stopserver

publish: # publish to master
	cd blog && git checkout source && make publish && git checkout gh-pages && ghp-import output && git checkout master && git merge gh-pages && git push --all && git checkout source
