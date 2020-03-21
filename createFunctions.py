from PIL import Image


# Get a range of chars for construction of dicts
# This uses ord, so make sure not to have your range go over
# any unwanted chars.
def char_range(cStart, cEnd):
    for c in range(ord(cStart), ord(cEnd)+1):
        yield chr(c)

for c in char_range('a', 'z'):
	im = Image.open('letters/{}.png'.format(c))
	print('def letter_city_{}():\n\treturn ({}, {})\n'.format(c, im.width, im.tobytes() + b'\x00\x00\x00\x00'*im.width*(18-im.height)))

print('def letter_city_space():\n\treturn (5, None)\n')
# print(""im.tobytes())

print('LETTER_ARR_CITY = {')
keyVals = []
for c in char_range('a', 'z'):
	keyVals.append('\t\'{}\': letter_city_{}'.format(c, c))
keyVals.append('\t\' \': letter_city_space')
print(',\n'.join(keyVals))
print('}')