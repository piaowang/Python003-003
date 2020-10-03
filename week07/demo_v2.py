
'''具体要求：
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。

猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。

动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

'''
from abc import  abstractmethod


class  Zoo():

    def __init__(self,name):

        self.name =name
        #print(self.name)
        self.__animal_list = []
        self.__animal_type = []
    def add_animal(self, animal):
        self.__animal_type.append(animal.__class__.__name__)
        #setattr(self, animal.__class__.__name__, None)
        if animal.name not in self.__animal_list:
            self.__animal_list.append(animal.name)
            print(f'{animal.name}  添加成功.')
        else:
            raise Exception(f'{animal.name} 已经添加过了.')

    def __getattr__(self, item):
        #print(a)
        if item in self.__animal_type:
          print('动物园有这种动物')
        else:
            print('动物园没有这种动物')



class Animal():
    @abstractmethod
    def __init__(self,name,ctype,body,nature):
        self.name = name  # 名称
        self.ctype = ctype   #类型
        self.body = body     #体型
        self.nature = nature #性格
        self.is_ferocity =bool(
            self.ctype == '食肉' and
            self.body >= '中等' and
            self.nature == '凶猛'
        ) #是否凶猛

class Cat(Animal):
    def __init__(self, name, catagory, body, nature):
        super().__init__(name, catagory, body, nature)


class Dog(Animal):
    #print('It ia a dog')
    def __init__(self, name, catagory, body, nature):
        super().__init__(name, catagory, body, nature)



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('大花猫 2', '食肉', '小', '温顺')
    cat3 = Dog('大狗 2', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)
    #z.add_animal(cat2)
    print(cat1.is_ferocity)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    have_cat = hasattr(z, 'Cat1')