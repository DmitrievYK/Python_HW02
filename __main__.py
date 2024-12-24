import SW_63, SW_64, HW_51, HW_52, HW_53



if __name__ == "__main__":
    SW_63.check_date(input('Введите год: '))
    SW_64.play_game()
    HW_51.check_date('13.05.2011')
    positions = [1, 3, 5, 7, 2, 4, 6, 8]
    print(HW_52.queens_position(positions))
    print(HW_53.generate_positions())


