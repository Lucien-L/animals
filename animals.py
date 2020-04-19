class Animal:
  def __init__(self, view, name, weight, voice):
    self.weight = weight
    self.voice = voice
    self.name = name    
    self.view = view
  def get_voice(self):
    return str(self.voice)
  def present(self):
    print(self.name+" с весом "+str(self.weight)+ " кг")
  def give_eat(self):
    print ("накормил", self.name)
class egg_bearing(Animal):
  def give_effect(self):
    return 'принес яица'
class dairy(Animal):
  def give_effect(self):
    return 'принес молока'
class woolen(Animal):
  def give_effect(self):
    return 'постриг шерсть'
tet = 0    

farm = []
new_animal = egg_bearing('гусь', 'Серый', 10, 'га_га_га')

farm.append(new_animal)
new_animal = egg_bearing('гусь', 'Белый', 10, 'га_га_га')
farm.append(new_animal)
farm.append(dairy('корова', 'Манька', 200, 'мууу'))
farm.append(woolen('овца', 'Барашек', 10, 'беее'))
farm.append(woolen('овца', 'Кудрявый', 10, 'беее'))
farm.append(egg_bearing('курица', 'Ко_Ко', 10, 'кудахтает'))
farm.append(egg_bearing('курица', 'Кукареку', 10, 'кудахтает'))
farm.append(dairy('козы', 'Рога', 10, 'меее'))
farm.append(dairy('козы', 'Копыта', 10, 'меее'))
farm.append(egg_bearing('утка', 'Кряква', 10, 'кря_кря'))
tet_1 = farm[0]
for animal in farm:
  animal.present()
  animal.give_eat()
  a=animal.voice
  b=animal.weight
  tet +=b
  if tet_1.weight <b:
    tet_1 = animal
  print(a)
  print(animal.give_effect())
print(tet)
print(tet_1.weight, ' ', tet_1.view)
