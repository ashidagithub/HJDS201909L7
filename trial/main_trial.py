# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11.3

# Description:
#   使用取名机器
# ------------------------(max to 80 columns)-----------------------------------


#import pkg_naming.naming_machine as nm
from pkg_naming.naming_machine import pick_a_full_name, pick_a_full_name_by_sex

print('---Generate some full names---')
for idx in range(10):
    new_name = pick_a_full_name()
    print(new_name)

print('---Generate some girl''s names---')
sex = 2
for idx in range(30):
    new_name = pick_a_full_name_by_sex(sex)
    print(new_name)
