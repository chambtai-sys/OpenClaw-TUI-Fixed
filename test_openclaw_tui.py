#!/usr/bin/env python3
import os
import sys
import subprocess
import unittest
import types
from importlib.machinery import SourceFileLoader

class TestOpenClawTUI(unittest.TestCase):

    def setUp(self):
        self.script_path = "./openclaw-tui"

    def test_executable_exists(self):
        self.assertTrue(os.path.exists(self.script_path), "openclaw-tui executable should exist")
        self.assertTrue(os.access(self.script_path, os.X_OK), "openclaw-tui should be executable")

    def test_help_command(self):
        res = subprocess.run([self.script_path, "--help"], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, "help command should exit with 0")
        self.assertIn("Usage:", res.stdout, "help output should contain Usage info")
        self.assertIn("TUI Tool", res.stdout, "help output should show TUI Tool title")

    def test_status_command(self):
        res = subprocess.run([self.script_path, "status"], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0, "status command should exit with 0")
        self.assertIn("OpenClaw System Diagnostics", res.stdout, "status output should have header")
        self.assertIn("System Information", res.stdout, "status output should contain system info")

    def test_invalid_command(self):
        res = subprocess.run([self.script_path, "invalidcommand"], capture_output=True, text=True)
        self.assertEqual(res.returncode, 1, "invalid command should exit with 1")
        self.assertIn("Unknown command", res.stderr, "error output should mention unknown command")

    def test_dynamic_import_helpers(self):
        # Dynamically load the non-.py executable file as a module using SourceFileLoader and exec_module
        loader = SourceFileLoader("openclaw_tui", self.script_path)
        tli_mod = types.ModuleType(loader.name)
        loader.exec_module(tli_mod)

        # Test helper presence
        node_status = tli_mod.get_node_status
        self.assertTrue(callable(node_status))

        ai_status_func = tli_mod.check_openclaw_ai_status
        self.assertTrue(callable(ai_status_func))

if __name__ == "__main__":
    unittest.main()
