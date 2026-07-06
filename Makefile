build:
	./build

package: build
	vsce package

publish: package
	vsce publish

clean:
	rm -f *.vsix themes/*.json

watch:
	find src/* | entr -c make build

table:
	{ \
		printf '| theme | type | base |\n|------|------|------|\n'; \
		awk ' \
		function f() { \
			n=a["name"]; sub(/^Logos /,"",n); \
			print "| " tolower(n) " | " tolower(a["type"]) " | " tolower(a["base_0"]) " |"; \
			delete a \
		} \
		FNR==1 && NR>1 { f() } \
		{ k=$$1; sub(/^[^ ]+ /,""); a[k]=$$0 } \
		END { f() } \
		' src/colors/*.conf | sort -k6,6 -r; \
	}

.PHONY: build package publish clean watch table
