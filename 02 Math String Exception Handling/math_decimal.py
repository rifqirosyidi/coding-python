from decimal import Decimal as D

jumlah = D(0)
jumlah += D("0.1")
jumlah += D("0.1")
jumlah += D("0.1")
jumlah -= D("0.3")

print("ACCURATE", jumlah)

# this Result below is not what we wanted
print("NOT ACCURATE", .1 + .1 + .1 - .3)
