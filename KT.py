class User:
  count = 0
  def __init__(self, name: str, login: str, password:str, grade: int):
    if grade <= 0:
            raise ValueError("grade должен быть строго положительным")
    self.name = name
    self.__login = login
    self.__password = password
    self.__grade = grade
    type(self).count += 1

  def show_info(self):
    print(f'{self.name} - {self.login}')

  def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self.__grade == other.__grade

  def __lt__(self, other):
      if not isinstance(other, User):
          return NotImplemented
      return self.__grade < other.__grade

  def __gt__(self, other):
      if not isinstance(other, User):
          return NotImplemented
      return self.__grade > other.__grade

  @property
  def login(self):
      return self.__login

  @login.setter
  def login(self, value):
      print("Невозможно изменить логин!")

  @property
  def password(self):
      return '*' * len(self.__password)

  @password.setter
  def password(self, value):
      self.__password = value

  @property
  def grade(self):
      return "Неизвестное свойство grade"

  @grade.setter
  def grade(self, value):
      print("Неизвестное свойство grade")

class SuperUser(User):
  count = 0
  def __init__(self, name: str, login: str, password:str, role: str, grade: int):
    self.__role = role
    super().__init__(name, login, password, grade)

  def show_info(self):
      super().show_info()
      print(f'   роль: {self.role}')

  @property
  def role(self):
      return self.__role

  @role.setter
  def role(self, value):
      self.__role = value
    
   

user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Star'
user1.password = 'Pa$$w0rd'

print(user3.name)
print(user2.password)
print(user2.login)

user2.login = 'geo'

print(user1.grade)
admin.grade = 10
