class Laptop:
    Price = 0
    Processor = ""
    Ram = ""

hp = Laptop()
dell = Laptop()
lenovo = Laptop()

hp.Price = 50000
hp.Processor = "i5"
hp.Ram = "8GB"

dell.Processor = "i5"
dell.Ram = "8GB"
dell.Price = 50000

lenovo.Processor = "i5"
lenovo.Price = 50000
lenovo.Ram = "8GB"

print(hp.Price)
print(lenovo.Ram)
print(dell.Processor)
