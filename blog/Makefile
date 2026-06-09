dev:
	hugo serve --buildDrafts --disableFastRender

build:
	hugo --minify

publish: build
	ghp-import -p -b master public/
