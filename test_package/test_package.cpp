
#ifdef WIN32
#    include <winsock2.h>
#endif
#include <restinio/all.hpp>

int main() {

#ifdef WIN32
    WORD wVersionRequested = MAKEWORD(2, 2);
    WSADATA wsaData;
    WSAStartup(wVersionRequested, &wsaData);
#endif

    restinio::run(
      restinio::on_this_thread()
        .port(8080)
        .address("0.0.0.0")
        .request_handler([](auto req) {
          return req->create_response().set_body("Hello, World!").done();
        }));

    return 0;
}
