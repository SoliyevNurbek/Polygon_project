import circle as aylana
import rectangle as turburchak
import square as kvadrat
import triangle as uchburchak

circl=aylana.Circle(5)
circl_isvalid=circl.is_valid()
circl_diametr=circl.diameter()
circl_circum=circl.circumference()
circl_area=circl.area()

rectan=turburchak.Rectangle(4,5)
rectan_isvalid=rectan.is_valid()
rectan_perim=rectan.perimeter()
rectan_area=rectan.area()

squar=kvadrat.Square(7)
squar_isvalid=squar.is_valid()
squar_area=squar.area()
squar_perim=squar.perimeter()

trian=uchburchak.Triangle(4,3,5)
trian_isvalid=trian.is_valid()
trian_gettype=trian.get_type()
trian_perim=trian.perimeter()
trian_area=trian.area()