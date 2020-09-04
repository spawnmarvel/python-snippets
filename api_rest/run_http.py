import http.client
import json
# https://docs.python.org/3/library/http.client.html
# GET HTTPS
# conn = http.client.HTTPSConnection("www.breakingbadapi.com", 443) # accepts a hostname, not url
# conn.request("GET", "/api/quotes/1")
# GET HTTP

# GET ALL
def get_all():
    print("GET ALL")
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("GET", "/api/tasks")
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    #for t in json_data["tasks"]:
    #    print(t)
    conn.close()

# GET ID
def get_id(t_id):
    print("GET ID")
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("GET", "/api/tasks/" + str(t_id))
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    # for t in json_data["tasks"]:
    #     print(t)
    conn.close()


# DELETE
def delete_id(t_id):
    print("DELETE ID")
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("DELETE", "/api/tasks/" + str(t_id))
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    # for t in json_data["tasks"]:
    #     print(t)
    conn.close()


# PUT

# POST

def main():
    get_all()
    print("\n")
    get_id(1)
    print("\n")
    delete_id(1)

if __name__ == "__main__":
    main()