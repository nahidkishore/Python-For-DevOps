# For loop example in DevOps: Iterating through server names for deployment
servers = ['server1', 'server2', 'server3']
for server in servers:
    print(f"Deploying changes to {server}")


# While loop example in DevOps: Waiting for servers to be ready before deployment
# servers_ready = False
# while not servers_ready:
#     # Check if servers are ready
#     if all_servers_ready():
#         servers_ready = True
#         print("Servers are ready. Proceeding with deployment.")
#     else:
#         print("Waiting for servers to be ready...")
count = 0
while count < 5:
    print(count)
    count += 1