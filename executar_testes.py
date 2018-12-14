import sys, doctest, os, glob

from getopt import gnu_getopt as getopt

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)

if __name__ == '__main__':
	run_level = None
	optlist, args = getopt(sys.argv[1:], "l:", ['--level='])

	for opt, arg in optlist:
		if opt in ('-l', '--list'):
			run_level = arg.zfill(2)

	if run_level is None:
		search_path = '%s/*.txt' % os.path.join(CUR_DIR, 'tests')
	else: search_path = '%s/%s-*.txt' % (os.path.join(CUR_DIR, 'tests'), run_level)

	test_files = glob.glob(search_path)
	test_files = map(lambda i: i[len(CUR_DIR)+1:], test_files)

	for fName in test_files:
		print('Executando "%s"...'%(os.path.splitext(os.path.split(fName)[-1])[0]))

		doctest.testfile(fName)

	print('Testes concluídos!!')
