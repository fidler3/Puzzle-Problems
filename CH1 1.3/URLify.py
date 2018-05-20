


def URLify(str1, lenstr):
	chars = list(str1)
	for i, c in enumerate(chars):
		if c == " ":
			chars[i] = "%20"
	return ''.join(chars)

word = "benny and the jets"

print(URLify(word, len(word)))

