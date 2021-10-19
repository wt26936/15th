'''
	игра "Пятнашки" - Стабильная консольная версия
	реализовано: новая игра, сохранить, восстановить
'''
import random
import os
import json
import time

class Display_msg:
	def display_pinup(self):
		print('CONGRATULATIONS! You are WIN!')
		print(' ')
		timeGameStop = time.time()
		timeGameTotal = timeGameStop - timeGameStart + timeGameTotalTemp
		disp_msg.display_game_over(count_move, timeGameTotal)
		#input('Нажмите Enter')
		os.system('cls')
		

	def display_help(self):
		"""отобразить инструкцию к игре на экран"""
		print('\n')
		print("+------------------------------------------------+")
		print("| Игра 'Пятнашки'                                |")
		print("|                                                |")
		print("| Соберите последовательнойть фишек от одного до |")
		print("| пятнадцати на игровом поле.                    |")
		print("|                                                |")
		print("| Управление:                                    |")
		print("| Пустое поле обозначено как '0'                 |")
		print("| Чтобы переместить 'фишку' на пустое поле,      |")
		print("| наберите цифру фишки на цифровой клавиатуре и  |")
		print("| подтвердите клавишей <Enter>                   |")
		print("| Ход сделан. Приятного времяприпровождения.     |")
		print("+------------------------------------------------+")
		print('\n')

	def display_menu_main(self):
		'''отображает сновное меню программы'''
		print('\n')
		print("============================")
		print("Меню:")
		print("----------------------------")
		print("[N]ew.......Новая игра")
		print("----------------------------")
		print("[H]elp......Помощь")
		print("[A]bout.....Об игре")
		print("----------------------------")
		print("[E]xit......Выход")
		print("============================")
		print('\n')

	def display_menu_game(self):
		'''отображает меню игры'''
		print('\n')
		print("============================")
		print("Меню:")
		print("----------------------------")
		print("[N]ew.......Новая игра")
		print("----------------------------")
		print("[S]ave......Сохранить игру")
		print("[R]estore...Загрузить игру")
		print("----------------------------")
		print("[Q]uit......Выход")
		print("============================")
		print('\n')
	
	def display_header(self):
		# отобразить заголовок окна с названием проги и версией
		print('Игра "Пятнашки" ver.06')

	def board_display(self, board):
		disp_msg.display_header() # отобразить заголовок окна с названием проги и версией
		
    	#отобразить игровую доску на экран - элементы String
		board_to_mon = []
		for item in board :
			s = str(item)
			if s == '0':
				s = " "
			if len(s) == 1:
				s = " " + s
			board_to_mon.append(s)

		#os.system('cls')
		print("\n")
		print("+-------------------+")
		print("|",board_to_mon[0], "|",board_to_mon[1], "|",board_to_mon[2], "|",board_to_mon[3], "|")
		print("+----+----+----+----+")
		print("|",board_to_mon[4], "|",board_to_mon[5], "|",board_to_mon[6], "|",board_to_mon[7], "|")
		print("+----+----+----+----+")
		print("|",board_to_mon[8], "|",board_to_mon[9], "|",board_to_mon[10], "|",board_to_mon[11], "|")
		print("+----+----+----+----+")
		print("|",board_to_mon[12], "|" ,board_to_mon[13], "|",board_to_mon[14], "|",board_to_mon[15], "|")
		print("+-------------------+")
		#print("\n")

	def display_trasparant_exit(self):
		print('\n')
		print ('+-----------------------------+')
		print ('| Игра завершена. Спасибо.    |')
		print ('+-----------------------------+')
		print('\n')
		print ('+-----------------------------+')
		print ('| (C) Копирайт                |')
		print ('| Контактная информация       |')
		print ('+-----------------------------+')
		print('\n\n\n\n\nНажмите любую клавишу')
		#time.sleep(4) # чистит экран через 4 сек.
		input('') #ожидает нажатие Enter от пользователя
		os.system('cls')

	def display_about(self):
		"""отобразить информацию о программе и разработчиках"""
		print('\n')
		print ('+--------------------------+')
		print ('| О программе:             |')
		print ('|                          |')
		print ('| Проба пера на Python3    |')
		print ('+--------------------------+')
		print('\n')

	def display_banner(self, banner_flag):
		#print('баннер работает?')
		if banner_flag == 's':
			print('Игра сохранена.')
		if banner_flag == 'r':
			print('Игра восстановлена.')
		if banner_flag == 'd':
			print(' Attention! (\___/) I do ')
			print("            (='.'=) not")
			print('            (")_(") understand.')
			print('\n')
			print('Для хода, используйте цифры.')
			
	def display_count_move(self, count_move):
		print('Кол-во ходов: ', count_move)
		
	def display_dont_understand(self, msg_str):
		'''отображает банер Ошибка меню'''
		#print('\n')
		print(' Attention! (\___/) I do ')
		print("            (='.'=) not")
		print('            (")_(") understand.')
		print('\n')
		print(msg_str)
		
	def display_game_over(self, count_move, timeGameTotal):
		print("============================")
		print('Игра завершена.')
		print("============================")
		print('Сделано ходов: ', count_move)
		print('----------------------------')
		print('Затрачено времени: ', int(timeGameTotal), 'сек.')
		print("============================")
		print('\n')
		input('Для продолжения, нажмите Enter')

class Game_15():
	def new_board(self):
		'''в List заливаю последовательность Integer 0..15'''
		self.board = []
		while len(self.board) < 16:
			item = random.randrange(16)
			if item not in  self.board:
				self.board.append(item)
		return self.board

	def board_move(self, board, choose_menu, count_move): #передаю доску и нажатую цифровую клавишу
		'''отрабатывает ход игрока'''
		
		index_num = board.index(int(choose_menu))

		if not index_num + 4 >= 16 :
			if board[index_num + 4] == 0:
				board[index_num + 4] = board[index_num]
				board[index_num] = 0
				count_move = count_move + 1

		if not(index_num - 1 == 3 or index_num - 1 == 7 or index_num - 1 == 11 or index_num - 1 == 15):
			if board[index_num - 1] == 0:
				board[index_num - 1] = board[index_num]
				board[index_num] = 0
				count_move = count_move + 1

		if board[index_num - 4] == 0:
			board[index_num - 4] = board[index_num]
			board[index_num] = 0
			count_move = count_move + 1

		if not(index_num + 1 == 4 or index_num + 1 == 8 or index_num + 1 == 12 or index_num + 1 > 15):
			if board[index_num + 1] == 0:
				board[index_num + 1] = board[index_num]
				board[index_num] = 0
				count_move = count_move + 1
		
		#выполнить проверку на отсортировку массива
		if board == [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
			disp_msg.display_pinup()
		
		return count_move
		#disp_msg.board_display(board)
		#disp_msg.display_count_move(count_move)

	def game_save(self, board, count_move, timeGameTotal):
		json_data = json.dumps({'board':board, 'count_move':count_move, 'timeGameTotal':timeGameTotal})
		file = open('savegame.txt', 'w')
		file.write(json_data)
		file.close()
		#print('Игра сохранена.')

	def game_restore(self):
		file = open('savegame.txt', 'r')
		json_data = file.read()
		file.close()
		data = json.loads(json_data)
		
		board = data['board']
		count_move = data['count_move']
		timeGameTotalTemp = data['timeGameTotal']
		
		return board, count_move, timeGameTotalTemp

if __name__ == '__main__':
	os.system('cls')
	disp_msg = Display_msg()
	gm = Game_15()

	#time_stop = 0.0
	#time_start = 0.0
	disp_msg.display_header()
	while True: #отработка Главного меню		
		disp_msg.display_menu_main() #отображает основное меню
		choose_menu = input('Главное меню ==> ')
		os.system('cls')

		if choose_menu.lower() == 'e': # выход из программы
			disp_msg.display_trasparant_exit()
			break
		elif choose_menu.lower() == 'n': # новая игра
			board_new = gm.new_board() # генерим случайную доску
			count_move = 0
			choose_move = ''
			timeGameTotalTemp = 0.0
			timeGameStart = time.time()
			while True: #отработка меню Игры - ход игрока
				os.system('cls')
				disp_msg.board_display(board_new) # отображаем доску
				disp_msg.display_count_move(count_move) #кол-во ходов
				disp_msg.display_banner(choose_move) # отображает баннер на действия юзера
				disp_msg.display_menu_game() #отображает меню игры
				choose_move = input('ход игрока ==> ')
				os.system('cls')

				if choose_move.lower() == 'q':
					
					timeGameStop = time.time()
					timeGameTotal = timeGameStop - timeGameStart + timeGameTotalTemp
					disp_msg.display_game_over(count_move, timeGameTotal)
					os.system('cls')
					break # завершение текущей игры
				elif choose_move.lower() == 's': #  save game
					timeGameStop = time.time()
					timeGameTotal = timeGameStop - timeGameStart
					gm.game_save(board_new, count_move, timeGameTotal)
				elif choose_move.lower() == 'r': # restore game
					board_new, count_move, timeGameTotalTemp = gm.game_restore()
				elif choose_move in str([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]): #отрабатывает ход игрока
					count_move = gm.board_move(board_new, choose_move, count_move)
				elif choose_move.lower() == 'n':
					count_move = 0
					board_new = gm.new_board() # генерим случайную доску
				elif choose_move.lower() == 'w':
					#os.system('cls')
					disp_msg.display_pinup()
					input()
					os.system('cls')
					break # завершение текущей игры					
				else:
					choose_move = 'd'

		elif choose_menu.lower() == 'h': # помощь по игре
			disp_msg.display_header()
			disp_msg.display_help()
		elif choose_menu.lower() == 'a': # инфориация о программе и разрабе
			disp_msg.display_header()
			disp_msg.display_about()
		else:
			msg_str = 'Для выбора меню,\nиспользуйте начальные буквы\nиз [к]вадратных скобок,\nбез учета регистра.'
			disp_msg.display_dont_understand(msg_str)
