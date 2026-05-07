import unittest
from port_scanner import get_open_ports


class UnitTests(unittest.TestCase):

    def test_return_type(self):
        self.assertIsInstance(
            get_open_ports("scanme.nmap.org", [20, 80]),
            list
        )

    def test_open_ports(self):
        ports = get_open_ports("scanme.nmap.org", [20, 80])
        self.assertIn(22, ports)

    def test_verbose(self):
        result = get_open_ports("scanme.nmap.org", [20, 80], True)
        self.assertTrue(isinstance(result, str))
        self.assertIn("Open ports for", result)

    def test_invalid_hostname(self):
        self.assertEqual(
            get_open_ports("invalid.hostname", [20, 80]),
            "Error: Invalid hostname"
        )

    def test_invalid_ip(self):
        self.assertEqual(
            get_open_ports("266.255.9.10", [20, 80]),
            "Error: Invalid IP address"
        )


if __name__ == "__main__":
    unittest.main()