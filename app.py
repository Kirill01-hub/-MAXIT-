import random

#Создание игрового поля 3x3 в котором содержатся рандомные цифры от 1 до 9.
def create_field():
    field = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    return field

#Вывод игрового поля.
def print_field(field):
  for row in field:
    print('  '.join(str(x) for x in row))

#Получает ход от игрока и проверяет его на корректность.
def player_move(player_numbr, field):
  while True:
    print(f"Игрок {player_numbr}, ваш ход.")
    try:
      row, col = map(int, input("Введите координаты хода (столбец, строка): ").split())
      col -= 1  
      row -= 1
      if 0 <= col <= 2 and 0 <= row <= 2 and field[col][row] != 0:
        return col, row
      else:
        print("Некорректный ход, попробуйте заново.")
    except ValueError:
      print("Некорректный ввод, вам нужно ввести два числа через пробел.")
      
#Проверка окончена игра или нет.
def game_over(field):
        return not any(cell != 0 for row in field for cell in row)

#Запуск игры.
def play_maxit():
  field = create_field()
  player1_score = 0
  player2_score = 0
  current_player = 1

  print("Игра Максит!")
  print_field(field)

  while not game_over(field):
    col, row = player_move(current_player, field)
    if current_player == 1:
      player1_score += field[col][row]
    else:
      player2_score += field[col][row]
    field[col][row] = 0
    
    print_field(field)
    
    if current_player == 1:
      current_player = 2
    else:
      current_player = 1

  print('''"Игра окончена!"''')
  print(f"Счет: Игрок 1 - {player1_score}, Игрок 2 - {player2_score}")

  if player1_score > player2_score:
    print("Победил Игрок 1!")
  elif player1_score < player2_score:
    print("Победил Игрок 2!")
  else:
    print("Ничья, победила дружба!")

play_maxit()
