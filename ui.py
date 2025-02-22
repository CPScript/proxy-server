import curses
from proxy_server import ProxyServer

class ProxyManagerUI:
    def __init__(self):
        self.proxy_server = ProxyServer()

    def main(self, stdscr):
        curses.curs_set(0)
        stdscr.nodelay(1) 

        while True:
            stdscr.clear()

            stdscr.addstr(0, 0, "Proxy Server Management", curses.A_BOLD)
            stdscr.addstr(2, 0, f"Uptime: {self.proxy_server.get_uptime()}")
            stdscr.addstr(3, 0, f"Connection Status: {self.proxy_server.connection_status()}")
            stdscr.addstr(5, 0, f"Public IP: {self.proxy_server.get_public_ip()}")
            stdscr.addstr(6, 0, f"Local IP: {self.proxy_server.get_local_ip()}")

            stdscr.addstr(8, 0, "Connect your device using this proxy:")
            stdscr.addstr(9, 0, "Set proxy to: <local_ip>:8888")
            stdscr.addstr(10, 0, "Make sure to allow connections from your device.")

            stdscr.addstr(12, 0, "Connected Devices:")
            devices = self.proxy_server.get_connected_devices()
            if devices:
                for idx, (ip, timestamp) in enumerate(devices.items(), start=1):
                    stdscr.addstr(12 + idx, 0, f"{ip} connected at {timestamp}")
            else:
                stdscr.addstr(13, 0, "No devices connected.")

            action = "[STOP]" if self.proxy_server.is_running else "[START]"
            stdscr.addstr(20, 0, f"{action} Press 's' to toggle the proxy")

            stdscr.addstr(22, 0, "[Q] Press 'q' to quit")

            stdscr.refresh()

            key = stdscr.getch()
            if key == ord('s'):
                if self.proxy_server.is_running:
                    self.proxy_server.stop_tinyproxy()
                else:
                    self.proxy_server.start_tinyproxy()
                    # Simulate adding a connected device for demonstration
                    self.proxy_server.add_connected_device(self.proxy_server.get_local_ip())
            elif key == ord('q'):
                break
