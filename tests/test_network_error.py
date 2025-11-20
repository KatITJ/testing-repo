import json
import requests
import socket
import time
import pytest
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "..", "network_config.json")

with open(CONFIG_PATH, "r") as f:
    cfg = json.load(f)


def test_connection_error():
    print("🚀 DEBUG: test_connection_error() se está ejecutando")

    if not cfg.get("run_connection_error", False):
        print("⚠️ DEBUG: saltado por config.json (run_connection_error = false)")
        pytest.skip("Skipping: run_connection_error = false")

    try:
        requests.get("http://127.0.0.1:9999", timeout=3)
    except Exception as e:
        raise AssertionError(f"ConnectionError simulated: {repr(e)}")


def test_timeout_error():
    if not cfg.get("run_timeout_error", False):
        pytest.skip("Skipping: run_timeout_error = false")

    try:
        requests.get("https://httpstat.us/200?sleep=5000", timeout=1)
    except Exception as e:
        raise AssertionError(f"TimeoutError simulated: {repr(e)}")


def test_dns_error():
    if not cfg.get("run_dns_error", False):
        pytest.skip("Skipping: run_dns_error = false")

    try:
        requests.get("http://domain.not-exist-123.xyz")
    except Exception as e:
        raise AssertionError(f"DNS Resolution simulated: {repr(e)}")


def test_connection_reset():
    if not cfg.get("run_connection_reset", False):
        pytest.skip("Skipping: run_connection_reset = false")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("google.com", 80))
        s.shutdown(socket.SHUT_RDWR)
        time.sleep(0.1)
        s.recv(1024)
    except Exception as e:
        raise AssertionError(f"ConnectionReset simulated: {repr(e)}")
