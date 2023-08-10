"""
Python Dictionary
Dictionaries are used to store data values in key:value pairs.
"""

car = dict(colour = 'Black', brand = "Ford", model = "Mustang", year = 2021)
print(car)
print (car['colour'])
print (car['brand'])

dict_of_cloud_services = {
    "aws": "Amazon Web Services",
    "azure": "Microsoft Azure",
    "gcp": "Google Cloud Platform"
}

print("AWS stands for", dict_of_cloud_services["aws"])
print("Azure stands for", dict_of_cloud_services["azure"])
print("GCP stands for", dict_of_cloud_services["gcp"])
print(dict_of_cloud_services.get('azure'))
dict_of_cloud_services.update({"linode":"Linode cloud"})
print(dict_of_cloud_services)