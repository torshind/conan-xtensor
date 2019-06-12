from conans import ConanFile, CMake


class XtensorConan(ConanFile):
    name = "xtensor"
    version = "0.20.7"
    license = "BSD 3-Clause"
    homepage = "http://quantstack.net/xtensor/"
    url = "https://github.com/torshind/conan-xtensor/"
    description = "C++ tensors with broadcasting and lazy computing"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake_find_package"
    exports_sources = "*"
    requires = "xtl/0.6.4@torshind/stable", \
               "xsimd/7.2.3@torshind/stable"

    def source(self):
        self.run("git clone --branch "
                 + self.version
                 + " https://github.com/QuantStack/xtensor.git")

    def build(self):
        pass

    def package(self):
        cmake = CMake(self)
        cmake.definitions["XTENSOR_USE_XSIMD"] = "ON"
        cmake.configure(source_folder="xtensor")
        cmake.install()

    def package_info(self):
        self.info.header_only()
