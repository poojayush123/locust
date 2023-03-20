

from locust import User, task, constant


class MyFirstTest(User):
    weight = 1
    wait_time = constant(1)

    @task
    def launch(self):
        print("launching the url")

        @task
        def search(self):
            print("searching")

            class appsecondtest(User):
                weight = 2
                wait_time = constant(1)

                @task
                def launch2(self):
                    print("Second Test")

                    @task
                    def search2(self):
                        print("second search test")
