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
        self.assertIn("Unified OpenClaw System Diagnostics", res.stdout, "status output should have header")
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

        # Test get_game_dependencies_status structure
        deps_status = tli_mod.get_game_dependencies_status()
        self.assertIsInstance(deps_status, dict)
        self.assertIn("cmake", deps_status)
        self.assertIn("SDL2", deps_status)

        # Test check_game_assets_present
        # Create a temporary directory structure to test the asset locator
        os.makedirs("./temp_test_game_dir", exist_ok=True)
        try:
            # When empty, should return None
            self.assertIsNone(tli_mod.check_game_assets_present("./temp_test_game_dir"))

            # With claw.rez, should return the path
            test_file = "./temp_test_game_dir/CLAW.REZ"
            with open(test_file, "w") as f:
                f.write("dummy assets")

            found_path = tli_mod.check_game_assets_present("./temp_test_game_dir")
            self.assertIsNotNone(found_path)
            self.assertTrue(found_path.endswith("CLAW.REZ"))
        finally:
            # Cleanup
            if os.path.exists("./temp_test_game_dir/CLAW.REZ"):
                os.remove("./temp_test_game_dir/CLAW.REZ")
            if os.path.exists("./temp_test_game_dir"):
                os.rmdir("./temp_test_game_dir")

if __name__ == "__main__":
    unittest.main()
