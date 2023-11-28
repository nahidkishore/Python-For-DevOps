ec2_instances_info= [
    {
        "id":"instance-0001",
        "type": "t2.micro"
        
    },
     {
        "id":"instance-0002",
        "type": "t2.medium"
        
    },
      {
        "id":"instance-0003",
        "type": "t2.large"
        
    }
]

print(ec2_instances_info[0]["id"]) 
print(ec2_instances_info[1]["type"]) 