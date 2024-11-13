from modules.module_one import module_one_hello, numbers_sum
from modules.module_two import module_two_hello, numbers_diff

from my_package.part_one.po_file_one import po_one_show_where
from my_package.part_one.po_file_two import po_two_show_where

from my_package.part_two.pt_file_one import pt_one_show_where 
from my_package.part_two.pt_file_two import pt_two_show_where

from my_package.part_two.directory.file_one import file_one_show_where 
from my_package.part_two.directory.file_two import file_two_show_where


module_one_hello()
numbers_sum(100, 25)

module_two_hello()
numbers_diff(125, 30)

po_one_show_where()
po_two_show_where()

pt_one_show_where()
pt_two_show_where()

file_one_show_where()
file_two_show_where()
