from conans import ConanFile, CMake, tools


class RestinioConan(ConanFile):
    name = "restinio"
    version = "0.4.8"
    license = "BSD-3"
    url = "https://bitbucket.org/sobjectizerteam/restinio-0.4"
    description = "RESTinio is a header-only C++14 library that gives you an embedded HTTP/Websocket server."
    no_copy_source = True
    requires = "asio/1.12.0@bincrafters/stable", \
                "fmt/5.2.0@bincrafters/stable", \
                "http-parser/2.8.1@bincrafters/stable"

    def source(self):
        self.run("git clone https://github.com/Stiffstream/restinio.git")
        self.run("cd restinio && git checkout v.0.4.8")

    def package(self):
        self.copy("*.hpp", dst="include/restinio", src="restinio/dev/restinio")
        self.copy("*.inl", dst="include/restinio", src="restinio/dev/restinio")

    def package_id(self):
        self.info.header_only()

