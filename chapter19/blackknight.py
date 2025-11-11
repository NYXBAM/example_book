class BlackKnight:
    def __init__(self):
        self.members = ['arm', 'second arm',
                        'leg', 'second leg']
        self.phrases = ['Tis but a scratch.',  
                        'It\'s just a flesh wound.',
                        'I am invincible!',
                        'Alright, we’ll call it a draw.'] 
    @property
    def member(self):
        print('Next member')
        return self.members[0]
    
    @member.deleter
    def member(self):
        text = 'Black Knight (lost {})\n-- {}'
        print(text.format(self.members.pop(0), self.phrases.pop(0)))
        
    
knight = BlackKnight()



del knight.member
del knight.member
del knight.member
del knight.member
