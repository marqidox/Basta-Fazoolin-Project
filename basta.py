from functools import reduce
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def convert_start_time(self):
    if self.start_time in range(13, 24):
      new_start_time = self.start_time - 12
      return str(new_start_time) + "pm"
    else:
      return "{start_time}am".format(start_time=self.start_time)

  def convert_end_time(self):
    if self.end_time in range(13, 24):
      new_end_time = self.end_time - 12
      return str(new_end_time) + "pm"
    else:
      return "{end_time}am".format(end_time=self.end_time)

  def __repr__(self):
    return "You can order from the {menu} menu from {start} to {end}.".format(menu=self.name, start=self.convert_start_time(), end=self.convert_end_time())

  def calculate_bill(self, purchased_items):
    sumTwo = lambda a,b : a+b
    prices = [self.items[item] for item in purchased_items]
    print("Your {menu} order will cost ${total_price}.".format(total_price=reduce(sumTwo, prices), menu=self.name))

brunch = Menu('brunch', {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, 11, 16)

early_bird = Menu('early bird', {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 15, 18)

dinner = Menu('dinner', {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 17, 23)

kids = Menu('kids', {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 11, 21)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  def __repr__(self):
    return 'This franchise is located at {address}.'.format(address=self.address)
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if menu.start_time <= time and menu.end_time >= time:
        available_menus.append(menu)
    for menu in available_menus:
      print(menu)
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

menu_times = lambda m1, m2, m3, m4 : '{m1}\n{m2}\n{m3}\n{m4}'.format(m1=m1, m2=m2, m3=m3, m4=m4)
all_menu_times = menu_times(brunch, early_bird, dinner, kids)

print("")
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
basta_fzoolin_with_my_heart = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepas_menu = Menu('arepas', {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 10, 20)
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])
take_a_arepa = Business('Take a Arepa', [arepas_place])
