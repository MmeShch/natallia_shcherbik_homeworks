# 3) Задан список слов, в которых встречается символ ‘_’ подчеркивание).
# Создать новый список, в котором символ подчеркивания в словах ‘_’ заменить символо ‘ ‘ (пробел).
# l = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]

l = [ "ab_cd_e", "abc", "a_b_c", "a__bc_d_", "__" ]
new_l = []
for x in l:
    new_l.append(x.replace('_', ' '))
print(new_l)
