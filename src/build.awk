FILENAME != template {
	if (NF >= 2 && !/^#/) {
		k = $1
		val = $0; sub(/^[^ \t]+[ \t]+/, "", val)
		v[k] = val
	}
	next
}

!resolved {
	for (k in v)
		for (j in v)
			gsub("[{]" j "[}]", v[j], v[k])
	resolved = 1
}

{
	for (k in v)
		gsub("[{]" k "[}]", v[k])
	print
}
