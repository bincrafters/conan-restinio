import os
from conans import ConanFile, tools


class RestinioConan(ConanFile):
    name = "restinio"
    license = "BSD-3-Clause"
    homepage = "https://github.com/Stiffstream/restinio"
    url = "https://github.com/bincrafters/conan-restinio"
    topics = ("conan", "restinio", "http-server", "websocket", "http")
    description = "RESTinio is a header-only C++14 library that gives you an embedded HTTP/Websocket server."
    no_copy_source = True
    requires = ("asio/1.13.0",
                "fmt/5.3.0",
                "http_parser/2.9.2")
    _source_subfolder = "source_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package(self):
        self.copy(pattern="LICENSE*", dst="licenses", src=self._source_subfolder)
        self.copy("*.hpp", dst=os.path.join("include", "restinio"), src=os.path.join(self._source_subfolder, "dev", "restinio"))
        self.copy("*.inl", dst=os.path.join("include", "restinio"), src=os.path.join(self._source_subfolder, "dev", "restinio"))

    def package_id(self):
        self.info.header_only()
