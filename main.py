class Object():
    def __init__(self, difficulty = 10, x = 0, y = 0):
        self.difficulty = difficulty
        self.manipulate_difficulty = difficulty/10
        self.strength = difficulty
        self.x = x
        self.y = y


    def move_to(self, x, y):
        r = ((self.x - x)**2 + (self.y - y)**2)**0.5
        self.x = x
        self.y = y
        manipulated = r*self.manipulate_difficulty
        return manipulated
    
    
    def print_stats(self):
        print('x, y:', self.x, self.y, 'strength:', self.strength)


class Aura(Object):
    element = None
    
    
    def __init__(self, difficulty = 5, x = 0, y = 0):
        super().__init__(difficulty, x, y)
        
        
    def transform(self, elem):
        element = elem


    def print_stats(self):
        print('x, y:', self.x, self.y, 'strength:', self.strength, 'elem:', self.elem)
        

class Nen():
    aura = 100
    passive_outflow = 1
    passive_production = 1
    

    def outflow(self, amount = 0):
        self.aura -= self.passive_outflow
        self.aura -= amount
        

    def production(self, amount = 0):
        self.aura += self.passive_production
        self.aura += amount


# control nen
class Ten(Nen):
    aura_around_body = 0
    
    
    def __init__(self):
        super().__init__()
        self.aura_around_body = self.aura
        self.passive_outflow /= 2
        
        
    def outflow(self, amount = 0):
        super().outflow(amount)
        self.aura_around_body = self.aura
        
    
    def production(self, amount = 0):
        super().production(amount)
        self.aura_around_body = self.aura
    

# hide nen
class Zetsu(Nen):
    def __init__(self):
        super().__init__()
        self.passive_outflow = 0
        self.passive_production /= 2


# Ten++, more control aura
class Ren(Ten):
    body_aura = {'arms': 0, 'legs': 0, 'torso': 0, 'head': 0}
    
    
    def __init__(self):
        super().__init__()
        self.whole_body_aura()
    
    
    def transfer_aura(self, to, amount):
        if amount >= self.aura_around_body:
            return 0
        
        need = self.aura_around_body - amount
        for i in self.body_aura:
            if i == to:
                self.body_aura[i] = amount
            else:
                self.body_aura[i] = need/(len(self.body_aura)-1)
                
                
    def whole_body_aura(self):
        for i in self.body_aura:
            self.body_aura[i] = self.aura_around_body/len(self.body_aura)
            
            
    def whole_body_changes(self, amount):
        one_amount = amount/len(self.body_aura)
        for i in self.body_aura:
            self.body_aura[i] += one_amount
        
        
    def outflow(self, amount = 0):
        before_aura = self.aura_around_body
        super().outflow(amount)
        changes = self.aura_around_body - before_aura
        self.whole_body_changes(changes)
    
    
    def production(self, amount = 0):
        before_aura = self.aura_around_body
        super().production(amount)
        changes = self.aura_around_body - before_aura
        self.whole_body_changes(changes)
    

# use aura, different types
class Hatsu(Ren):
    def __init__(self):
        super().__init__()
    
    
    # Enhancer - Усиление
    def enhant(self, obj, amount):
        obj.strength += amount
        self.outflow(amount)
        return obj
    
    
    # Transmuter - Трансформация
    def transmute(self, obj:Aura, elem):
        obj.elem = elem
        self.outflow(obj.manipulate_difficulty)
        return obj
    
    
    # Emitter - Выделение
    def emit(self, obj:Aura):
        self.outflow(obj.difficulty)
        return obj
    
    
    # Conjurer - Материализация
    def create(self, obj:Object):
        self.outflow(obj.difficulty)
        return obj
    
    
    # Manipulator - Манипуляция
    def manipulate(self, obj, x, y):
        m = obj.move_to(x, y)
        self.outflow(m)
        return obj


if __name__ == '__main__':
    hatsu = Hatsu()
    print(hatsu.aura, hatsu.body_aura)
    
    print('\n')
    
    obj = hatsu.create(Object())
    obj.print_stats()
    print(hatsu.aura, hatsu.body_aura)
    
    print('\n')
    
    obj = hatsu.manipulate(obj, 4, 4)
    obj.print_stats()
    print(hatsu.aura, hatsu.body_aura)
    
    print('\n')
    
    aura = hatsu.emit(Aura())
    aura = hatsu.transmute(aura, 'fire')
    aura = hatsu.enhant(aura, 10)
    aura.print_stats()
    print(hatsu.aura, hatsu.body_aura)
    
    print('\n')
    
    aura = hatsu.manipulate(aura, 4, 4)
    aura.print_stats()
    print(hatsu.aura, hatsu.body_aura)
