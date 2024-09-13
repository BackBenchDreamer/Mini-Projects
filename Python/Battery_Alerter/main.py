import psutil

battery_status = psutil.sensors_battery()
is_charging = battery_status.power_plugged
charge_level = battery_status.percent

#print(charge_level, is_charging)

if charge_level <= 30 and not is_charging:
    
    # pip install py-notifier
    # pip install win10toast
    from pynotifier import Notification

    Notification(
        title="Low Battery Warning",
        description=f"Only {charge_level}% battery remaining!",
        duration=5,  # Duration in seconds
        
    ).send()
