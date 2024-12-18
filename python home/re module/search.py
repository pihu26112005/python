import re
text = '''
Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. 
Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. 
It became a tropical disturbance on 2 March, 
and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, 
with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph),
 and a central atmospheric pressure of 945 hPa (27.91 inHg). 
As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear,
 and became a post-tropical cyclone on 7 March
Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi haiaiinaiiiiiiiiiiii '''

pattern = r"[A-Z]+yclodne"

match = re.search(pattern, text)
print(match)