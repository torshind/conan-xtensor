from conans import ConanFile, CMake, tools


class XtensorConan(ConanFile):
    name = "xtensor"
    version = "0.20.7"
    license = "BSD 3-Clause"
    url = "http://quantstack.net/xtensor"
    description = "C++ tensors with broadcasting and lazy computing"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_find_package"
    exports_sources = "*"
    requires = "xtl/0.6.4@mdm/testing", \
               "xsimd/7.2.2@mdm/testing"

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/QuantStack/xtensor.git", self.version)

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["XTENSOR_USE_XSIMD"] = "ON"
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.info.header_only()
        self.cpp_info.libs = ["xtensor"]
