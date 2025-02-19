class Speaker:
   """
   Класс Speaker представляет собой абстрактный класс, который определяет интерфейс для объектов, которые могут отвечать на вопросы.
   """

   def __init__(self, SpeakerName):
       """
       Инициализирует объект Speaker с заданным именем.

       :param SpeakerName: Имя объекта Speaker.
       """
       self.name = SpeakerName

   def __getanswer(self):
       """
       Метод __getanswer является абстрактным и должен быть реализован в подклассах.
       """
       raise NotImplementedError("You must implement this method")

   def answer(self):
       """
       Метод answer является абстрактным и должен быть реализован в подклассах.
       """
       raise NotImplementedError("You must implement this method")




class Kitty(Speaker):
   """
   Класс Kitty представляет собой подкласс класса Speaker и реализует методы для отслеживания количества ответов "да" и "нет".
   """

   def __init__(self, SpeakerName):
       """
       Инициализирует объект Kitty с заданным именем.

       :param SpeakerName: Имя объекта Kitty.
       """
       super().__init__(SpeakerName)
       self.__count_yes = 0
       self.__count_no = 0

   def __getanswer(self):
       """
       Метод __getanswer возвращает случайный ответ "да" или "нет" и увеличивает соответствующий счетчик.

       :return: Случайный ответ "да" или "нет".
       """
       if self.__count_no < self.__count_yes:
           self.__count_no += 1
           return "meow-meow"
       else:
           self.__count_yes += 1
           return "moore-moore"

   def number_no(self):
       """
       Метод number_no возвращает количество ответов "нет".

       :return: Количество ответов "нет".
       """
       return self.__count_no

   def number_yes(self):
       """
       Метод number_yes возвращает количество ответов "да".

       :return: Количество ответов "да".
       """
       return self.__count_yes

   def to_answer(self):
       """
       Метод to_answer возвращает случайный ответ "да" или "нет".

       :return: Случайный ответ "да" или "нет".
       """
       answer = self.__getanswer()
       return answer



tk = Kitty("MyKitty")
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f"{tk.name} says 'yes': {tk.number_yes()} times\
 and 'no': {tk.number_no()} times.")
