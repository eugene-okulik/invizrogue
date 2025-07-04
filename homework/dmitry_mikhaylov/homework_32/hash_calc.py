from Crypto.Hash import SHA3_256
import time

count = 0
try:
    while True:
        data = f"{count}---{count}".encode("utf-8")
        hash_obj = SHA3_256.new(data)
        hash_result = hash_obj.hexdigest()

        print(hash_result)

        count += 1
        time.sleep(1)
except KeyboardInterrupt:
    print("Прерывание")
