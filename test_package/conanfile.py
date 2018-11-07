#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import subprocess
import requests
import time
from conans import ConanFile, CMake, tools, RunEnvironment


class RestinioTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        bin_path = os.path.join("bin", "test_package")
        env_build = RunEnvironment(self)
        with tools.environment_append(env_build.vars):
            process = subprocess.Popen([bin_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        time.sleep(1)
        response = requests.get("http://0.0.0.0:8080")
        assert response.ok
