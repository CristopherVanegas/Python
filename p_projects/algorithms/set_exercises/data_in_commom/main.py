# this code search for the commom items in between the sets 

class Main: 
    a = [1, 2, 3, 4, 5, 6, 7] 
    b = [6, 7, 8, 9, 10, 11, 12] 

    def __init__(self, a, b): 
        self.a = a 
        self.b = b 


    def search_commom_items(set_a, set_b):
        commom = []
        for x in set_a: 
            index = x

            for x in set_b: 
                if index == x: 
                    commom.append(x) 
        return commom 


if __name__ == '__main__': 
    print(f'>>> Commom Items: {Main.search_commom_items(Main.a, Main.b)}') 


