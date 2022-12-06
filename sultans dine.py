#ROZA (er mane ki ? )
class SultansDine: ##can write cls instead of sultansdine
  tnb = 0
  sl= 0 #full price
  lis= []

  def __init__(self, br):
    self.br= br
    SultansDine.tnb+= 1
    SultansDine.lis.append(self)

  def sellQuantity(self, quantity):
    if quantity < 10:
      self.sl= quantity * 300
    elif quantity < 20:
      self.sl= quantity * 350
    else:
      self.sl= quantity * 400
    SultansDine.sl+= self.sl #allover

  @classmethod
  def details(cls):
    print('Total Number of branch(s):', cls.tnb)
    print('Total Sell:', cls.sl, 'Taka')
    if len(SultansDine.lis)!=0 :
      for i in SultansDine.lis:
        print(f'Branch Name: {i.br}, Branch Sell: {i.sl} Taka')#notice
        print(f'Branch consists of total sell\'s: {round((i.sl / SultansDine.sl)*100, 2)}%')

  def branchInformation(self):
    print('Branch Name:', self.br)
    print('Branch Sell:', self.sl, 'Taka')

SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()