from time import sleep
from subprocess import check_output

def KeyboardFind() -> int:
	DEVICE_ID = int(check_output('xinput list --id-only "AT Translated Set 2 keyboard"', shell=True))
	print(f"Клавиатура найдена, ID = {DEVICE_ID}")
	return DEVICE_ID

def CheckState(DeviceID: int) -> int:
	STATE = int(check_output(f'xinput --list-props {DeviceID} | grep "Device Enabled" | grep -Eo "[0-9]+$"', shell = True))
	print(f"Статус клавиатуры = {STATE}")
	return STATE

def RunSwitcher(DeviceState: int, DeviceID: int) -> None:
	if DeviceState == 1:
		check_output(f'xinput disable {DeviceID}', shell=True)
		print("Клавиатура ОТКЛЮЧЕНА.")
	elif DeviceState == 0:
		check_output(f'xinput enable {DeviceID}', shell=True)
		print("Клавиатура ВКЛЮЧЕНА")
	else:
		print("Что-то пошло не так...")

if __name__ == "__main__":
	DEVICE_ID = KeyboardFind()
	DEVICE_STATE = CheckState(DEVICE_ID)
	RunSwitcher(DEVICE_STATE, DEVICE_ID)
	sleep(5)
