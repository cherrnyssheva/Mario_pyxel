import time
Flag = False
current = time.time()
fail = current+2
while time.time() < fail:
    Flag = False
Flag = True
if Flag == True:
    print('123')