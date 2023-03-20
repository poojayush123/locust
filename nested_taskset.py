from locust import TaskSet, constant, task, HttpUser


class MyHTTPCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Get Status of 200")
        self.interrupt(reschedule=True)


class MyAnotherHTTPCat(TaskSet):

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Get Status of 500")
        # self.interrupt()
        # self.interrupt(reschedule=True)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHTTPCat, MyAnotherHTTPCat]
    wait_time = constant(1)
