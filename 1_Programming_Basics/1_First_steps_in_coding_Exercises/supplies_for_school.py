# nr_packs_pens = int(input())
# nr_packs_markers = int(input())
# liters_board_cleaning_detergent = int(input())
# discount_rate = int(input())/100
#
# pack_pens_price = 5.80
# pack_markers_price = 7.20
# liter_board_cleaning_detergent_price = 1.20
#
# total_pen = nr_packs_pens * pack_pens_price
# total_markers = nr_packs_markers * pack_markers_price
# total_detergent = liters_board_cleaning_detergent * liter_board_cleaning_detergent_price
#
# total_price = total_pen + total_markers + total_detergent
# discount = total_price * discount_rate
#
# money_needed = total_price - discount
#
# print(money_needed)

#kato go napravq po po-kusiq nachin, vtoriq test izliza s mn cifri sled zapetaqta, neshto se burka nqkude (58.68000000000001),
# no puk judge go priema
nr_packs_pens = int(input())
nr_packs_markers = int(input())
liters_board_cleaning_detergent = int(input())
discount_rate = int(input())/100

pack_pens_price = 5.80
pack_markers_price = 7.20
liter_board_cleaning_detergent_price = 1.20

money_needed = (nr_packs_pens * pack_pens_price + nr_packs_markers * pack_markers_price +
liters_board_cleaning_detergent * liter_board_cleaning_detergent_price) * (1 - discount_rate)

print(money_needed)