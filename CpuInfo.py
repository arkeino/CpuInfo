import psutil

cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
cpu_freq = psutil.cpu_freq(percpu=True)
virtual_mem = psutil.virtual_memory()
swap = psutil.swap_memory()

print("CPU USAGE:")

for i, (percent, freq) in enumerate(zip(cpu_percent, cpu_freq), start=1):
    print(f"Core {i} : {percent}% Frequency: {freq.current} MHz")

print("\nVirtual Memory:")
print(f"Total: {virtual_mem.total / (1024**3):.2f} GB")
print(f"Used: {virtual_mem.used / (1024**3):.2f} GB")
print(f"Swap total: {swap.total / (1024**3):.2f} GB")
print(f"Swap Used: {swap.used / (1024**3):.2f} GB")

network = psutil.net_io_counters()
print("\nNetwork info:")
print(f"Bytes received: {network.bytes_recv}")
print(f"Bytes sent: {network.bytes_sent}")

try:
    temperature = psutil.sensors_temperatures()
    if temperature:
        print("\nTemperature:")
        for name, entries in temperature.items():
            for entry in entries:
                print(f"{name}: {entry.current}°C")
    else:
        print("\nTemperature refused")
except AttributeError:
    print("\nTemperature unavailable.")

disk = psutil.disk_usage("/")
print("\nDisk info:")
print(f"Total Disk space: {disk.total / (1024 **3):.2f}GB")
print(f"Used disk space: {disk.used / (1024 **3):.2f}GB")
print(f"Free disk space: {disk.free / (1024 **3):.2f}GB")
