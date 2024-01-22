from typing import List, Callable, TypeVar 

dollars = ["32$", "15$", "12$", "17$", "20$"] 


# Usando typing modules 
E = TypeVar('E') 
R = TypeVar('R') 
A = TypeVar('A')

def map_f(iterable: List[E], func: Callable[[E], R]) -> List[R]: 
    mapped: List[R] = [] 
    for e in iterable: 
        mapped.append(func(e)) 
    return mapped 


def filter_f(iterable: List[E], func: Callable[[E], bool]) -> List[E]: 
    filtered: List[E] = [] 
    for e in iterable: 
        if func(e): 
            filtered.append(e) 
    return filtered 

def acum(iterable: List[E], func: Callable[[A, E], A], acum: A) -> List[E]: 
    for e in iterable: 
        acum = func(acum, e)
    return acum 
    

prices = map_f(dollars, lambda dollar: int(dollar[0:-1])) 
expensive = filter_f(prices, lambda price: price >= 20) 
total = acum(prices, lambda acum, price: acum + price, 0)
print(prices) 
print(expensive)  
print(total)

