from time import sleep
from subprocess import check_output

DeviceName = "AT Translated Set 2 keyboard" #Find your xinput device using the command "xinput list" then paste it here

def DeviceFind() -> int: #Find xinput device id by using --id-only
	DEVICE_ID = int(check_output(f'xinput list --id-only "{DeviceName}"', shell=True))
	print(f"Device found = {DEVICE_ID}")
	return DEVICE_ID

def CheckState(DeviceID: int) -> int: #Checks the status of xinput device. Getting the value with grep. I'm not very good at grep yet...
	STATE = int(check_output(f'xinput --list-props {DeviceID} | grep "Device Enabled" | grep -Eo "[0-9]+$"', shell = True))
	print(f"Device state = {STATE}")
	return STATE

def RunSwitcher(DeviceState: int, DeviceID: int) -> None: #Simple switch
	if DeviceState == 1:
		check_output(f'xinput disable {DeviceID}', shell=True)
		print(f"{DeviceName} DISABLED")
	elif DeviceState == 0:
		check_output(f'xinput enable {DeviceID}', shell=True)
		print(f"{DeviceName} ENABLED")
	else:
		print("Something went wrong...")

if __name__ == "__main__": #Entry point
	DEVICE_ID = DeviceFind()
	DEVICE_STATE = CheckState(DEVICE_ID)
	RunSwitcher(DEVICE_STATE, DEVICE_ID)
	sleep(5)
