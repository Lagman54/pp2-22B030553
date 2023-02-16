import json


with open("data.json", "r") as file:
    data = json.load(file)

    print("Interface Status")
    print("=" * 77)
    print("{:<50} {:<18} {:<8} {:<8}".format("DN", "Description", "Speed", "MTU"))
    print("-" * 50 + " " + "-" * 18 + " " + "-" * 7 + " " + "-" * 5)
    for im in data["imdata"]:
        for obj in im:
            print("{:<50} {:<18} {:<8} {:<8}".format(
                im[obj]["attributes"]["dn"],
                im[obj]["attributes"]["descr"],
                im[obj]["attributes"]["speed"],
                im[obj]["attributes"]["mtu"],
            ))
