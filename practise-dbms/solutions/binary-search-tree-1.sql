-- Database Used: BST(bst.sql)

select N, if (N in (select P from BST), if (P <> "null", "Inner", "Root"), "Leaf")
from BST
order by N;