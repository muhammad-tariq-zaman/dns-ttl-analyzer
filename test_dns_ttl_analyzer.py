import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import unittest
from main import analyze

def row(n, t, ttl):
    return {"name": n, "type": t, "ttl_seconds": str(ttl)}

class TestTTL(unittest.TestCase):
    def test_too_low(self):
        self.assertEqual(analyze([row("a.example", "A", 30)])[0][3], "TOO LOW")
    def test_too_high(self):
        self.assertEqual(analyze([row("a.example", "A", 172800)])[0][3], "TOO HIGH")
    def test_ok(self):
        self.assertEqual(analyze([row("a.example", "A", 3600)])[0][3], "OK")
    def test_lowest_first(self):
        r = analyze([row("b.example", "A", 3600), row("a.example", "A", 30)])
        self.assertEqual(r[0][0], "a.example")
