import psutil
import tkinter as tk
from tkinter import ttk

class CPUMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("CPU Monitor")

        self.label = ttk.Label(root, text="CPU Usages:")
        self.label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, length=200, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.start_button = ttk.Button(root, text="Start Monitoring", command=self.start_monitoring)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(root, text="Stop Monitoring", command=self.stop_monitoring)
        self.stop_button.pack(pady=10)

        self.is_monitoring = False
        self.monitor_interval = 1
        self.update_interval = 1000 #  1000 mili seconds = 1 seconds


    def update_cpu_usages(self):
       cpu_percentage = psutil.cpu_percent(interval=self.monitor_interval)
       self.progress_bar["value"]= cpu_percentage
       self.label["text"]= f"CPU usages : {cpu_percentage:.2f}%"
       if self.is_monitoring :
           self.root.after(self.update_interval,self.update_cpu_usages)

    def start_monitoring(self):
        if not self.is_monitoring:
            self.is_monitoring = True
            self.start_button["state"] = tk.DISABLED
            self.stop_button["state"] = tk.NORMAL
            self.update_cpu_usages()

    def stop_monitoring(self):
        if self.is_monitoring:
            self.is_monitoring = False
            self.start_button["state"] = tk.NORMAL
            self.stop_button["state"] = tk.DISABLED


if __name__ == "__main__":
    root = tk.Tk()
    app = CPUMonitor(root)
    root.mainloop()


