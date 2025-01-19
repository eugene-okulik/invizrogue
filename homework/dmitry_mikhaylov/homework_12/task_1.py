class Flowers:
    def __init__(self, name, color, price):
        self.__name = name
        self.__color = color
        self.__price = price

    def __lt__(self, other):
        return self.price < other.price

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return (f'Name: {self.__name}, '
                f'Color: {self.__color}, '
                f'Price: {self.__price}, ')

    def __repr__(self):
        return (f'--> Name: {self.__name}, '
                f'Color: {self.__color}, '
                f'Price: {self.__price}, ')


class Rose(Flowers):
    def __init__(self, name, color, stem_length, thorns, cluster, price):
        super().__init__(name, color, price)
        self.__stem_length = stem_length
        self.__thorns = thorns
        self.__cluster = cluster
        self.__wilting = 10

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def thorns(self):
        return self.__thorns

    @property
    def cluster(self):
        return self.__cluster

    @property
    def wilting(self):
        return self.__wilting

    def __str__(self):
        return (super().__str__() +
                f'Stem length: {self.__stem_length}, '
                f'Have thorns: {self.__thorns}, '
                f'Is cluster: {self.__cluster}')

    def __repr__(self):
        return (super().__repr__() +
                f'Stem length: {self.__stem_length}, '
                f'Have thorns: {self.__thorns}, '
                f'Is cluster: {self.__cluster}\n')


class Orchid(Flowers):
    def __init__(self, name, color, leaf_type, lip_color, price):
        super().__init__(name, color, price)
        self.__leaf_type = leaf_type
        self.__lip_color = lip_color
        self.__wilting = 25

    @property
    def leaf_type(self):
        return self.__leaf_type

    @property
    def lip_color(self):
        return self.__lip_color

    @property
    def wilting(self):
        return self.__wilting

    def __str__(self):
        return (super().__str__() +
                f'Leaf type: {self.__leaf_type}, '
                f'Lip color: {self.__lip_color}')

    def __repr__(self):
        return (super().__repr__() +
                f'Leaf type: {self.__leaf_type}, '
                f'Lip color: {self.__lip_color}\n')


class Narcissus(Flowers):
    def __init__(self, name, color, center_color, stem_length, price):
        super().__init__(name, color, price)
        self.__stem_length = stem_length
        self.__center_color = center_color
        self.__wilting = 15

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def center_color(self):
        return self.__center_color

    @property
    def wilting(self):
        return self.__wilting

    def __str__(self):
        return (super().__str__() +
                f'Center color: {self.__center_color}, '
                f'Stem length: {self.__stem_length}')

    def __repr__(self):
        return (super().__repr__() +
                f'Center color: {self.__center_color}, '
                f'Stem length: {self.__stem_length}\n')


class Gladiola(Flowers):
    def __init__(self, name, color, flower_count, price):
        super().__init__(name, color, price)
        self.__flower_count = flower_count
        self.__wilting = 15

    @property
    def flower_count(self):
        return self.__flower_count

    @property
    def wilting(self):
        return self.__wilting

    def __str__(self):
        return (super().__str__() +
                f'Flower count: {self.__flower_count}')

    def __repr__(self):
        return (super().__repr__() +
                f'Flower count: {self.__flower_count}\n')


class Lily(Flowers):
    def __init__(self, name, color, flower_count, stem_length, price):
        super().__init__(name, color, price)
        self.__flower_count = flower_count
        self.__stem_length = stem_length
        self.__wilting = 14

    @property
    def flower_count(self):
        return self.__flower_count

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def wilting(self):
        return self.__wilting

    def __str__(self):
        return (super().__str__() +
                f'Flower count: {self.__flower_count}, '
                f'Stem length: {self.__stem_length}')

    def __repr__(self):
        return (super().__repr__() +
                f'Flower count: {self.__flower_count}, '
                f'Stem length: {self.__stem_length}\n')


class Bouquet:
    def __init__(self):
        self.__price = 0
        self.__composition = []
        self.__avg_wilting = 0

    def add_flower(self, flower):
        self.__composition.append(flower)
        self.__price += flower.price
        self.__avg_wilting = (
            round(self.__get_wilting() / len(self.__composition), 2))

    def property_find(self, prop, value):
        for flower in self.__composition:
            if hasattr(flower, prop):
                if prop == 'name' and flower.name == value:
                    return flower
                elif prop == 'color' and flower.color == value:
                    return flower
                elif prop == 'price' and flower.price == value:
                    return flower
                elif prop == 'wilting' and flower.wilting == value:
                    return flower
                elif (prop == 'flower_count'
                      and flower.flower_count == value):
                    return flower
                elif (prop == 'stem_length'
                      and flower.stem_length == value):
                    return flower
                elif (prop == 'leaf_type'
                      and flower.leaf_type == value):
                    return flower
                elif (prop == 'lip_color'
                      and flower.lip_color == value):
                    return flower
                elif (prop == 'center_color'
                      and flower.center_color == value):
                    return flower
                elif (prop == 'cluster'
                      and flower.cluster == value):
                    return flower
                elif (prop == 'thorns'
                      and flower.thorns == value):
                    return flower

    def __get_wilting(self):
        value = 0
        for flower in self.__composition:
            value += flower.wilting
        return value

    @property
    def avg_wilting(self):
        return self.__avg_wilting

    @property
    def price(self):
        return self.__price

    @property
    def composition(self):
        return self.__composition

    def __str__(self):
        return f'{self.__composition}'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__composition}'


rose_1 = Rose('rose', 'red', 30, True, False, 100)
gladiola_1 = Gladiola('gladiola', 'white', 5, 150)
narcissus_1 = Narcissus('narcissus', 'yellow', 'red', True, 200)

bouquet = Bouquet()
bouquet.add_flower(gladiola_1)
bouquet.add_flower(narcissus_1)
bouquet.add_flower(rose_1)

print(bouquet.price)
print(bouquet.avg_wilting, 2)

print(rose_1)

print(f'Found by color = red: {bouquet.property_find('color', 'red')}')
print(f'Found by flower_count = 5: {bouquet.property_find('flower_count', 5)}')
print(f'Unsorted: {bouquet.composition}')
print(f'Sorted by name: {
    sorted(bouquet.composition, key=lambda composition: composition.name)
}')
print(f'Sorted by price: {sorted(bouquet.composition)}')
