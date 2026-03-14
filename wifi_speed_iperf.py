import subprocess
import json
import time
from datetime import datetime

def test_speed_iperf(server_host="speedtest.server.com", duration=10):
    """
    Test speed using iperf3 (requires iperf3 server)
    
    Args:
        server_host (str): IP/hostname of iperf3 server
        duration (int): Test duration in seconds
    
    Returns:
        float: Speed in Mbps, or None if error
    """
    try:
        cmd = [
            "iperf3",
            "-c", server_host,
            "-J",  # JSON output
            "-t", str(duration)
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        data = json.loads(result.stdout)
        
        bits_per_sec = data['end']['sum_received']['bits_per_second']
        mbps = bits_per_sec / 1_000_000
        
        return mbps
    except FileNotFoundError:
        print("❌ Error: iperf3 is not installed. Please install it first:")
        print("   Ubuntu/Debian: sudo apt-get install iperf3")
        print("   macOS: brew install iperf3")
        print("   Windows: Download from https://iperf.fr/iperf-download.php")
        return None
    except json.JSONDecodeError:
        print("❌ Error: Could not parse iperf3 output. Check server connection.")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def monitor_with_iperf(server_host="speedtest.server.com", interval=10, duration=10):
    """
    Monitor WiFi speed in real-time using iperf3
    
    Args:
        server_host (str): iperf3 server address
        interval (int): Seconds between tests
        duration (int): Duration of each test in seconds
    """
    print("=" * 60)
    print("🚀 Starting WiFi Speed Monitor (iperf3)")
    print("=" * 60)
    print(f"Server: {server_host}")
    print(f"Test Interval: {interval} seconds")
    print(f"Test Duration: {duration} seconds")
    print("=" * 60)
    print("Press Ctrl+C to stop\n")
    
    try:
        while True:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{timestamp}] Testing network speed...")
            
            speed = test_speed_iperf(server_host, duration)
            
            if speed is not None:
                status = "✅ GOOD"
                if speed < 10:
                    status = "⚠️  SLOW"
                elif speed < 50:
                    status = "⚡ FAIR"
                elif speed > 100:
                    status = "🚀 EXCELLENT"
                
                print(f"  Speed: {speed:.2f} Mbps {status}\n")
            else:
                print("  Retrying in next interval...\n")
            
            time.sleep(interval)
    
    except KeyboardInterrupt:
        print("\n" + "=" * 60)
        print("❌ Monitoring stopped by user")
        print("=" * 60)

if __name__ == "__main__":
    # Configure these parameters
    SERVER = "speedtest.server.com"  # Change to your iperf3 server
    TEST_INTERVAL = 10               # Seconds between tests
    TEST_DURATION = 10               # Duration of each test
    
    monitor_with_iperf(
        server_host=SERVER,
        interval=TEST_INTERVAL,
        duration=TEST_DURATION
    )
