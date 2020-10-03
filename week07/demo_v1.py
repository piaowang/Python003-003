
'''具体要求：
背景：在使用 Python 进行《我是动物饲养员》这个游戏的开发过程中，有一个代码片段要求定义动物园、动物、猫、狗四个类。

这个类可以使用如下形式为动物园增加一只猫：

定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。

猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类。

动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。

'''
from abc import  abstractmethod

a = set()  # 存放动物名称，用来检验是否重复放入
b = set()  # 存放动物类型
class  Zoo():

    def __init__(self,name):

        self.name =name

        #print(self.name)
    @classmethod
    def add_animal(cls,name):
        name1 = type(name).__name__
        name2 = name.name
        print(name2)
        if name2 in b:
            print('此猫已经在动物园了，不用重复添加')
        else:
            b.add(name2)
            print(f'此动物'+name2+'已添加到动物园')
        print(name1)
        a.add(name1)

    def __getattr__(self, item):
        #print(a)
        if item in a:
          print('动物园有这种动物')
        else:
            print('动物园没有这种动物')
class Animal():
    @abstractmethod
    def __init__(self,ctype,body,nature):
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
        super().__init__( catagory, body, nature)
        self.name = name #名称
    #print('It ia a cat')

class D(Animal):
    #print('It ia a dog')
    pass



if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('大花猫 2', '食肉', '小', '温顺')

    print(cat1.is_ferocity)
    # 增加一只猫到动物园
    z.add_animal(cat1)
    z.add_animal(cat2)
    z.add_animal(cat2)

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')