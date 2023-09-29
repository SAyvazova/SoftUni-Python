num = float(input())

while num < 1 or num > 100:
    num = float(input())

else: #nqma nujda ot else, zashtoto ako num se zadade v intervala, to while cikula priklyuchva i tazi stoynost e zapazena v
    #num i printa si raboti normalno
    print(f"The number {num} is between 1 and 100")

# reshenie lektor
# while True:
#     num = float(input())
#
#     if 1 <= num <= 100:
#         print(f"The number {num} is between 1 and 100")
#         break
