# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.3

# Description:
#   使用取名机器
# ------------------------(max to 80 columns)-----------------------------------


from pkg_naming.naming_machine import *
#from pkg_naming.naming_machine import pick_a_full_name


# Generate a new full name
new_name = pick_a_full_name()
print(new_name)

# Generate a new boy's name
sex = 1
new_boy_name = pick_a_full_name_by_sex(sex)
print(new_boy_name)
