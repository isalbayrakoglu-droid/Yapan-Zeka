import time

print("Python dünyasına hoş geldin!")
time.sleep(1)

isim = input("Adın ne? ")

print("\nHazırlan", end="")
for i in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)

print(f"\n\nMerhaba {isim}! 🎉")
print("Bu senin ilk Python programın!")
print("Bundan sonrası tamamen hayal gücüne kalmış… 😎")
