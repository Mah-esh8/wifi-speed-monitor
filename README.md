# wifi-speed-monitor
# 🌐 WiFi Speed Monitor (iperf3)

A real-time WiFi network speed monitoring tool using iperf3 for highly accurate bandwidth measurements.

## 📋 Features

- ✅ **Real-time speed monitoring** - Continuous WiFi speed testing
- ✅ **High accuracy** - Uses iperf3 for precise measurements
- ✅ **Configurable intervals** - Test every 10, 30, or 60 seconds
- ✅ **Status indicators** - Visual feedback (SLOW, FAIR, GOOD, EXCELLENT)
- ✅ **JSON output** - Machine-readable results
- ✅ **Error handling** - Robust connection management

## 📦 Requirements

### System Requirements:
- Python 3.6+
- iperf3 (server and client)

### Python Libraries:
- Standard library only (subprocess, json, time, datetime)

## 🚀 Installation

### Step 1: Install iperf3

**Ubuntu/Debian:**
```bash
sudo apt-get install iperf3
```

**macOS:**
```bash
brew install iperf3
```

**Windows:**
- Download from: https://iperf.fr/iperf-download.php
- Or use: `choco install iperf3`

**Verify installation:**
```bash
iperf3 --version
```

### Step 2: Clone Repository

```bash
git clone https://github.com/Mah-esh8/wifi-speed-monitor.git
cd wifi-speed-monitor
```

### Step 3: Run Monitor

```bash
python wifi_speed_iperf.py
```

## 🔧 Configuration

Edit the main section in `wifi_speed_iperf.py`:

```python
if __name__ == "__main__":
    SERVER = "speedtest.server.com"  # Your iperf3 server
    TEST_INTERVAL = 10               # Seconds between tests (10, 30, 60, etc)
    TEST_DURATION = 10               # Duration of each test (5-20 seconds)
    
    monitor_with_iperf(
        server_host=SERVER,
        interval=TEST_INTERVAL,
        duration=TEST_DURATION
    )
```

## 📡 Setting Up Your Own iperf3 Server

### On the Server Machine:

```bash
# Install iperf3
sudo apt-get install iperf3

# Run iperf3 server (listen on port 5201)
iperf3 -s -D
```

### On the Client Machine:

```bash
# Update SERVER variable to your server's IP
SERVER = "192.168.1.100"  # Your server IP
```

## 💻 Usage Examples

### Basic Usage (Default - 10s interval):
```bash
python wifi_speed_iperf.py
```

### Custom Server:
Edit `wifi_speed_iperf.py`:
```python
SERVER = "192.168.1.50"  # Your iperf3 server IP
monitor_with_iperf(server_host=SERVER)
```

### Longer Test Duration:
```python
monitor_with_iperf(
    server_host="192.168.1.50",
    interval=30,      # Test every 30 seconds
    duration=20       # Each test lasts 20 seconds
)
```

## 📊 Output Example

```
============================================================
🚀 Starting WiFi Speed Monitor (iperf3)
============================================================
Server: 192.168.1.50
Test Interval: 10 seconds
Test Duration: 10 seconds
============================================================
Press Ctrl+C to stop

[2026-03-11 10:30:45] Testing network speed...
  Speed: 450.75 Mbps 🚀 EXCELLENT

[2026-03-11 10:30:55] Testing network speed...
  Speed: 445.32 Mbps 🚀 EXCELLENT

[2026-03-11 10:31:05] Testing network speed...
  Speed: 442.18 Mbps 🚀 EXCELLENT
```

## 🔍 Status Indicators

| Status | Speed Range | Emoji |
|--------|-------------|-------|
| SLOW | < 10 Mbps | ⚠️ |
| FAIR | 10-50 Mbps | ⚡ |
| GOOD | 50-100 Mbps | ✅ |
| EXCELLENT | > 100 Mbps | 🚀 |

## 🛠️ Troubleshooting

### "iperf3 is not installed"
```bash
# Ubuntu/Debian
sudo apt-get install iperf3

# macOS
brew install iperf3

# Or download from https://iperf.fr/iperf-download.php
```

### "Connection refused" Error
- Ensure iperf3 server is running: `iperf3 -s -D`
- Check correct server IP/hostname
- Verify firewall allows port 5201
- Check network connectivity: `ping <server-ip>`

### "Cannot parse JSON" Error
- Server may not be running
- Try increasing TEST_DURATION to 15-20 seconds
- Check iperf3 server logs

### High Latency/Slow Speeds
- This is normal for WiFi, especially far from router
- Speeds depend on your actual internet connection
- Use a wired iperf3 server for best results

## 📈 Performance Tips

1. **Test from same network** - Client and server should be on same network for LAN speed
2. **Use wired connection for server** - More stable baseline
3. **Increase test duration** - 15-20 seconds gives more accurate results
4. **Test multiple times** - Average the results for better accuracy
5. **Close background apps** - Reduces network congestion

## 🔗 Related Resources

- [iperf3 Documentation](https://iperf.fr/)
- [iperf3 User Guide](https://iperf.fr/iperf-doc.php)
- [Network Performance Testing](https://en.wikipedia.org/wiki/Iperf)

## 📝 License

MIT License - Feel free to use and modify

## 👨‍💻 Author

Created for real-time WiFi speed monitoring

## 🐛 Issues & Contributions

Found a bug or have suggestions? Feel free to open an issue or submit a pull request!

---

**Happy Speed Monitoring! 🚀📊**
