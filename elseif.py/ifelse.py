class cleaner:
    followers = 0
    def __init__(self, name: str ,address: str,colour:str, height : int=0,) -> None:
        self.name=name
        self.height=height
        self.addres=address
        self.colour=colour
    def display(self,subject_name):
        print(f"Hi , i am {self.name } and i tech {subject_name}")
    def followers_update (self,followers_update):
        self.followers += 1

cleaner_1=cleaner(name='sundy',height='6.1',address='maine', colour='black man')
cleaner_1.display("python")
cleaner_1.followers_update("payal")
print(cleaner_1.followers)

cleaner_2=cleaner(name='sundy',height='6.1',address='maine', colour='black man')
cleaner_2.followers_update("jenny")
print(cleaner_2.followers)