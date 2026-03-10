from locust import HttpUser, task, between
import random

class WebsiteUser(HttpUser):
    wait_time = between(0.5, 2)
    
    @task(3)
    def index(self):
        self.client.get("/")
    
    @task(1)
    def metrics(self):
        self.client.get("/metrics")
    
    def on_start(self):
        """Вызывается при старте каждого пользователя"""
        print(f"User started: {self.environment.runner.user_count}")