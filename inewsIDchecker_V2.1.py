import time
from PyQt5 import QtWidgets, uic


def hascyr(words):
	lower = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюяйцукенгшщзхїфівапролджєячсмитьбю')
	return lower.intersection(words.lower()) != set()


words = input('Input iNEWS ID here: ')
unisearch = hascyr(words)

if (len(words) <= 30):
	print('ID lenght is okay')
	if(unisearch == True):
		print('ID contains cyryllic')
	else:
		print('ID is correct')
	print(len(words))

elif (len(words) >= 31):
	print('ID is too lenghty')
	if(unisearch == True):
		print('ID contains cyryllic')
	else:
		print('ID is correct')
	print(len(words))

cyryl = ['а', 'А', 'с', 'С', 'і', 'І', 'е', 'Е', 'о', 'О', 'р', 'Р', 'К', 'к', 'B', 'Т']
for i in words:
	if i in cyryl:
		print('Cyrylic is :', i)

time.sleep(60)

