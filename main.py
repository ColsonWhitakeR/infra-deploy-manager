class DeploymentManager:
    def __init__(self):
        self.status = "Pending"

    def deploy(self):
        self.status = "Completed"
        return "Infrastructure deployed successfully"

manager = DeploymentManager()
print(manager.deploy())
