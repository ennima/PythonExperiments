import os

max_mtime = 0
for dirname,subdir,files in os.walk("."):
	for fname in files:
		full_path = os.path.join(dirname, fname)
		mtime = os.stat(full_path).st_mtime
		if mtime > max_mtime:
			max_mtime = mtime
			max_dir = dirname
			max_file = fname
			print "max_dir: "+max_dir+" --- max_file: "+max_file
