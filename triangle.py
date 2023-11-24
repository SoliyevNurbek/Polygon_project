from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        return True if self.a>0 and self.b>0 and self.c>0 and (self.a+self.b)>self.c and (self.a+self.c)>self.b and (self.b+self.c)>self.a else False 
    
    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.is_valid():
            return "Teng yonli" if ((self.a==self.b and self.a!=self.c) or (self.a==self.c and self.a!=self.b) or (self.c==self.b and self.c!=self.a)) else "Teng tomonli" if((self.a==self.b) and (self.a==self.c) and (self.c==self.b))  else "Turli tomonli"
        else :
            return "Error Triangle"
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        return self.a+self.b+self.c if self.is_valid() else 0

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        p=(self.a+self.b+self.c)/2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)) if self.is_valid() else 0
