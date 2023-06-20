abs_path = '/Users/sg/python/geekbrainz-python/l5/t1.py'
print(abs_path)


def parser(abs_path: str) -> tuple:
	full_name = abs_path.split('/')[-1]
	name, ext = full_name.split('.')
	path = abs_path.replace(full_name, '')

	return path, name, ext


path, name, ext = parser(abs_path)
print(f'{path=}, {name=}, {ext=}')

# /Users/sg/python/geekbrainz-python/l5/t1.py
# path='/Users/sg/python/geekbrainz-python/l5/', name='t1', ext='py'
