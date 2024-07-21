from threading import Thread
# from time import sleep
from colorama import  Fore
from time import sleep

class Knight(Thread):
    enemies = 100
    day = 0

    def __init__(self, name, power, color):
        self.color = color
        self.power = int(power)
        super().__init__(name=name)

    def run(self):
        while 0 != self.enemies:
            if self.day == 0:
                print(self.color + f"{self.name}, на нас напали!")
                sleep(1)
                self.day += 1
            else:
                for i in range(0, 100, self.power):
                    self.enemies -= self.power
                    if self.enemies != 0:
                        print(
                            self.color + f"{self.name} сражается {self.day} дней(дня), осталось {self.enemies} воинов.")
                        sleep(1)
                        self.day += 1
                    else:
                        print(self.color + f"{self.name} одержал победу спустя {self.day}  дней(дня)!")
                        continue


first_knight = Knight('Sir Lancelot', 10, Fore.RED)
second_knight = Knight("Sir Galahad", 20, Fore.CYAN)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
