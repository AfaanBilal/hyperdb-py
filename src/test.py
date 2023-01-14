# *
# * HyperDB JS Client
# *
# * @author Afaan Bilal
# * @link   https://afaan.dev
# *

from hyperdb_py.HyperDB import HyperDB

if __name__ == '__main__':
    # Setup with address (default: http:#localhost:8765)
    hyperdb = HyperDB("http://localhost:8765")

    # OR
    # Setup with address and authentication
    # hyperdb = new HyperDB("http://localhost:8765", "username", "password")

    # Ping the server
    r = hyperdb.ping()
    print(str(r))  # True

    # Get the version number
    r = hyperdb.version()
    print(str(r))  # "[HyperDB v0.1.0 (https:#afaan.dev)]"

    # Set a value
    r = hyperdb.set("test", "value")
    print(str(r))  # value

    # Check if a key is present
    r = hyperdb.has("test")
    print(str(r))  # True

    # Get a value
    r = hyperdb.get("test")
    print(str(r))  # value

    # Get all stored data
    r = hyperdb.all()
    print(str(r))  # {test: "value"}

    # Remove a key
    r = hyperdb.delete("test")
    print(str(r))  # True

    # Delete all stored data
    r = hyperdb.clear()
    print(str(r))  # True

    # Check if the store is empty
    r = hyperdb.empty()
    print(str(r))  # True

    # Persist the store to disk
    r = hyperdb.save()
    print(str(r))  # True

    # Reload the store from disk
    r = hyperdb.reload()
    print(str(r))  # True

    # Delete all store data from memory and disk
    r = hyperdb.reset()
    print(str(r))  # True
