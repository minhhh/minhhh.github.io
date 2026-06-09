dev:
	cd blog && hugo serve --buildDrafts --disableFastRender

build:
	cd blog && hugo --minify && npx pagefind --site public
