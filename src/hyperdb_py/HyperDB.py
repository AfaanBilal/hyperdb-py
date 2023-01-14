# *
# * HyperDB JS Client
# *
# * @author Afaan Bilal
# * @link   https://afaan.dev
# *

import requests


class HyperDB:
    address = ""
    username = ""
    password = ""

    authEnabled = False
    token = ""

    def __init__(self, address="http://localhost:8765", username="", password=""):
        self.address = address
        self.username = username
        self.password = password

        if self.username != "" and self.password != "":
            self.authEnabled = True

    R_PONG = "PONG"
    R_TRUE = "YES"
    R_OK = "OK"
    R_INVALID_CREDENTIALS = "INVALID_CREDENTIALS"
    R_AUTH_FAILED = "AUTH_FAILED"

    def http(self, url="", method="GET", body=""):
        headers = {}
        if self.authEnabled:
            if self.token == "":
                self.auth()

            headers["Auth"] = self.token

        response = self.sendRequest(url, method, body, headers)

        if response == self.R_AUTH_FAILED:
            self.auth()
            headers["Auth"] = self.token
            response = self.sendRequest(url, method, body, headers)

        return response

    def sendRequest(self, url="", method="GET", body="", headers={}):
        if method == "POST":
            return requests.post(self.address + "/" + url, body, headers=headers).text
        elif method == "DELETE":
            return requests.delete(self.address + "/" + url, headers=headers).text
        else:
            return requests.get(self.address + "/" + url, headers=headers).text

    def auth(self):
        authResponse = requests.post(
            self.address + "/auth",
            data="",
            headers={"username": self.username, "password": self.password}
        ).text

        if authResponse == self.R_INVALID_CREDENTIALS:
            print("Invalid credentials")
            exit(1)

        self.token = authResponse

    def ping(self):
        return self.http("ping") == self.R_PONG

    def version(self):
        return self.http()

    def has(self, key):
        return self.http("has/" + key) == self.R_TRUE

    def get(self, key):
        return self.http("data/" + key)

    def set(self, key, value):
        return self.http("data/" + key, "POST", value)

    def delete(self, key):
        return self.http("data/" + key, "DELETE") == self.R_OK

    def all(self):
        return self.http("data")

    def clear(self):
        return self.http("data", "DELETE") == self.R_OK

    def empty(self):
        return self.http("empty") == self.R_TRUE

    def save(self):
        return self.http("save", "POST") == self.R_OK

    def reload(self):
        return self.http("reload", "POST") == self.R_OK

    def reset(self):
        return self.http("reset", "DELETE") == self.R_OK
