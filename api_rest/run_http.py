import http.client, urllib.parse
import json
# https://docs.python.org/3/library/http.client.html
# GET HTTPS
# conn = http.client.HTTPSConnection("www.breakingbadapi.com", 443) # accepts a hostname, not url
# conn.request("GET", "/api/quotes/1")
# GET HTTP

# GET ALL
def get_all():
    """Gets all tasks """
    print("GET ALL")
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("GET", "/api/tasks")
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    #for t in json_data["tasks"]:
    #    print(t)
    print(response.status, response.reason)
    conn.close()

# GET ID
def get_id(t_id):
    """"Returns the information from ID, NONE if ID does not exists"""
    print("GET ID " +str(t_id))
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("GET", "/api/tasks/" + str(t_id))
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    # for t in json_data["tasks"]:
    #     print(t)
    print(response.status, response.reason)
    conn.close()


# DELETE
def delete_id(t_id):
    """"Deletes the information from ID, NONE if ID does not exists"""
    print("DELETE ID " + str(t_id))
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("DELETE", "/api/tasks/" + str(t_id))
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    # for t in json_data["tasks"]:
    #     print(t)
    print(response.status, response.reason)
    conn.close()

# PUT
def put_id(t_id,data):
    print("PUT ID " + str(t_id))
    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("PUT", "/api/tasks/" + str(t_id),str(data))
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    # for t in json_data["tasks"]:
    #     print(t)
    print(response.status, response.reason)
    conn.close()

# POST 
def post_id(data):
    print("POST ID")
    # to_bytes= bytes(json.dumps(data), "utf8")
    json_data = json.dumps(data)
    params = urllib.parse.urlencode({})
    # params = urllib.parse.urlencode(data)
    headers = {"Content-Type": "application/json"}
    # headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}

    conn = http.client.HTTPConnection("localhost",8080) # accepts a hostname, not url
    conn.request("POST", "/api/tasks",json_data, headers)
    print(conn)
    response = conn.getresponse()
    json_data = json.loads(str(response.read(), "utf-8"))
    print(json_data)
    # for t in json_data["tasks"]:
    #     print(t)
    print(response.status, response.reason)
    conn.close()



def main():
    get_all()
    print("\n")
    get_id(1)
    print("\n")
    get_id(45)
    print("\n")
    delete_id(1)
    print("\n")
    # Get all again, so verify that ID 1 is deleted
    get_all()
    print("\n")
    # data = {"t_id":0, "desc":"work" }
    # put_id(0,data)
    # print("\n")
    # data = {"desc":"new day" }
    # post_id(data)

if __name__ == "__main__":
    main()